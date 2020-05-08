from tkinter import *
import ctypes

from src.controller.ControllerHome import ControllerHome

class Home(Frame):

    def __init__(self, width, height, title):
        Frame.__init__(self, master=None)
        self.master.title(title)
        self.controller = ControllerHome(home=self)
        self.set_geometry(width, height)

        self.text = Label(self.master, text='Enter text or link: ')
        self.text.grid(row=0, column=0, padx=3, pady=3)

        self.entry = Entry(self.master, width=43)
        self.entry.grid(row=0, column=1, padx=3, pady=3)

        self.bnt = Button(self.master, text='Gerar', width=10)
        self.bnt.grid(row=0, column=2, padx=3, pady=3)

        self.show_qr = Label(self.master, text='QR CODE: ')
        self.show_qr.grid(row=1, column=0, padx=3, pady=3)

        self.qr = Label(self.master, background='#fed304')
        self.qr.grid(row=2, column=0, padx=3, pady=3, columnspan=3)

        self.bnt.config(command=self.setImage)



    def set_geometry(self, width, height):
        positionRight = int(self.master.winfo_screenwidth() / 2 - width / 2)
        positionDown = int(self.master.winfo_screenheight() / 2 - height / 2)
        self.master.geometry("{}x{}+{}+{}".format(width, height, positionRight, positionDown - 40))

    def message(self, title, description):
        ctypes.windll.user32.MessageBoxW(0, description, title, 1)

    def getText(self):
        return str(self.entry.get())


    def setImage(self):
        image = self.controller.gerarQRCode()
        self.qr.config(image=image)
        self.qr.photo = image