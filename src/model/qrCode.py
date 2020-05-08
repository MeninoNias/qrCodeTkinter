import pyqrcode
from PIL import Image, ImageTk

def QRCodeGenerate():

    qr = pyqrcode.create()

    file_name = 'my qrcode'
    save_path = ''

    name = save_path+file_name+'.png'

    qr.png(name, scale=10)

    image = Image.open(name)
    image = image.relize((400,400), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)