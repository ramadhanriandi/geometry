# from Tkinter import *
# import tkFileDialog
# import ScrolledText
# import logging
# import ttk
from tkinter import filedialog
from PIL import Image

class Application(Frame):
    #Get image file
    def getImageFile(self):
        # Open browse file window
        file = filedialog.askopenfilename(initialdir=root, title='Choose a file')
        if file != None:
            data = file.read()
            getphoto = Image.open(file)
            getphoto = getphoto.resize((250, 250), Image.ANTIALIAS) 
            file.close()
            print("I got %d bytes from this file." % len(data))
            self.displayImage(getphoto)

# class Application(Frame):
    
#     # Get image file
#     def getImageFile(self):
#         # Open browse file window
#         file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
#         if file != None:
#             data = file.read()
#             getphoto = Image.open(file)
#             getphoto = getphoto.resize((250, 250), Image.ANTIALIAS) 
#             file.close()
#             print "I got %d bytes from this file." % len(data)
#             self.displayImage(getphoto)

#     # Update chosen image on image widget
#     def displayImage(self,photo):
#         img = ImageTk.PhotoImage(photo)
#         self.panel1.configure(image=img)
#         self.panel1.image = img 

#     def createWidgets(self):

#         # Set up image widget
#         Label(root,text="Source Image").grid(row=0, column=0)
#         self.panel1 = Label(root, image=None,text="No image selected",bg='#fff')
#         self.panel1.grid(row=1, column=0,rowspan=9)

#         Label(root,text="Detection Image").grid(row=0, column=1)
#         Label(root,text="No image selected",image=None,bg='#fff').grid(row=1, column=1,rowspan=9)
        
#         # Set up button list
#         Button(text="Open Image",command=self.getImageFile).grid(row=1, column=2,pady=(5, 5))
#         Button(text="Open Rule Editor").grid(row=2, column=2,pady=(5, 5))
#         Button(text="Show Rules").grid(row=3, column=2,pady=(5, 5))
#         Button(text="Show Facts").grid(row=4, column=2,pady=(5, 5))
#         Button(text="Run").grid(row=5, column=2,pady=(5, 5))


#         # Set up tree view
#         self.tree = ttk.Treeview(root, show="tree")
#         # Level 1
#         folder1=self.tree.insert("",END, text="folder 1", values=("23-Jun-17 11:05","File folder",""))
#         folder2=self.tree.insert("",END, text="folder 2", values=("23-Jun-17 11:25","TXT file","1 KB"))
#         # Level 2
#         self.tree.insert(folder1,END, text="file_1",values=("23-Jun-17 11:28","PNG file","2.6 KB"))
#         self.tree.insert(folder1,END, text="file_2", values=("23-Jun-17 11:29","PNG file","3.2 KB"))
#         self.tree.insert(folder2,END, text="file_3", values=("23-Jun-17 11:30","PNG file","3.1 KB"))
#         self.tree.grid(row=6, column=2,rowspan=2,pady=(5, 5))
#         self.tree.bind("<Double-1>", self.OnDoubleClick)

#         # Set up scrolled text
#         Label(root,text="Detection Result").grid(row=10, column=0)
#         st = ScrolledText.ScrolledText(root, state='normal',width=30,height=10)
#         st.configure(font='TkFixedFont')
#         st.grid(row=11, column=0,padx=(3, 3),pady=(0,5))

#         Label(root,text="Matched Facts").grid(row=10, column=1)
#         wt = ScrolledText.ScrolledText(root, state='normal',width=30,height=10)
#         wt.configure(font='TkFixedFont')
#         wt.grid(row=11, column=1,padx=(3, 3),pady=(0,5))

#         Label(root,text="Hit Rules").grid(row=10, column=2)
#         qt = ScrolledText.ScrolledText(root, state='normal',width=30,height=10)
#         qt.configure(font='TkFixedFont')
#         qt.grid(row=11, column=2,padx=(3, 3),pady=(0,5))

#          # Create textLogger
#         text_handler = TextHandler(st)

#         # Add the handler to logger
#         self.logger = logging.getLogger()
#         self.logger.addHandler(text_handler)

#         # Log some messages
#         self.logger.debug('debug message')
#         self.logger.info('info message')
#         self.logger.warn('warn message')
#         self.logger.error('error message')
#         self.logger.critical('critical message')

#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.createWidgets()
    
#     def OnDoubleClick(self, event):
#         item = self.tree.identify('item',event.x,event.y)
#         self.logger.error("you clicked on"+ self.tree.item(item,"text"))

# class TextHandler(logging.Handler):
#     """This class allows you to log to a Tkinter Text or ScrolledText widget"""
#     def __init__(self, text):
#         # run the regular Handler __init__
#         logging.Handler.__init__(self)
#         # Store a reference to the Text it will log to
#         self.text = text

#     def emit(self, record):
#         msg = self.format(record)
#         def append():
#             self.text.configure(state='normal')
#             self.text.insert(END, msg + '\n')
#             self.text.configure(state='disabled')
#             # Autoscroll to the bottom
#             self.text.yview(END)
#         # This is necessary because we can't modify the Text from other threads
#         self.text.after(0, append)       

# root = Tk(className='KBS Shape Detection')
# root.geometry("800x605")
# root.resizable(0, 0)

 
# app = Application(master=root)
# app.mainloop()
# root.destroy()