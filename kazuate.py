#数当てゲーム
import tkinter as tk
import random
root=tk.Tk()
root.title("数当てゲーム")
root.resizable(False, False)
root.geometry("1200x900")
root.configure(bg='lightblue')

def end():
    root.destroy()

def start():
    global label1,label2,label3,button0,button1
    label1=tk.Label(root,text="数当てゲーム",font=("Times New Roman",20))
    label2=tk.Label(root,text="eat = 桁も数も当たっている数字の数",font=("Times New Roman",20))
    label3=tk.Label(root,text="bite = 選ばれた数字だけ当たっている数字の数",font=("Times New Roman",20))
    button0=tk.Button(root,text="メインに戻る",font=("Times New Roman",20),command=end)
    button1=tk.Button(root,text="スタート",font=("Times New Roman",20),command=cli1)
    label1.pack(pady=20)
    label2.pack()
    label3.pack()
    button1.pack(pady=10)
    button0.place(x=950,y=750)

def cli1():
    global button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,frame0
    label1["text"]="桁数を選んでね"
    label1.pack(pady=25)
    label3.pack_forget()
    button1.pack_forget()
    frame0=tk.Frame(root,padx=20,pady=20)
    button1=tk.Button(frame0,text="1",font=("Times New Roman",20),command=cli2_1)
    button2=tk.Button(frame0,text="2",font=("Times New Roman",20),command=cli2_2)
    button3=tk.Button(frame0,text="3",font=("Times New Roman",20),command=cli2_3)
    button4=tk.Button(frame0,text="4",font=("Times New Roman",20),command=cli2_4)
    button5=tk.Button(frame0,text="5",font=("Times New Roman",20),command=cli2_5)
    button6=tk.Button(frame0,text="6",font=("Times New Roman",20),command=cli2_6)
    button7=tk.Button(frame0,text="7",font=("Times New Roman",20),command=cli2_7)
    button8=tk.Button(frame0,text="8",font=("Times New Roman",20),command=cli2_8)
    button9=tk.Button(frame0,text="9",font=("Times New Roman",20),command=cli2_9)
    button10=tk.Button(frame0,text="10",font=("Times New Roman",20),command=cli2_10)
    button1.grid(row=0,column=0)
    button2.grid(row=0,column=1)
    button3.grid(row=0,column=2)
    button4.grid(row=0,column=3)
    button5.grid(row=0,column=4)
    button6.grid(row=1,column=0)
    button7.grid(row=1,column=1)
    button8.grid(row=1,column=2)
    button9.grid(row=1,column=3)
    button10.grid(row=1,column=4)
    label2["text"]="数字が高いほど難易度が上がるよ"
    label2.pack(pady=30)
    frame0.pack()
    root.update()
    
def cli2_1():
    global keta
    keta=1
    cli2()

def cli2_2():
    global keta
    keta=2
    cli2()

def cli2_3():
    global keta
    keta=3
    cli2()

def cli2_4():
    global keta
    keta=4
    cli2()

def cli2_5():
    global keta
    keta=5
    cli2()

def cli2_6():
    global keta
    keta=6
    cli2()

def cli2_7():
    global keta
    keta=7
    cli2()

def cli2_8():
    global keta
    keta=8
    cli2()

def cli2_9():
    global keta
    keta=9
    cli2()

def cli2_10():
    global keta
    keta=10
    cli2()

def callback(var, indx, mode):
    global ans1,ans2,ans0
    ans1=len(sv.get())
    ans2=ans1-ans0
    if ans2>=1 and ans1==keta:
        button1["state"]="active"
    elif ans2<=0:
        button1["state"]="disable"
    ans0=ans1

def cli2():
    global frame,entry,vc,ans0,mondai,button_kazu,label4,label5,label6,label7,label8,sv,button1,button2
    frame0.pack_forget()
    label1["text"]="0～9までの中から数字を選んでね"
    kazu=["0","1","2","3","4","5","6","7","8","9"]
    r=random.sample(kazu,keta)
    mondai=""
    for i in range(keta):
        mondai=mondai+r[i]
    label2["text"]=("桁数["+str(keta)+"]")
    label2.pack(pady=10)
    label3["text"]="結果"
    label3.place(x=900,y=200)
    label4=tk.Label(root,text="",font=("Times New Roman",20))
    label5=tk.Label(root,text="",font=("Times New Roman",20))
    label6=tk.Label(root,text="",font=("Times New Roman",20))
    label7=tk.Label(root,text="",font=("Times New Roman",20))
    label8=tk.Label(root,text="",font=("Times New Roman",20))
    button1=tk.Button(root,text="GO!",font=("Times New Roman",30),command=cli3_1,state="disable")
    button2=tk.Button(root,text="答え",font=("Times New Roman",30),command=cli3_2)
    button1.place(x=200,y=300)
    button2.place(x=200,y=500)
    button0.place(x=200,y=700)
    button_kazu=0
    ans0=0
    frame = tk.Frame(root, pady=20, padx=keta,bg="lightblue")
    sv = tk.StringVar()
    sv.trace_add("write", callback)
    sv.set("")
    vc = root.register(moji)
    entry=tk.Entry(frame, validate="key", validatecommand=(vc, "%P"), textvariable=sv)
    frame.place(x=200,y=200)
    entry.pack()

def moji(string):
    return len(string) <= keta

def cli3_1():
    global ans,eat,bite,button_kazu,kai
    kai=0
    ans=""
    ans=ans+entry.get()
    eat=0
    bite=0
    for i in range(keta):
        if ans[i]==mondai[i]:
            eat=eat+1
        for j in range(keta):
            if ans[j]==mondai[i]:
                bite=bite+1
    bite=bite-eat
    button_kazu=button_kazu+1
    if button_kazu>=5:
        label8["text"]=label7["text"]
        label8.place(x=900,y=700)
    if button_kazu>=4:
        label7["text"]=label6["text"]
        label7.place(x=900,y=600)
    if button_kazu>=3:
        label6["text"]=label5["text"]
        label6.place(x=900,y=500)
    if button_kazu>=2:
        label5["text"]=label4["text"]
        label5.place(x=900,y=400)
    label4["text"]="解答 = "+str(ans)+"\neat = "+str(eat)+",bite = "+str(bite)
    label4.place(x=900,y=300)
    if eat==keta:
        cli4()
    entry.delete(0, tk.END)

def cli3_2():
    global kai
    kai=1
    cli4()

def cli4():
    global frame1,frame2,label1,label2,label3,label4,label5
    button2.place_forget()
    frame.place_forget()
    entry.pack_forget()
    label1.pack_forget()
    label2.pack_forget()
    label3.place_forget()
    label4.place_forget()
    label5.place_forget()
    label6.place_forget()
    label7.place_forget()
    label8.place_forget()
    frame1=tk.Frame(root,padx=20,pady=50,bg="red")
    frame2=tk.Frame(root,padx=20,pady=50,bg="blue")
    frame1.pack()
    frame2.pack()
    label3=tk.Label(frame2,text="答えは",font=("Times New Roman",20))
    label4=tk.Label(frame2,text=mondai,font=("Times New Roman",20))
    label5=tk.Label(frame2,text="でした！",font=("Times New Roman",20))
    if kai==0:
        label1=tk.Label(frame1,text="congratulation",font=("Haettenschweiler",75),fg="green",bg="yellow")
        label2=tk.Label(frame1,text="正解おめでとう",font=("Times New Roman",20))
    else:
        label1=tk.Label(frame1,text="",font=("Times New Roman",20),bg="lightblue")
        label2=tk.Label(frame1,text="",font=("Times New Roman",20),bg="lightblue")
    label1.pack(pady=10)
    label2.pack(pady=10)
    label3.pack(pady=10)
    label4.pack(pady=10)
    label5.pack(pady=10)
    button1["text"]="スタートに戻る"
    button1["state"]="active"
    button1["font"]="Times New Roman",20
    button1["command"]=loop
    button1.pack()
    button0.pack()

def loop():
    frame1.pack_forget()
    frame2.pack_forget()
    button1.pack_forget()
    button0.pack_forget()
    start()

start()

root.mainloop()    
