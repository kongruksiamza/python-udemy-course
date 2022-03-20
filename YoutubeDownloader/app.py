from tkinter import *
from pytube import YouTube
from moviepy.editor import *

def download():
    #ดึง URL
    video_path=link.get()
    mp4=YouTube(video_path).streams.get_highest_resolution().download()
    video_clip=VideoFileClip(mp4)
    video_clip.close()
    

#หน้าจอโปรแกรม
root=Tk()
root.title("Youtube Downloader")
canvas=Canvas(root,width=400,height=200)
canvas.pack()

#ชื่อโปรแกรม
app_title=Label(root,text="ดาวน์โหลดวิดีโอจากยูทูป",font=('Arial',20,'bold'))
canvas.create_window(200,30,window=app_title)

#ระบุ link / ปุ่มกดดาวน์โหลด
label=Label(root,text="ป้อนลิงก์วิดีโอ (URL)")
canvas.create_window(200,80,window=label)
link=Entry(root,width=60)
canvas.create_window(200,100,window=link)

downloadBtn=Button(text="ดาวน์โหลด",command=download)
canvas.create_window(200,150,window=downloadBtn)

root.mainloop()