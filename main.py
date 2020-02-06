from tkinter import ttk,Frame,Tk,Label,Button,END,scrolledtext,filedialog,Toplevel
import PIL.Image
import PIL.ImageTk
import logging
import cv2
from src.KeyFeatureDetector import *
from src.ShapeDetector import *
from dialog_windows import *


class Application(Frame):

    # Constructor
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.KFDetector = KeyFeatureDetector()
        self.path_clp='test.clp'
        self.SDetector = ShapeDetector()
        self.SDetector._reload_clp(self.path_clp)
        self.createWidgets()
    
    # Get image file
    def getImageFile(self):
        self.KFDetector = KeyFeatureDetector()
        self.SDetector = ShapeDetector()
        self.SDetector._reload_clp(self.path_clp)
        # Open browse file window
        file = filedialog.askopenfile(parent=root,mode='rb',title='Choose a file')
        if file != None:
            data = file.read()
            getphoto = PIL.Image.open(file)
            # self.logger.warn(self.item_text)
            self.KFDetector._read_file(file=file.name)
            getphoto = getphoto.resize((250, 250), PIL.Image.ANTIALIAS) 
            print("I got %d bytes from this file." % len(data))
            self.displayImage(getphoto)

            self.KFDetector._detect_corner()
            self.KFDetector._find_vertices()
            facts = self.KFDetector._extract_fact()
            self.SDetector._add_facts(facts)
    
    def openTextEditor(self):
        self.newWindow = Toplevel(root)
        self.app=TextEditor(self.newWindow)
        self.SDetector = ShapeDetector()
        self.SDetector._reload_clp(self.path_clp)

    def showRules(self):
        self.newWindow = Toplevel(root)
        self.app=ShowRules(self.newWindow)

    def showFacts(self):
        facts=self.KFDetector._get_facts()
        self.newWindow = Toplevel(root)
        self.app=ShowFacts(self.newWindow,facts=facts)


    def run(self):
        result = self.SDetector._detect("("+self.item_text[0]+")")

        self.detectionResult.config(state='normal')
        self.matchedFacts.config(state='normal')
        self.hitRules.config(state='normal')

        self.detectionResult.delete('1.0', END)
        self.matchedFacts.delete('1.0', END)
        self.hitRules.delete('1.0', END)

        if(result):
            self.detectionResult.insert(INSERT,"true\n")
        else:
            self.detectionResult.insert(INSERT,"false\n")

        for fact in self.SDetector._get_facts():
            self.matchedFacts.insert(INSERT,str(fact)+'\n')

        im = self.KFDetector._get_image()
        b,g,r = cv2.split(im)
        im = cv2.merge((r,g,b))

        img = PIL.Image.fromarray(im)
        img = img.resize((250, 250), PIL.Image.ANTIALIAS) 
        imgtk = PIL.ImageTk.PhotoImage(image=img) 
        self.panel2.configure(image=imgtk)
        self.panel2.image = imgtk
        
        # Hit Rules
        hit_rules=self.SDetector._get_hit_rule()
        for hit_rule in hit_rules:
            self.hitRules.insert(INSERT,hit_rule.name+"\n")


        self.detectionResult.config(state=DISABLED)
        self.matchedFacts.config(state=DISABLED)
        self.hitRules.config(state=DISABLED)

    # Update chosen image on image widget
    def displayImage(self,photo):
        img = PIL.ImageTk.PhotoImage(photo)
        self.panel1.configure(image=img)
        self.panel1.image = img 

    def createWidgets(self):

        # Set up image widget
        Label(root,text="Source Image").grid(row=0, column=0)
        self.panel1 = Label(root, image=None,text="No image selected",bg='#fff')
        self.panel1.grid(row=1, column=0,rowspan=9)

        Label(root,text="Detection Image").grid(row=0, column=1)
        self.panel2 = Label(root,text="No image selected",image=None,bg='#fff')
        self.panel2.grid(row=1, column=1,rowspan=9)
        
        # Set up button list
        Button(text="Open Image",command=self.getImageFile).grid(row=1, column=2,pady=(5, 5))
        Button(text="Open Rule Editor",command=self.openTextEditor).grid(row=2, column=2,pady=(5, 5))
        Button(text="Show Rules",command=self.showRules).grid(row=3, column=2,pady=(5, 5))
        Button(text="Show Facts",command=self.showFacts).grid(row=4, column=2,pady=(5, 5))
        Button(text="Run",command=self.run).grid(row=5, column=2,pady=(5, 5))


        # Set up tree view
        self.tree = ttk.Treeview(root, show="tree")
        # Level 1
        folder1=self.tree.insert("",END, text="Segitiga", values=("segitiga"))
        folder2=self.tree.insert("",END, text="Segiempat", values=("segiempat"))
        folder3=self.tree.insert("",END, text="Segi lima", values=("segilima"))
        folder4=self.tree.insert("",END, text="Segi enam", values=("segienam"))
        # Level 2
        folder10 = self.tree.insert(folder1,END, text="beraturan",values=("segitiga_beraturan"))
        folder11 = self.tree.insert(folder1,END, text="tidak beraturan",values=("segitiga_tidak_beraturan"))
        self.tree.insert(folder10,END, text="lancip",values=("segitiga_lancip"))
        self.tree.insert(folder10,END, text="tumpul", values=("segitiga_tumpul"))
        self.tree.insert(folder10,END, text="siku-siku",values=("segitiga_siku"))
        folder5=self.tree.insert(folder10,END, text="sama kaki", values=("segitiga_samakaki"))
        self.tree.insert(folder10,END, text="sama sisi", values=("segitiga_samasisi"))

        self.tree.insert(folder5,END, text="siku-siku",values=("segitiga_siku_samakaki"))
        self.tree.insert(folder5,END, text="tumpul", values=("segitiga_tumpul_samakaki"))
        self.tree.insert(folder5,END, text="lancip",values=("segitiga_lancip_samakaki"))


        folder12 = self.tree.insert(folder2,END, text="Segiempat beraturan",values=("segiempat_beraturan"))
        folder13 = self.tree.insert(folder2,END, text="Segiempat tidak beraturan",values=("segiempat_tidak_beraturan"))
        folder6=self.tree.insert(folder12,END, text="Jajaran Genjang",values=("jajarangenjang"))
        self.tree.insert(folder12,END, text="Persegi",values=("persegi"))
        self.tree.insert(folder12,END, text="Persegi Panjang",values=("persegi_panjang"))


        self.tree.insert(folder6,END, text="Jajaran Genjang beraturan",values=("jajar_genjang_beraturan"))
        self.tree.insert(folder6,END, text="Jajaran Genjang berbentuk layang-layang", values=("jajar_genjang_layang_layang"))

        folder7=self.tree.insert(folder12,END, text="Trapesium", values=("trapesium"))

        self.tree.insert(folder7,END, text="Trapesium sama kaki",values=("trapesium_sama_kaki"))
        self.tree.insert(folder7,END, text="Trapesium rata sisi", values=("trapesium_rata_sisi"))

        folder14 = self.tree.insert(folder3,END, text="beraturan",values=("segilima_beraturan"))
        folder15 = self.tree.insert(folder3,END, text="tidak beraturan",values=("segilima_tidak_beraturan"))

        folder16 = self.tree.insert(folder4,END, text="beraturan",values=("segienam_beraturan"))
        folder17 = self.tree.insert(folder4,END, text="tidak beraturan",values=("segienam_tidak_beraturan"))

        self.chosen_shape = Label(root,text="Chosen Chape :")
        self.chosen_shape.grid(row=6, column=2)

        self.tree.grid(row=7, column=2,rowspan=5,pady=(5, 5))
        self.tree.bind("<Double-1>", self.on_tree_select)

        # Set up scrolled text
        Label(root,text="Detection Result").grid(row=14, column=0)
        self.detectionResult = scrolledtext.ScrolledText(root, state='normal',width=40,height=10)
        self.detectionResult.configure(font='TkFixedFont')
        self.detectionResult.grid(row=15, column=0,padx=(3, 3),pady=(0,5))
        
        Label(root,text="Matched Facts").grid(row=14, column=1)
        self.matchedFacts = scrolledtext.ScrolledText(root, state='normal',width=40,height=10)
        self.matchedFacts.configure(font='TkFixedFont')
        self.matchedFacts.grid(row=15, column=1,padx=(3, 3),pady=(0,5))

        Label(root,text="Hit Rules").grid(row=14, column=2)
        self.hitRules = scrolledtext.ScrolledText(root, state='normal',width=40,height=10)
        self.hitRules.configure(font='TkFixedFont')
        self.hitRules.grid(row=15, column=2,padx=(3, 3),pady=(0,5))
    
    def on_tree_select(self, event):
        print("selected items:")
        for item in self.tree.selection():
            self.item_text = self.tree.item(item,"value")
            self.chosen_shape.config(text='Chosen shape : '+self.item_text[0])

root = Tk(className='KBS Shape Detection')
root.geometry("1100x680")
root.resizable(0, 0)

 
app = Application(master=root)
app.mainloop()
root.destroy()