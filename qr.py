import tkinter
from PIL import ImageTk, Image
import wifi_qrcode_generator as qr
import qrcode
qrCode = qr.wifi_qrcode('Syntax error', False, 'WPA', '111111111')
qrCode.show()


data = 'http://192.168.165.66:5000'
img1 = qrcode.make(data)
img1.save('site.png')
# creating main window
root = tkinter.Tk()
root.title("Online Site")
  
# loading the image
img = ImageTk.PhotoImage(Image.open("site.png"))
  
# reading the image
panel = tkinter.Label(root, image = img)
  
# setting the application
panel.pack(side = "bottom", fill = "both",
           expand = "yes")
def run_qr_code():
    qrCode.show()
# running the application
    root.mainloop()
    
# Use wifi_qrcode() to create a QR image

