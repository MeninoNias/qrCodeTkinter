from tkinter import *
import ctypes

class Home(Frame):

    def __init__(self, width, height, title):
        Frame.__init__(self, master=None)
        self.master.title(title)
        self.set_geometry(width, height)

        self.text = Label(self.master, text='Enter text or link: ')
        self.text.grid(row=0, column=0, padx=3, pady=3)

        self.entry = Entry(self.master, width=43)
        self.entry.grid(row=0, column=1, padx=3, pady=3)

        self.bnt = Button(self.master, text='Gerar', width=10, command=)
        self.bnt.grid(row=0, column=2, padx=3, pady=3)

        self.show_qr = Label(self.master, text='QR CODE: ')
        self.show_qr.grid(row=1, column=0, padx=3, pady=3)

        self.qr = Label(self.master)
        self.qr.grid(row=2, column=0, padx=3, pady=3, columnspan=3)

    def set_geometry(self, width, height):
        positionRight = int(self.master.winfo_screenwidth() / 2 - width / 2)
        positionDown = int(self.master.winfo_screenheight() / 2 - height / 2)
        self.master.geometry("{}x{}+{}+{}".format(width, height, positionRight, positionDown - 40))

    def message(self, title, description):
        ctypes.windll.user32.MessageBoxW(0, description, title, 1)