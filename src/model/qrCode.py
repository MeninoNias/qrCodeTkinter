import pyqrcode
from PIL import Image, ImageTk

import os

def QRCode(text):
    print(os.getcwd()+'QRCode: Model')
    qr = pyqrcode.create(text)

    file_name = 'my_qrcode'
    save_path = os.getcwd()

    name = save_path+'/'+file_name+'.png'

    print(name)

    qr.png(name, scale=10)

    image = Image.open(name)
    image = image.resize((400,400), Image.ANTIALIAS)
    return ImageTk.PhotoImage(image)