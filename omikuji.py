#おみくじ
import tkinter as tk
import random
def click_btn():
    label["text"]=random.choice(["大吉", "中吉", "小吉"," 吉 ", " 凶 ","大凶"])
    label.update()

def cli():
    root.destroy()

root=tk.Tk()
root.title("おみくじソフト")
root.resizable(False, False)
canvas=tk.Canvas(root, width=800, height=600)
canvas.pack()
gazou=tk.PhotoImage(file="miko.png")
canvas.create_image(400, 300, image=gazou)
label=tk.Label(root, text="？？", font=("Times New Roman", 120), bg="lightgreen")
label.place(x=380, y=60)
button1=tk.Button(root, text="おみくじを引く", font=("Times New Roman", 36), command=click_btn, fg="skyblue")
button1.place(x=360, y=300)
button2=tk.Button(root,text="終了",font=("Times New Roman", 36), command=cli,fg="orange")
button2.place(x=480,y=450)
root.mainloop()
