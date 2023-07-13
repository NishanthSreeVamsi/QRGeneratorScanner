from tkinter import *
from tkinter import messagebox
import pyqrcode
import cv2
import pyzbar.pyzbar as pyzbar

def scanQR():
   i = 0
   vid = cv2.VideoCapture(0)
   while i<2:
       _,f = vid.read()
       decoded = pyzbar.decode(f)
       for obj in decoded:
           lbl.config(text=f'{obj.data}')
           i += 1
       cv2.imshow('QRCode',f)
       cv2.waitKey(5)
       cv2.destroyAllWindows

ws = Tk()
ws.title('QR code Generator & Scanner')
ws.geometry('500x500')
ws.config(bg='#F3C5C5')


Button(
    ws,
    text='Scan QRCode',
    command=scanQR
).pack(pady=10)




def generate_QR():
    if len(user_input.get())!=0 :
        global qr,img
        qr = pyqrcode.create(user_input.get())
        img = BitmapImage(data = qr.xbm(scale=8))
    else:
        messagebox.showwarning('warning', 'All Fields are Required!')
    try:
        display_code()
    except:
        pass

def display_code():
    img_lbl.config(image = img)
    output.config(text="QR code of " + user_input.get())


lbl = Label(
    ws,
    text="Enter message or URL",
    bg='#C1A3A3'
    )
lbl.pack()


user_input = StringVar()
entry = Entry(
    ws,
    textvariable = user_input
    )
entry.pack(padx=10)


button = Button(
    ws,
    text = "Generate QR",
    width=15,
    command = generate_QR
    )
button.pack(pady=10)

img_lbl = Label(
    ws,
    bg='#C1A3A3')
img_lbl.pack()

output = Label(
    ws,
    text="",
    bg='#C1A3A3'
    )
output.pack()

ws.mainloop()