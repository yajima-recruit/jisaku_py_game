#文字探し
import tkinter as tk
import random
import datetime
root=tk.Tk()
root.title("文字探し")
root.resizable(False, False)
root.geometry("1200x900")
root.configure(bg='lightgreen')
def cli0():
    root.destroy()
    
def cli1():
    global st,r,frame,buttonA,buttonB,buttonC,buttonD,buttonE,buttonF,buttonG,buttonH,buttonI,buttonJ,buttonK,buttonL,buttonM,buttonN,buttonO,buttonP,buttonQ,buttonR,buttonS,buttonT,buttonU,buttonV,buttonW,buttonX,buttonY,buttonZ
    button1.pack_forget()
    ALP = [
        "A","B","C","D","E","F","G",
        "H","I","J","K","L","M","N",
        "O","P","Q","R","S","T","U",
        "V","W","X","Y","Z"
    ]
    r = random.choice(ALP)
    alp = " "
    for i in ALP:
        if i != r:
            alp = alp + i
    label1["text"]=alp
    label1["font"]=("Times New Roman",30)
    label1.pack(pady=30)
    label2["text"]="抜けているアルファベットは?"
    label2["font"]=("Times New Roman",20)
    label2.pack(pady=30)
    st = datetime.datetime.now()
    frame=tk.Frame(root,width=0,height=0)
    frame.pack()
    buttonA=tk.Button(frame,text="A",font=("Times New Roman",25),command=A)
    buttonB=tk.Button(frame,text="B",font=("Times New Roman",25),command=B)
    buttonC=tk.Button(frame,text="C",font=("Times New Roman",25),command=C)
    buttonD=tk.Button(frame,text="D",font=("Times New Roman",25),command=D)
    buttonE=tk.Button(frame,text="E",font=("Times New Roman",25),command=E)
    buttonF=tk.Button(frame,text="F",font=("Times New Roman",25),command=F)
    buttonG=tk.Button(frame,text="G",font=("Times New Roman",25),command=G)
    buttonH=tk.Button(frame,text="H",font=("Times New Roman",25),command=H)
    buttonI=tk.Button(frame,text="I",font=("Times New Roman",25),command=I)
    buttonJ=tk.Button(frame,text="J",font=("Times New Roman",25),command=J)
    buttonK=tk.Button(frame,text="K",font=("Times New Roman",25),command=K)
    buttonL=tk.Button(frame,text="L",font=("Times New Roman",25),command=L)
    buttonM=tk.Button(frame,text="M",font=("Times New Roman",25),command=M)
    buttonN=tk.Button(frame,text="N",font=("Times New Roman",25),command=N)
    buttonO=tk.Button(frame,text="O",font=("Times New Roman",25),command=O)
    buttonP=tk.Button(frame,text="P",font=("Times New Roman",25),command=P)
    buttonQ=tk.Button(frame,text="Q",font=("Times New Roman",25),command=Q)
    buttonR=tk.Button(frame,text="R",font=("Times New Roman",25),command=R)
    buttonS=tk.Button(frame,text="S",font=("Times New Roman",25),command=S)
    buttonT=tk.Button(frame,text="T",font=("Times New Roman",25),command=T)
    buttonU=tk.Button(frame,text="U",font=("Times New Roman",25),command=U)
    buttonV=tk.Button(frame,text="V",font=("Times New Roman",25),command=V)
    buttonW=tk.Button(frame,text="W",font=("Times New Roman",25),command=W)
    buttonX=tk.Button(frame,text="X",font=("Times New Roman",25),command=X)
    buttonY=tk.Button(frame,text="Y",font=("Times New Roman",25),command=Y)
    buttonZ=tk.Button(frame,text="Z",font=("Times New Roman",25),command=Z)
    buttonA.grid(row=0,column=0)
    buttonB.grid(row=0,column=1)
    buttonC.grid(row=0,column=2)
    buttonD.grid(row=0,column=3)
    buttonE.grid(row=0,column=4)
    buttonF.grid(row=0,column=5)
    buttonG.grid(row=0,column=6)
    buttonH.grid(row=0,column=7)
    buttonI.grid(row=0,column=8)
    buttonJ.grid(row=0,column=9)
    buttonK.grid(row=0,column=10)
    buttonL.grid(row=0,column=11)
    buttonM.grid(row=0,column=12)
    buttonN.grid(row=1,column=0)
    buttonO.grid(row=1,column=1)
    buttonP.grid(row=1,column=2)
    buttonQ.grid(row=1,column=3)
    buttonR.grid(row=1,column=4)
    buttonS.grid(row=1,column=5)
    buttonT.grid(row=1,column=6)
    buttonU.grid(row=1,column=7)
    buttonV.grid(row=1,column=8)
    buttonW.grid(row=1,column=9)
    buttonX.grid(row=1,column=10)
    buttonY.grid(row=1,column=11)
    buttonZ.grid(row=1,column=12)
    
def A():
    global ans
    ans="A"
    cli2()
def B():
    global ans
    ans="B"
    cli2()
def C():
    global ans
    ans="C"
    cli2()
def D():
    global ans
    ans="D"
    cli2()
def E():
    global ans
    ans="E"
    cli2()
def F():
    global ans
    ans="F"
    cli2()
def G():
    global ans
    ans="G"
    cli2()
def H():
    global ans
    ans="H"
    cli2()
def I():
    global ans
    ans="I"
    cli2()
def J():
    global ans
    ans="J"
    cli2()
def K():
    global ans
    ans="K"
    cli2()
def L():
    global ans
    ans="L"
    cli2()
def M():
    global ans
    ans="M"
    cli2()
def N():
    global ans
    ans="N"
    cli2()
def O():
    global ans
    ans="O"
    cli2()
def P():
    global ans
    ans="P"
    cli2()
def Q():
    global ans
    ans="Q"
    cli2()
def R():
    global ans
    ans="R"
    cli2()
def S():
    global ans
    ans="S"
    cli2()
def T():
    global ans
    ans="T"
    cli2()
def U():
    global ans
    ans="U"
    cli2()
def V():
    global ans
    ans="V"
    cli2()
def W():
    global ans
    ans="W"
    cli2()
def X():
    global ans
    ans="X"
    cli2()
def Y():
    global ans
    ans="Y"
    cli2()
def Z():
    global ans
    ans="Z"
    cli2()

def cli2():
    global label3,label4,label5,button3
    label3=tk.Label(root,text=" ",font=("Times New Roman",40))
    if ans == r:
        et = datetime.datetime.now()
        label1.pack_forget()
        label2.pack_forget()
        frame.pack_forget()
        label3["text"]="正解です"
        label3.pack(pady=30)
        label4=tk.Label(root,text=str((et-st).seconds)+"秒掛かりました",font=("Times New Roman",20))
        label4.pack(pady=20)
        button1.pack_forget()
        label5=tk.Label(root,text="もう一度やりますか？",font=("Times New Roman",30))
        label5.pack(pady=20)
        button3=tk.Button(root,text="YES!",font=("Times New Roman",24),command=cli3)
        button0.place(x=700,y=600)
        button3.place(x=400,y=600)
        root.update()
    else:
        label3["text"]="不正解です"
        label3["font"]=("Times New Roman",20)
        label3.place(x=300,y=800)
        root.update()
        
def cli3():
    global label1,label2,button1
    label3.pack_forget()
    label4.pack_forget()
    label5.pack_forget()
    button3.place_forget()
    label1=tk.Label(root,text="ボタンを押すとアルファベットが表示されるよ",font=("Times New Roman",18))
    label2=tk.Label(root,text="足りない文字があるから見つけたら書き込んでね",font=("Times New Roman",18))
    button1=tk.Button(root,text="スタート",font=("Times New Roman",24),command=cli1)
    label1.pack(pady=20)
    label2.pack(pady=60)
    button1.pack(pady=300)
    button0.place(x=950,y=750)
    root.update()

label1=tk.Label(root,text="ボタンを押すとアルファベットが表示されるよ",font=("Times New Roman",18))
label2=tk.Label(root,text="足りない文字があるから見つけたら書き込んでね",font=("Times New Roman",18))
button1=tk.Button(root,text="スタート",font=("Times New Roman",24),command=cli1)
button0=tk.Button(root,text="メインに戻る",font=("Times New Roman",24),command=cli0)
button0.place(x=950,y=750)
label1.pack(pady=20)
label2.pack(pady=60)
button1.pack(pady=300)

root.mainloop()