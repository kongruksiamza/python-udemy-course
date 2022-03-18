from tkinter import *
import pyqrcode
import png
from PIL import ImageTk,Image

def generateQRCode():
    #ดึงข้อมูล link มาสร้าง QRCode
    link_name = name_entry.get()
    link=link_entry.get()
    file_name=link_name+".png"
    #สร้าง QRCode
    url=pyqrcode.create(link)
    url.png(file_name,scale=5)
    #แสดงภาพ QRCode
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label=Label(image=image)
    image_label.image=image
    canvas.create_window(200,370,window=image_label)


root=Tk()
root.title("QRCode Generator")
canvas=Canvas(root,width=400,height=500)
canvas.pack()
#ชื่อโปรแกรม
app_label=Label(root,text="QRCode Generator",font=('Arial',20,'bold'))
canvas.create_window(200,50,window=app_label)
#ระบุชื่อพร้อมกับลิงก์ -> QRCode
name_label=Label(root,text="ชื่อคิวอาร์โค้ด")
canvas.create_window(200,100,window=name_label)

link_label=Label(root,text="URL")
canvas.create_window(200,160,window=link_label)

#สร้าง Textbox
name_entry=Entry(root)
canvas.create_window(200,130,window=name_entry)

link_entry=Entry(root)
canvas.create_window(200,180,window=link_entry)

#ปุ่มสร้าง QRCode
button=Button(text="สร้างคิวอาร์โค้ด",command=generateQRCode)
canvas.create_window(200,230,window=button)

root.mainloop()