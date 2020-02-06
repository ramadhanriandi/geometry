from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from tkinter import filedialog
import os

class TextEditor(Frame):
    def __init__(self, parent=None, file=None):
        Frame.__init__(self, parent)
        self.frm = Frame(parent)
        self.frm.pack(fill=X)
        # self.buatJudul()
        parent.title('Rules Editor')
        self.buatTombol()
        self.kolomTeksUtama()
        self.settext(text='',file=file)
        self.kolomTeks.config(font=('DejaVu Sans Mono', 10))
        self.path = ''
        text = self.readFile('test.clp')
        self.kolomTeks.delete('0.1',END)
        self.kolomTeks.insert(END, text)

    def buatTombol(self):
        Button(self.frm, text='Simpan',relief='flat',  command=self.perintahSimpan).pack(side=LEFT)

    def kolomTeksUtama(self):
        scroll = Scrollbar(self)
        kolomTeks = Text(self, relief=SUNKEN)
        scroll.config(command=kolomTeks.yview)
        kolomTeks.config(yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT, fill=Y)
        kolomTeks.pack(side=LEFT, expand=YES, fill=BOTH)
        self.kolomTeks = kolomTeks
        self.pack(expand=YES, fill=BOTH)

    def perintahSimpan(self):
        print(self.path)
        if self.path:
            alltext = self.gettext()
            open(self.path, 'w').write(alltext)
            messagebox.showinfo('Berhasil', 'Selamat File telah tersimpan ! ')
        else:
            tipeFile = [('Text file', '*.txt'), ('Python file', '*asdf.py'), ('All files', '.*')]
            alltext = self.gettext()
            open('test.clp', 'w').write(alltext)
            self.master.destroy()

    def settext(self, text='', file=None):
        if file:
            text = open(file, 'r').read()
        self.kolomTeks.delete('1.0', END)
        self.kolomTeks.insert('1.0', text)
        self.kolomTeks.mark_set(INSERT, '1.0')
        self.kolomTeks.focus()

    def gettext(self):
        return self.kolomTeks.get('1.0', END+'-1c')

    def buatJudul(self):
        top = Frame(root)
        top.pack(fill=BOTH, expand=1, padx=17, pady=5)
        judul = Label(top, text="Judul : ")
        judul.pack(side="left")
        self.kolomJudul = Entry(top)
        self.kolomJudul.pack(side="left")

    def bukaFile(self):
        extensiFile = [ ('All files', '*'), ('Text files', '*.txt'),('Python files', '*.py')]
        buka = filedialog.askopenfilename(filetypes = extensiFile)

    def readFile(self, filename):
        try:
            f = open(filename, "r")
            text = f.read()
            return text
        except:
            messagebox.showerror("Error!!","Maaf file tidak dapat dibuka ! :) \nsabar ya..")
            return None

class ShowFacts(Frame):
    def __init__(self, parent=None, file=None,facts=None):
        Frame.__init__(self, parent)
        parent.title('Show Facts')
        self.showfacts = scrolledtext.ScrolledText(parent, state='normal',width=40,height=20)
        self.showfacts.configure(font='TkFixedFont')
        self.showfacts.grid(row=0, column=0,padx=(5, 5),pady=(5,5))
        for fact in facts:
            self.showfacts.insert(INSERT,fact+'\n')
        self.showfacts.config(state=DISABLED)

class ShowRules(Frame):
    def __init__(self, parent=None, file=None):
        Frame.__init__(self, parent)
        parent.title('Show Rules')
        self.showrules = scrolledtext.ScrolledText(parent, state='normal',width=40,height=20)
        self.showrules.configure(font='TkFixedFont')
        self.showrules.grid(row=0, column=0,padx=(5, 5),pady=(5,5))
        rules = open('test.clp', 'r').read()
        self.showrules.delete('1.0', END)
        self.showrules.insert('1.0', rules)
        self.showrules.mark_set(INSERT, '1.0')
        self.showrules.focus()
        self.showrules.config(state=DISABLED)