from tkinter import *
from tkinter import messagebox
import os
import sys

py = sys.executable

# creating window
class MainWin(Tk):
    def __init__(self):
        super().__init__()

        self.resizable(width=False, height=False)
        self.geometry('350x350')
        self.configure(bg="#ADD8E6")
        self.title("STEGANOGRAPHY")
        self.a = StringVar()
        self.b = StringVar()
        self.mymenu = Menu(self)

        def one():
            os.system('%s %s' % (py, 'encrypt.py'))

        def two():
            os.system('%s %s' % (py, 'decrypt.py'))

        def log():
            conf = messagebox.askyesno("Confirm", "Are you sure you want to quit?")
            if conf:
                self.destroy()
                os.system('%s %s' % (py, 'main.py'))

        
        self.label = Label(self, text="Select any option: ", bg='#ADD8E6', fg='white', font=('Arial',20,'bold')).place(x=30, y=10)

        self.button = Button(self, text="Encryption",bg='#495057',fg='#f9f9f9', command=one, width=10, height=2,
                             font=('Arial',15,'bold'))
        self.button.place(x=45, y=70, width=260)

        self.button1 = Button(self, text="Decryption",bg='#495057',fg='#f9f9f9', command=two, width=10, height=2,
                              font=('Arial',15,'bold'))
        self.button1.place(x=45, y=140, width=260)


        self.button_quit = Button(self, text="Quit", bg='#dc3545',fg='white', command=log, width=10, height=2,
                                  font='Helvetica')
        self.button_quit.place(x=125, y=280)

MainWin().mainloop()
                                       