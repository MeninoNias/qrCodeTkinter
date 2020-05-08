from src.model.qrCode import QRCode
import os

class ControllerHome:

    def __init__(self, home):
        self.home = home

    def gerarQRCode(self):
        print('gerarQRCode: Controller')
        text = self.home.getText()
        print(os.getcwd() + 'gerarQRCode: Controller -->'+ text)
        return QRCode(text)
