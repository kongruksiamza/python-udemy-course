from cgitb import text
from tkinter import *
from gtts import gTTS

def convertToMP3():
    #ดึงข้อความมาใช้งาน
    word=text_entry.get()
    language='th'
    #แปลงข้อความเป็นเสียง
    output=gTTS(text=word,lang=language,slow=False)
    output.save("sound.mp3")

root=Tk()
root.title("โปรแกรมแปลงข้อความเป็นเสียง (รองรับภาษาไทย)")
canvas=Canvas(root,width=400,height=300)
canvas.pack()

app_label=Label(text="แปลงข้อความเป็นเสียง",font=('Arial',20,'bold'))
canvas.create_window(200,100,window=app_label)

text_entry=Entry(root)
canvas.create_window(200,180,window=text_entry)

button=Button(text="แปลงเป็นเสียง",command=convertToMP3)
canvas.create_window(200,230,window=button)

root.mainloop()