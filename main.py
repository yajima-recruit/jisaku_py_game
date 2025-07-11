#メインプログラム
import tkinter as tk
import random
import datetime
import winsound
def moji():
    global root
    root.destroy()
    root=tk.Tk()
    root.title("文字探し")
    root.resizable(False, False)
    root.geometry("1200x900")
    root.configure(bg='ForestGreen')
    def cli0():
        root.destroy()
        main_game()
        
    def cli1():
        global st,r,frame
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
        label2.pack(pady=80)
        frame=tk.Frame(root,width=0,height=0,bg="ForestGreen")
        frame.pack()
        st=datetime.datetime.now()
        buttonA=tk.Button(frame,text="A",font=("Times New Roman",25),command=A,width=3)
        buttonB=tk.Button(frame,text="B",font=("Times New Roman",25),command=B,width=3)
        buttonC=tk.Button(frame,text="C",font=("Times New Roman",25),command=C,width=3)
        buttonD=tk.Button(frame,text="D",font=("Times New Roman",25),command=D,width=3)
        buttonE=tk.Button(frame,text="E",font=("Times New Roman",25),command=E,width=3)
        buttonF=tk.Button(frame,text="F",font=("Times New Roman",25),command=F,width=3)
        buttonG=tk.Button(frame,text="G",font=("Times New Roman",25),command=G,width=3)
        buttonH=tk.Button(frame,text="H",font=("Times New Roman",25),command=H,width=3)
        buttonI=tk.Button(frame,text="I",font=("Times New Roman",25),command=I,width=3)
        buttonJ=tk.Button(frame,text="J",font=("Times New Roman",25),command=J,width=3)
        buttonK=tk.Button(frame,text="K",font=("Times New Roman",25),command=K,width=3)
        buttonL=tk.Button(frame,text="L",font=("Times New Roman",25),command=L,width=3)
        buttonM=tk.Button(frame,text="M",font=("Times New Roman",25),command=M,width=3)
        buttonN=tk.Button(frame,text="N",font=("Times New Roman",25),command=N,width=3)
        buttonO=tk.Button(frame,text="O",font=("Times New Roman",25),command=O,width=3)
        buttonP=tk.Button(frame,text="P",font=("Times New Roman",25),command=P,width=3)
        buttonQ=tk.Button(frame,text="Q",font=("Times New Roman",25),command=Q,width=3)
        buttonR=tk.Button(frame,text="R",font=("Times New Roman",25),command=R,width=3)
        buttonS=tk.Button(frame,text="S",font=("Times New Roman",25),command=S,width=3)
        buttonT=tk.Button(frame,text="T",font=("Times New Roman",25),command=T,width=3)
        buttonU=tk.Button(frame,text="U",font=("Times New Roman",25),command=U,width=3)
        buttonV=tk.Button(frame,text="V",font=("Times New Roman",25),command=V,width=3)
        buttonW=tk.Button(frame,text="W",font=("Times New Roman",25),command=W,width=3)
        buttonX=tk.Button(frame,text="X",font=("Times New Roman",25),command=X,width=3)
        buttonY=tk.Button(frame,text="Y",font=("Times New Roman",25),command=Y,width=3)
        buttonZ=tk.Button(frame,text="Z",font=("Times New Roman",25),command=Z,width=3)
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
        label3.pack_forget()
        label4.pack_forget()
        label5.pack_forget()
        button3.place_forget()
        button0.place_forget()
        start()
    
    def start():
        global label1,label2,button1,button0
        label1=tk.Label(root,text="ボタンを押すとアルファベットが表示されるよ",font=("Times New Roman",18))
        label2=tk.Label(root,text="足りない文字があるから見つけたら書き込んでね",font=("Times New Roman",18))
        button1=tk.Button(root,text="スタート",font=("Times New Roman",24),command=cli1)
        button0=tk.Button(root,text="ゲームランドに戻る",font=("Times New Roman",24),command=cli0)
        button0.place(x=850,y=750)
        label1.pack(pady=20)
        label2.pack(pady=60)
        button1.pack(pady=300)
    start()
    root.mainloop()

def kazuate():
    global root
    root.destroy()
    root=tk.Tk()
    root.title("数当てゲーム")
    root.resizable(False, False)
    root.geometry("1200x900")
    root.configure(bg='lightblue')
    def end():
        root.destroy()
        main_game()
    def start():
        global label1,label2,label3,button0,button1,frame1,frame2
        frame1=tk.Frame(root,bg='lightblue')
        frame2=tk.Frame(frame1,bg='lightblue')
        label1=tk.Label(frame1,text="数当てゲーム",font=("Times New Roman",20))
        label2=tk.Label(frame2,text="eat = 桁も数も当たっている数字の数",font=("Times New Roman",20))
        label3=tk.Label(frame2,text="bite = 選ばれた数字だけ当たっている数字の数",font=("Times New Roman",20))
        button0=tk.Button(root,text="ゲームランドに戻る",font=("Times New Roman",20),command=end)
        button1=tk.Button(root,text="スタート",font=("Times New Roman",20),command=cli1)
        frame1.pack(expand=True,anchor=tk.CENTER)
        label1.pack()
        frame2.pack(pady=50)
        label2.pack(pady=20)
        label3.pack(pady=20)
        button1.pack(expand=True,anchor=tk.N)
        button0.place(x=850,y=750)
    def cli1():
        global button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,frame0,label1,label2
        frame1.destroy()
        button1.destroy()
        label1=tk.Label(root,text="桁数を選んでね",font=("Times New Roman",20))
        label1.pack(pady=25)
        label2=tk.Label(root,text="数字が高いほど難易度が上がるよ",font=("Times New Roman",20))
        label2.pack(pady=30)
        frame0=tk.Frame(root,padx=20,pady=20,bg='lightblue')
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
        button1.grid(row=0,column=0,padx=25,pady=50)
        button2.grid(row=0,column=1,padx=25,pady=50)
        button3.grid(row=0,column=2,padx=25,pady=50)
        button4.grid(row=0,column=3,padx=25,pady=50)
        button5.grid(row=0,column=4,padx=25,pady=50)
        button6.grid(row=1,column=0,padx=25,pady=50)
        button7.grid(row=1,column=1,padx=25,pady=50)
        button8.grid(row=1,column=2,padx=25,pady=50)
        button9.grid(row=1,column=3,padx=25,pady=50)
        button10.grid(row=1,column=4,padx=25,pady=50)
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
        global frame,entry,vc,ans0,mondai,button_kazu,label1,label2,label3,label4,label5,label6,label7,label8,sv,button1,button2
        frame0.pack_forget()
        label2.pack_forget()
        label1["text"]="0～9までの中から数字を選んでね"
        kazu=["0","1","2","3","4","5","6","7","8","9"]
        r=random.sample(kazu,keta)
        mondai=""
        for i in range(keta):
            mondai=mondai+r[i]
        label2=tk.Label(root,text="桁数["+str(keta)+"]",font=("Times New Roman",20))
        label2.pack(pady=10)
        label3=tk.Label(root,text="結果",font=("Times New Roman",20))
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
        global frame1,frame2,label1,label2,label3,label4,label5,button3,button0
        button0.place_forget()
        button1.place_forget()
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
        frame1=tk.Frame(root,bg='lightblue')
        frame2=tk.Frame(root,bg='lightblue')
        frame1.pack(expand=True,anchor=tk.CENTER)
        frame2.pack(expand=True,anchor=tk.N)
        if kai==0:
            label1=tk.Label(frame1,text="congratulation",font=("Haettenschweiler",75),fg="green",bg="yellow")
            label2=tk.Label(frame1,text="正解おめでとう",font=("Times New Roman",20))
            label1.pack(pady=10)
            label2.pack(pady=10)
        else:
            label1=tk.Label(frame1,text="答えは"+str(mondai)+"でした！",font=("Haettenschweiler",75),fg="green",bg="yellow")
            label1.pack(pady=10)
        button3=tk.Button(frame2,text="スタートに戻る",font=("Times New Roman",20),command=loop)
        button3.pack(pady=20)
        button0=tk.Button(frame2,text="ゲームランドに戻る",font=("Times New Roman",20),command=end)
        button0.pack(pady=20)
    
    def loop():
        frame1.destroy()
        frame2.destroy()
        start()
    start()
    root.mainloop()

def meiro():
    global root,after_id
    root.destroy()
    root=tk.Tk()
    root.title("一筆書き迷路")
    root.resizable(False, False)
    root.geometry("1200x900")
    root.configure(bg='orange')
    after_id=None
    
    def end():
        root.destroy()
        main_game()
    
    def start():
        global frame1,canvas1,img,label1,label2,label3,label4,button1,button0,key,label5
        label1=tk.Label(root,text="一筆書き迷路！",font=("ＭＳ Ｐ明朝",50))
        label1.pack(pady=30)
        frame1=tk.Frame(root,width=500,height=183,bg='violet')
        canvas1=tk.Canvas(frame1,width=183, height=183,bg="purple")
        img=tk.PhotoImage(file="mimi_s_183.png")
        canvas1.create_image(91.5,91.5, image=img)
        label2=tk.Label(frame1,text="やあ！僕はシュガー！",font=('UD デジタル 教科書体 N-B',20),bg='violet')
        label3=tk.Label(frame1,text="僕をゴールまで連れてって！",font=('UD デジタル 教科書体 N-B',20),bg='violet')
        label2.grid(row=0,column=1)
        label3.grid(row=1,column=1)
        canvas1.grid(row=0,column=0,rowspan=2)
        frame1.pack()
        label5=tk.Label(root,text="w a s dで移動、Shiftでリセットできるよ！",font=("Century Schoolbook",20))
        label4=tk.Label(root,text="準備はいい？",font=("Century Schoolbook",20))
        button1=tk.Button(root,text="スタート！",font=('Showcard Gothic',20),command=cli1)
        button0=tk.Button(root,text="ゲームランドに戻る",font=('Lucida Sans Unicode',20),command=end)
        label5.pack(pady=20)
        label4.pack(pady=20)
        button1.pack(pady=20)
        button0.place(x=950,y=750)
        key=""
    
    def cli1():
        global button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,buttonR,restart_count,reset_count,loop0_count,stage_lve
        label4.pack_forget()
        label5.pack_forget()
        button1.pack_forget()
        canvas1.grid_forget()
        label2.grid_forget()
        label3.grid_forget()
        frame1["bg"]="orange"
        label1["text"]="レベルの選択"
        button1=tk.Button(frame1,text="1",font=('Showcard Gothic',20),command=lve1)
        button2=tk.Button(frame1,text="2",font=('Showcard Gothic',20),command=lve2)
        button3=tk.Button(frame1,text="3",font=('Showcard Gothic',20),command=lve3)
        button4=tk.Button(frame1,text="4",font=('Showcard Gothic',20),command=lve4)
        button5=tk.Button(frame1,text="5",font=('Showcard Gothic',20),command=lve5)
        button6=tk.Button(frame1,text="6",font=('Showcard Gothic',20),command=lve6)
        button7=tk.Button(frame1,text="7",font=('Showcard Gothic',20),command=lve7)
        button8=tk.Button(frame1,text="8",font=('Showcard Gothic',20),command=lve8)
        button9=tk.Button(frame1,text="9",font=('Showcard Gothic',20),command=lve9)
        button10=tk.Button(frame1,text="10",font=('Showcard Gothic',20),command=lve10)
        buttonR=tk.Button(root,text="ランダム",font=('Showcard Gothic',20),command=lveR)
        button1.grid(row=0,column=0,padx=50,pady=50)
        button2.grid(row=0,column=1,padx=50,pady=50)
        button3.grid(row=0,column=2,padx=50,pady=50)
        button4.grid(row=0,column=3,padx=50,pady=50)
        button5.grid(row=0,column=4,padx=50,pady=50)
        button6.grid(row=1,column=0,padx=50,pady=50)
        button7.grid(row=1,column=1,padx=50,pady=50)
        button8.grid(row=1,column=2,padx=50,pady=50)
        button9.grid(row=1,column=3,padx=50,pady=50)
        button10.grid(row=1,column=4,padx=50,pady=50)
        buttonR.pack(pady=50)
        restart_count=0
        reset_count=0
        loop0_count=0
        stage_lve=0
    
    def preprocessor():
        global img_s1,img_s2,img_s3,img_g,img1,img2,img3,img4,img5,imgW,num,yuka,buttonRe,img1_2,img2_2,img3_2,img4_2,img5_2,img_g2,img_g3,imgW2,imgW3,button1
        global imgWS,imgWS2,imgWC,imgWC2,num2,imgN2,imgN,imgE2,imgE,imgS,imgS2,imgW_1,imgW_2,tag_label,imgWB,img6,img7,img8,img9,img1_3,img2_3,img3_3,img4_3,img5_3
        label1.pack_forget()
        buttonR.pack_forget()
        button0.place_forget()
        button1.grid_forget()
        button2.grid_forget()
        button3.grid_forget()
        button4.grid_forget()
        button5.grid_forget()
        button6.grid_forget()
        button7.grid_forget()
        button8.grid_forget()
        button9.grid_forget()
        button10.grid_forget()
        frame1.pack_forget()
        img_s1=tk.PhotoImage(file="mimi_s_80.png")
        img_s2=tk.PhotoImage(file="mimi_s_50.png")
        img_s3=tk.PhotoImage(file="mimi_s_60.png")
        img_g=tk.PhotoImage(file="text_goal_80.png")
        img_g2=tk.PhotoImage(file="text_goal_50.png")
        img_g3=tk.PhotoImage(file="text_goal_60.png")
        img1=tk.PhotoImage(file="num1.png")
        img2=tk.PhotoImage(file="num2.png")
        img3=tk.PhotoImage(file="num3.png")
        img4=tk.PhotoImage(file="num4.png")
        img5=tk.PhotoImage(file="num5.png")
        img1_2=tk.PhotoImage(file="num1_60.png")
        img2_2=tk.PhotoImage(file="num2_60.png")
        img3_2=tk.PhotoImage(file="num3_60.png")
        img4_2=tk.PhotoImage(file="num4_60.png")
        img5_2=tk.PhotoImage(file="num5_60.png")
        img1_3=tk.PhotoImage(file="num1_50.png")
        img2_3=tk.PhotoImage(file="num2_50.png")
        img3_3=tk.PhotoImage(file="num3_50.png")
        img4_3=tk.PhotoImage(file="num4_50.png")
        img5_3=tk.PhotoImage(file="num5_50.png")
        img6=tk.PhotoImage(file="num6.png")
        img7=tk.PhotoImage(file="num7.png")
        img8=tk.PhotoImage(file="num8.png")
        img9=tk.PhotoImage(file="num9.png")
        imgW=tk.PhotoImage(file="W_80.png")
        imgW2=tk.PhotoImage(file="W_50.png")
        imgW3=tk.PhotoImage(file="W_60.png")
        imgWS=tk.PhotoImage(file="W_S_60.png")
        imgWS2=tk.PhotoImage(file="W_S_50.png")
        imgWC=tk.PhotoImage(file="W_C_60.png")
        imgWC2=tk.PhotoImage(file="W_C_50.png")
        imgWB=tk.PhotoImage(file="W_B_50.png")
        imgN=tk.PhotoImage(file="yajirusi_N_50.png")
        imgN2=tk.PhotoImage(file="yajirusi_N_60.png")
        imgE=tk.PhotoImage(file="yajirusi_E_50.png")
        imgE2=tk.PhotoImage(file="yajirusi_E_60.png")
        imgS=tk.PhotoImage(file="yajirusi_S_50.png")
        imgS2=tk.PhotoImage(file="yajirusi_S_60.png")
        imgW_1=tk.PhotoImage(file="yajirusi_W_50.png")
        imgW_2=tk.PhotoImage(file="yajirusi_W_60.png")
        num=0
        num2=0
        yuka=0
        tag_label=0
        if stage_lve!=10:
            buttonRe=tk.Button(root,text="やり直す",font=('Mongolian Baiti',20),command=restart)
            button1=tk.Button(root,text="タイトルに戻る",font=('Microsoft New Tai Lue',20),command=loop0)
        
    def key_down(e):
        global key
        key=e.keysym
        
    def key_up(e):
        global key
        key=""
    
    def restart():
        global restart_count,num,yuka,num2
        canvas_lve.place_forget()
        buttonRe.place_forget()
        button1.place_forget()
        label1.place_forget()
        num=0
        num2=0
        yuka=0
        restart_count=1
        if stage_lve==1:
            lve1()
        elif stage_lve==2:
            lve2()
        elif stage_lve==3:
            lve3()
        elif stage_lve==4:
            lve4()
        elif stage_lve==5:
            lve5()
        elif stage_lve==6:
            lve6()
        elif stage_lve==7:
            lve7()
        elif stage_lve==8:
            lve8()
        elif stage_lve==9:
            lve9()
        else:
            lve10()
        
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    
    def main_proc():
        global atlas_x,atlas_y,num,yuka,num2,tag_label,idou,after_id
        if key=="Up" or key=="w":
            if atlas[atlas_y-1][atlas_x]==8 and num==4:
                atlas_y=atlas_y-1
                num=5
            elif atlas[atlas_y-1][atlas_x]==7 and num==3:
                atlas_y=atlas_y-1
                num=4
            elif atlas[atlas_y-1][atlas_x]==6 and num==2:
                atlas_y=atlas_y-1
                num=3
            elif atlas[atlas_y-1][atlas_x]==5 and num==1:
                atlas_y=atlas_y-1
                num=2
            elif atlas[atlas_y-1][atlas_x]==18 and num==5:
                atlas_y=atlas_y-1
                num=6
            elif atlas[atlas_y-1][atlas_x]==19 and num==6:
                atlas_y=atlas_y-1
                num=7
            elif atlas[atlas_y-1][atlas_x]==20 and num==7:
                atlas_y=atlas_y-1
                num=8
            elif atlas[atlas_y-1][atlas_x]==21 and num==8:
                atlas_y=atlas_y-1
                num=9
            elif atlas[atlas_y-1][atlas_x]==4:
                atlas_y=atlas_y-1
                num=1
            elif atlas[atlas_y-1][atlas_x]==9:
                atlas_y=atlas_y-1
                num2=1
            elif atlas[atlas_y-1][atlas_x]==10 and num2==1:
                atlas_y=atlas_y-1
                num2=2
            elif atlas[atlas_y-1][atlas_x]==11 and num2==2:
                atlas_y=atlas_y-1
                num2=3
            elif atlas[atlas_y-1][atlas_x]==3: #ゴールの時に実行
                if stage_lve==1 and yuka==19:
                    atlas_y=atlas_y-1
                elif stage_lve!=1 and num==5 and yuka==yuka_clear-1:
                    atlas_y=atlas_y-1
            elif atlas[atlas_y-1][atlas_x]==1 or atlas[atlas_y-1][atlas_x]==12 or atlas[atlas_y-1][atlas_x]==13 or atlas[atlas_y-1][atlas_x]==15:
                atlas_y=atlas_y-1
        if key=="Down" or key=="s":
            if atlas[atlas_y+1][atlas_x]==8 and num==4:
                atlas_y=atlas_y+1
                num=5
            elif atlas[atlas_y+1][atlas_x]==7 and num==3:
                atlas_y=atlas_y+1
                num=4
            elif atlas[atlas_y+1][atlas_x]==6 and num==2:
                atlas_y=atlas_y+1
                num=3
            elif atlas[atlas_y+1][atlas_x]==5 and num==1:
                atlas_y=atlas_y+1
                num=2
            elif atlas[atlas_y+1][atlas_x]==18 and num==5:
                atlas_y=atlas_y+1
                num=6
            elif atlas[atlas_y+1][atlas_x]==19 and num==6:
                atlas_y=atlas_y+1
                num=7
            elif atlas[atlas_y+1][atlas_x]==20 and num==7:
                atlas_y=atlas_y+1
                num=8
            elif atlas[atlas_y+1][atlas_x]==21 and num==8:
                atlas_y=atlas_y+1
                num=9
            elif atlas[atlas_y+1][atlas_x]==4:
                atlas_y=atlas_y+1
                num=1
            elif atlas[atlas_y+1][atlas_x]==9:
                atlas_y=atlas_y+1
                num2=1
            elif atlas[atlas_y+1][atlas_x]==10 and num2==1:
                atlas_y=atlas_y+1
                num2=2
            elif atlas[atlas_y+1][atlas_x]==11 and num2==2:
                atlas_y=atlas_y+1
                num2=3
            elif atlas[atlas_y+1][atlas_x]==3: #ゴールの時に実行
                if stage_lve==1 and yuka==19:
                    atlas_y=atlas_y+1
                elif stage_lve!=1 and num>4 and yuka==yuka_clear-1:
                    atlas_y=atlas_y+1
            elif atlas[atlas_y+1][atlas_x]==1 or atlas[atlas_y+1][atlas_x]==13 or atlas[atlas_y+1][atlas_x]==14 or atlas[atlas_y+1][atlas_x]==15:
                atlas_y=atlas_y+1
        if key=="Left" or key=="a":
            if atlas[atlas_y][atlas_x-1]==8 and num==4:
                atlas_x=atlas_x-1
                num=5
            elif atlas[atlas_y][atlas_x-1]==7 and num==3:
                atlas_x=atlas_x-1
                num=4
            elif atlas[atlas_y][atlas_x-1]==6 and num==2:
                atlas_x=atlas_x-1
                num=3
            elif atlas[atlas_y][atlas_x-1]==5 and num==1:
                atlas_x=atlas_x-1
                num=2
            elif atlas[atlas_y][atlas_x-1]==18 and num==5:
                atlas_x=atlas_x-1
                num=6
            elif atlas[atlas_y][atlas_x-1]==19 and num==6:
                atlas_x=atlas_x-1
                num=7
            elif atlas[atlas_y][atlas_x-1]==20 and num==7:
                atlas_x=atlas_x-1
                num=8
            elif atlas[atlas_y][atlas_x-1]==21 and num==8:
                atlas_x=atlas_x-1
                num=9
            elif atlas[atlas_y][atlas_x-1]==4:
                atlas_x=atlas_x-1
                num=1
            elif atlas[atlas_y][atlas_x-1]==9:
                atlas_x=atlas_x-1
                num2=1
            elif atlas[atlas_y][atlas_x-1]==10 and num2==1:
                atlas_x=atlas_x-1
                num2=2
            elif atlas[atlas_y][atlas_x-1]==11 and num2==2:
                atlas_x=atlas_x-1
                num2=3
            elif atlas[atlas_y][atlas_x-1]==16 and num2==3:
                atlas_x=atlas_x-1
            elif  atlas[atlas_y][atlas_x-1]==11 and num2==3:
                atlas_x=atlas_x-1
            elif atlas[atlas_y][atlas_x-1]==3: #ゴールの時に実行
                if stage_lve==1 and yuka==19:
                    atlas_x=atlas_x-1
                elif stage_lve!=1 and num==5 and yuka==yuka_clear-1:
                    atlas_x=atlas_x-1
            elif atlas[atlas_y][atlas_x-1]==1 or atlas[atlas_y][atlas_x-1]==12 or atlas[atlas_y][atlas_x-1]==14 or atlas[atlas_y][atlas_x-1]==15:
                atlas_x=atlas_x-1
        if key=="Right" or key=="d":
            if atlas[atlas_y][atlas_x+1]==8 and num==4:
                atlas_x=atlas_x+1
                num=5
            elif atlas[atlas_y][atlas_x+1]==7 and num==3:
                atlas_x=atlas_x+1
                num=4
            elif atlas[atlas_y][atlas_x+1]==6 and num==2:
                atlas_x=atlas_x+1
                num=3
            elif atlas[atlas_y][atlas_x+1]==5 and num==1:
                atlas_x=atlas_x+1
                num=2
            elif atlas[atlas_y][atlas_x+1]==18 and num==5:
                atlas_x=atlas_x+1
                num=6
            elif atlas[atlas_y][atlas_x+1]==19 and num==6:
                atlas_x=atlas_x+1
                num=7
            elif atlas[atlas_y][atlas_x+1]==20 and num==7:
                atlas_x=atlas_x+1
                num=8
            elif atlas[atlas_y][atlas_x+1]==21 and num==8:
                atlas_x=atlas_x+1
                num=9
            elif atlas[atlas_y][atlas_x+1]==4:
                atlas_x=atlas_x+1
                num=1
            elif atlas[atlas_y][atlas_x+1]==9:
                atlas_x=atlas_x+1
                num2=1
            elif atlas[atlas_y][atlas_x+1]==10 and num2==1:
                atlas_x=atlas_x+1
                num2=2
            elif atlas[atlas_y][atlas_x+1]==11 and num2==2:
                atlas_x=atlas_x+1
                num2=3
            elif atlas[atlas_y][atlas_x+1]==3: #ゴールの時に実行
                if stage_lve==1 and yuka==19:
                    atlas_x=atlas_x+1
                elif stage_lve!=1 and num==5 and yuka==yuka_clear-1:
                    atlas_x=atlas_x+1
            elif atlas[atlas_y][atlas_x+1]==1 or atlas[atlas_y][atlas_x+1]==12 or atlas[atlas_y][atlas_x+1]==13 or atlas[atlas_y][atlas_x+1]==14:
                atlas_x=atlas_x+1
        if key=="Shift_L" or key=="Shift_R":
            restart()
        if tag_label==12:
            atlas_y=atlas_y-1
            tag_label=0
            if atlas[atlas_y][atlas_x]==2:
                restart()
        elif tag_label==13:
            atlas_x=atlas_x+1
            tag_label=0
            if atlas[atlas_y][atlas_x]==2:
                restart()
        elif tag_label==14:
            atlas_y=atlas_y+1
            tag_label=0
            if atlas[atlas_y][atlas_x]==2:
                restart()
        elif tag_label==15:
            atlas_x=atlas_x-1
            tag_label=0
            if atlas[atlas_y][atlas_x]==2:
                restart()
        if atlas[atlas_y][atlas_x]!=0 and atlas[atlas_y][atlas_x]!=2:
            if atlas[atlas_y][atlas_x]==9:
                atlas[atlas_y][atlas_x]=2
                yuka=yuka+1
                canvas_lve.create_rectangle(atlas_x*a,atlas_y*a,atlas_x*a+a-1,atlas_y*a+a-1,fill="pink",width=0)
                for y in range(c):
                    for x in range(b):
                        if atlas[y][x]==9 and atlas_x!=x and  atlas_y!=y:
                            atlas_x=x
                            atlas_y=y
                atlas[atlas_y][atlas_x]=2
                yuka=yuka+1
                canvas_lve.create_rectangle(atlas_x*a,atlas_y*a,atlas_x*a+a-1,atlas_y*a+a-1,fill="pink",width=0)
            elif atlas[atlas_y][atlas_x]==10:
                atlas[atlas_y][atlas_x]=2
                yuka=yuka+1
                canvas_lve.create_rectangle(atlas_x*a,atlas_y*a,atlas_x*a+a-1,atlas_y*a+a-1,fill="pink",width=0)
                for y in range(c):
                    for x in range(b):
                        if atlas[y][x]==10 and atlas_x!=x and  atlas_y!=y:
                            atlas_x=x
                            atlas_y=y
                atlas[atlas_y][atlas_x]=2
                yuka=yuka+1
                canvas_lve.create_rectangle(atlas_x*a,atlas_y*a,atlas_x*a+a-1,atlas_y*a+a-1,fill="pink",width=0)
            elif atlas[atlas_y][atlas_x]==11:
                atlas[atlas_y][atlas_x]=2
                yuka=yuka+1
                canvas_lve.create_rectangle(atlas_x*a,atlas_y*a,atlas_x*a+a-1,atlas_y*a+a-1,fill="pink",width=0)
                for y in range(c):
                    for x in range(b):
                        if atlas[y][x]==11 and atlas_x!=x and  atlas_y!=y:
                            atlas_x=x
                            atlas_y=y
                atlas[atlas_y][atlas_x]=2
                yuka=yuka+1
                canvas_lve.create_rectangle(atlas_x*a,atlas_y*a,atlas_x*a+a-1,atlas_y*a+a-1,fill="pink",width=0)
            elif atlas[atlas_y][atlas_x]==12:
                atlas[atlas_y][atlas_x]=2
                yuka=yuka+1
                canvas_lve.create_rectangle(atlas_x*a,atlas_y*a,atlas_x*a+a-1,atlas_y*a+a-1,fill="pink",width=0)
                tag_label=12
            elif atlas[atlas_y][atlas_x]==13:
                atlas[atlas_y][atlas_x]=2
                yuka=yuka+1
                canvas_lve.create_rectangle(atlas_x*a,atlas_y*a,atlas_x*a+a-1,atlas_y*a+a-1,fill="pink",width=0)
                tag_label=13
            elif atlas[atlas_y][atlas_x]==14:
                atlas[atlas_y][atlas_x]=2
                yuka=yuka+1
                canvas_lve.create_rectangle(atlas_x*a,atlas_y*a,atlas_x*a+a-1,atlas_y*a+a-1,fill="pink",width=0)
                tag_label=14
            elif atlas[atlas_y][atlas_x]==15:
                atlas[atlas_y][atlas_x]=2
                yuka=yuka+1
                canvas_lve.create_rectangle(atlas_x*a,atlas_y*a,atlas_x*a+a-1,atlas_y*a+a-1,fill="pink",width=0)
                tag_label=15
            elif atlas[atlas_y][atlas_x]==16:
                atlas[atlas_y][atlas_x]=2
                yuka=yuka+1
                canvas_lve.create_rectangle(atlas_x*a,atlas_y*a,atlas_x*a+a-1,atlas_y*a+a-1,fill="pink",width=0)
                for y in range(c):
                    for x in range(b):
                        if atlas[y][x]==17:
                            atlas_y=y
                            atlas_x=x
                atlas[atlas_y][atlas_x]=2
                yuka=yuka+1
                canvas_lve.create_rectangle(atlas_x*a,atlas_y*a,atlas_x*a+a-1,atlas_y*a+a-1,fill="pink",width=0)
                canvas_lve.delete("MYCHAR")
                canvas_lve.create_image(atlas_x*a+a/2,atlas_y*a+a/2,image=img_s2,tag="MYCHAR")
                atlas_y=atlas_y-1
                atlas[atlas_y][atlas_x]=2
                yuka=yuka+1
                canvas_lve.create_rectangle(atlas_x*a,atlas_y*a,atlas_x*a+a-1,atlas_y*a+a-1,fill="pink",width=0)
                canvas_lve.delete("MYCHAR")
                canvas_lve.create_image(atlas_x*a+a/2,atlas_y*a+a/2,image=img_s2,tag="MYCHAR")
            else:
                atlas[atlas_y][atlas_x]=2
                yuka=yuka+1
                canvas_lve.create_rectangle(atlas_x*a,atlas_y*a,atlas_x*a+a-1,atlas_y*a+a-1,fill="pink",width=0)
        canvas_lve.delete("MYCHAR")
        if stage_lve!=9 and stage_lve!=10:
            canvas_lve.create_image(atlas_x*a+a/2,atlas_y*a+a/2,image=img_s1,tag="MYCHAR")
        elif stage_lve==9:
            canvas_lve.create_image(atlas_x*a+a/2,atlas_y*a+a/2,image=img_s3,tag="MYCHAR")
        else:
            canvas_lve.create_image(atlas_x*a+a/2,atlas_y*a+a/2,image=img_s2,tag="MYCHAR")
        if yuka==yuka_clear:
            root.after(500,clear)
        elif loop0_count!=1:
            after_id=root.after(200, main_proc)
            
    def loop0():
        global restart_count,loop0_count
        canvas_lve.place_forget()
        buttonRe.place_forget()
        button1.place_forget()
        label1.place_forget()
        restart_count=1
        loop0_count=1
        start()
        
    def lve1():
        global canvas_lve,stage_lve,atlas,atlas_x,atlas_y,a,yuka_clear,b,c,label1
        stage_lve=1
        if restart_count==0 and reset_count==0:
            preprocessor()
        a=80
        b=7
        c=6
        yuka_clear=20
        atlas_x=1 #スタートの位置
        atlas_y=1 #スタートの位置
        label1=tk.Label(root,text="レベル"+str(stage_lve),font=('Mongolian Baiti',20))
        canvas_lve=tk.Canvas(root,width=a*b-b,height=a*c-c,bg="white")
        #壁=0,空白=1,通り道=2,ゴール=3に設定
        atlas=[
                [0,0,0,0,0,0,0],
                [0,1,1,1,1,1,0],
                [0,1,1,3,1,1,0],
                [0,1,1,1,1,1,0],
                [0,1,1,1,1,1,0],
                [0,0,0,0,0,0,0]
              ]
        canvas_lve.create_image(atlas_x*a+a/2,atlas_y*a+a/2,image=img_s1,tag="MYCHAR")
        for y in range(c):
            for x in range(b):
                if atlas[y][x]==0:
                    canvas_lve.create_rectangle(x*a,y*a,x*a+a-1,y*a+a-1,fill="skyblue",width=0)
                elif atlas[y][x]==3:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img_g)
        if restart_count==0:
            main_proc()
        canvas_lve.place(x=0,y=0)
        buttonRe.place(x=1000,y=750)
        button1.place(x=1000,y=800)
        label1.place(x=1000,y=700)
    
    def lve2():
        global canvas_lve,stage_lve,atlas,atlas_x,atlas_y,a,yuka_clear,b,c,label1
        stage_lve=2
        if restart_count==0 and reset_count==0:
            preprocessor()
        a=80
        b=7
        c=6
        yuka_clear=20
        atlas_x=1
        atlas_y=1
        label1=tk.Label(root,text="レベル"+str(stage_lve),font=('Mongolian Baiti',20))
        canvas_lve=tk.Canvas(root,width=a*b-b,height=a*c-c,bg="white")
        #壁=0,空白=1,通り道=2,ゴール=3,1=4,2=5,3=6,4=7,5=8
        atlas=[
                [0,0,0,0,0,0,0],
                [0,1,1,5,3,8,0],
                [0,4,1,1,1,1,0],
                [0,1,1,1,1,1,0],
                [0,6,1,1,1,7,0],
                [0,0,0,0,0,0,0]
              ]
        canvas_lve.create_image(atlas_x*a+a/2,atlas_y*a+a/2,image=img_s1,tag="MYCHAR")
        for y in range(c):
            for x in range(b):
                if atlas[y][x]==0:
                    canvas_lve.create_rectangle(x*a,y*a, x*a+a-1,y*a+a-1,fill="skyblue",width=0)
                elif atlas[y][x]==3:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img_g)
                elif atlas[y][x]==4:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img1)
                elif atlas[y][x]==5:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img2)
                elif atlas[y][x]==6:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img3)
                elif atlas[y][x]==7:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img4)
                elif atlas[y][x]==8:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img5)
        if restart_count==0:
            main_proc()
        canvas_lve.place(x=0,y=0)
        buttonRe.place(x=1000,y=750)
        button1.place(x=1000,y=800)
        label1.place(x=1000,y=700)
    
    def lve3():
        global canvas_lve,stage_lve,atlas,atlas_x,atlas_y,a,yuka_clear,b,c,label1
        stage_lve=3
        if restart_count==0 and reset_count==0:
            preprocessor()
        a=80
        b=9
        c=7
        yuka_clear=35
        atlas_x=1
        atlas_y=1
        label1=tk.Label(root,text="レベル"+str(stage_lve),font=('Mongolian Baiti',20))
        canvas_lve=tk.Canvas(root,width=a*b-b,height=a*c-c,bg="white")
        atlas=[
                [0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,8,0],
                [0,4,1,1,1,7,1,1,0],
                [0,1,5,1,1,1,1,1,0],
                [0,1,1,1,1,6,1,1,0],
                [0,1,1,1,1,1,1,3,0],
                [0,0,0,0,0,0,0,0,0]
              ]
        canvas_lve.create_image(atlas_x*a+a/2,atlas_y*a+a/2,image=img_s1,tag="MYCHAR")
        for y in range(c):
            for x in range(b):
                if atlas[y][x]==0:
                    canvas_lve.create_rectangle(x*a,y*a, x*a+a-1,y*a+a-1,fill="skyblue",width=0)
                elif atlas[y][x]==3:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img_g)
                elif atlas[y][x]==4:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img1)
                elif atlas[y][x]==5:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img2)
                elif atlas[y][x]==6:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img3)
                elif atlas[y][x]==7:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img4)
                elif atlas[y][x]==8:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img5)
        if restart_count==0:
            main_proc()
        canvas_lve.place(x=0,y=0)
        buttonRe.place(x=1000,y=750)
        button1.place(x=1000,y=800)
        label1.place(x=1000,y=700)
    
    def lve4():
        global canvas_lve,stage_lve,atlas,atlas_x,atlas_y,a,yuka_clear,b,c,label1
        stage_lve=4
        if restart_count==0 and reset_count==0:
            preprocessor()
        a=80
        b=9
        c=7
        yuka_clear=33
        atlas_x=4
        atlas_y=5
        label1=tk.Label(root,text="レベル"+str(stage_lve),font=('Mongolian Baiti',20))
        canvas_lve=tk.Canvas(root,width=a*b-b, height=a*c-c,bg="white")
        atlas=[
                [0,0,0,0,0,0,0,0,0],
                [0,1,1,1,6,1,1,1,0],
                [0,1,1,1,8,1,0,1,0],
                [0,1,7,1,3,1,5,1,0],
                [0,1,0,1,4,1,1,1,0],
                [0,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0]
              ]
        canvas_lve.create_image(atlas_x*a+a/2,atlas_y*a+a/2,image=img_s1,tag="MYCHAR")
        for y in range(c):
            for x in range(b):
                if atlas[y][x]==0:
                    canvas_lve.create_rectangle(x*a,y*a,x*a+a-1,y*a+a-1,fill="skyblue",width=0)
                elif atlas[y][x]==3:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img_g)
                elif atlas[y][x]==4:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img1)
                elif atlas[y][x]==5:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img2)
                elif atlas[y][x]==6:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img3)
                elif atlas[y][x]==7:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img4)
                elif atlas[y][x]==8:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img5)
        if restart_count==0:
            main_proc()
        canvas_lve.place(x=0,y=0)
        buttonRe.place(x=1000,y=750)
        button1.place(x=1000,y=800)
        label1.place(x=1000,y=700)
    
    def lve5():
        global canvas_lve,stage_lve,atlas,atlas_x,atlas_y,a,yuka_clear,b,c,label1
        stage_lve=5
        if restart_count==0 and reset_count==0:
            preprocessor()
        a=80
        b=11
        c=8
        yuka_clear=0
        atlas_x=1
        atlas_y=1
        label1=tk.Label(root,text="レベル"+str(stage_lve),font=('Mongolian Baiti',20))
        canvas_lve=tk.Canvas(root,width=a*b-b, height=a*c-c,bg="white")
        atlas=[
                [0,0,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,7,1,0],
                [0,1,1,1,1,4,1,1,1,1,0],
                [0,1,1,1,5,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,3,1,1,1,8,1,0],
                [0,1,1,1,1,1,6,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0]
              ]
        canvas_lve.create_image(atlas_x*a+a/2,atlas_y*a+a/2,image=img_s1,tag="MYCHAR")
        for y in range(c):
            for x in range(b):
                if atlas[y][x]!=0:
                    yuka_clear=yuka_clear+1
                if atlas[y][x]==0:
                    canvas_lve.create_rectangle(x*a,y*a,x*a+a-1,y*a+a-1,fill="skyblue",width=0)
                elif atlas[y][x]==3:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img_g)
                elif atlas[y][x]==4:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img1)
                elif atlas[y][x]==5:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img2)
                elif atlas[y][x]==6:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img3)
                elif atlas[y][x]==7:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img4)
                elif atlas[y][x]==8:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img5)
        if restart_count==0:
            main_proc()
        canvas_lve.place(x=0,y=0)
        buttonRe.place(x=1000,y=750)
        button1.place(x=1000,y=800)
        label1.place(x=1000,y=700)
        
    def lve6():
        global canvas_lve,stage_lve,atlas,atlas_x,atlas_y,a,yuka_clear,b,c,label1
        stage_lve=6
        if restart_count==0 and reset_count==0:
            preprocessor()
        a=80
        b=11
        c=8
        yuka_clear=0
        atlas_x=1
        atlas_y=1
        label1=tk.Label(root,text="レベル"+str(stage_lve),font=('Mongolian Baiti',20))
        canvas_lve=tk.Canvas(root,width=a*b-b, height=a*c-c,bg="white")
        atlas=[
                [0,0,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,7,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,8,1,1,1,1,0],
                [0,1,1,5,1,1,1,1,1,1,0],
                [0,1,3,1,1,1,1,1,1,1,0],
                [0,4,1,1,1,1,1,1,1,6,0],
                [0,0,0,0,0,0,0,0,0,0,0]
              ]
        canvas_lve.create_image(atlas_x*a+a/2,atlas_y*a+a/2,image=img_s1,tag="MYCHAR")
        for y in range(c):
            for x in range(b):
                if atlas[y][x]!=0:
                    yuka_clear=yuka_clear+1
                if atlas[y][x]==0:
                    canvas_lve.create_rectangle(x*a,y*a,x*a+a-1,y*a+a-1,fill="skyblue",width=0)
                elif atlas[y][x]==3:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img_g)
                elif atlas[y][x]==4:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img1)
                elif atlas[y][x]==5:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img2)
                elif atlas[y][x]==6:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img3)
                elif atlas[y][x]==7:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img4)
                elif atlas[y][x]==8:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img5)
        if restart_count==0:
            main_proc()
        canvas_lve.place(x=0,y=0)
        buttonRe.place(x=1000,y=750)
        button1.place(x=1000,y=800)
        label1.place(x=1000,y=700)
        
    def lve7():
        global canvas_lve,stage_lve,atlas,atlas_x,atlas_y,a,yuka_clear,b,c,label1
        stage_lve=7
        if restart_count==0 and reset_count==0:
            preprocessor()
        a=80
        b=12
        c=8
        yuka_clear=0
        atlas_x=1
        atlas_y=1
        label1=tk.Label(root,text="レベル"+str(stage_lve),font=('Mongolian Baiti',20))
        canvas_lve=tk.Canvas(root,width=a*b-b,height=a*c-c,bg="white")
        atlas=[
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,4,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,6,1,1,0],
                [0,5,1,1,1,1,1,1,1,1,1,0],
                [0,9,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,9,3,1,0],
                [0,1,1,1,1,1,1,7,1,1,8,0],
                [0,0,0,0,0,0,0,0,0,0,0,0]
              ]
        canvas_lve.create_image(atlas_x*a+a/2,atlas_y*a+a/2,image=img_s1,tag="MYCHAR")
        for y in range(c):
            for x in range(b):
                if atlas[y][x]!=0:
                    yuka_clear=yuka_clear+1
                if atlas[y][x]==0:
                    canvas_lve.create_rectangle(x*a,y*a,x*a+a-1,y*a+a-1,fill="skyblue",width=0)
                elif atlas[y][x]==3:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img_g)
                elif atlas[y][x]==4:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img1)
                elif atlas[y][x]==5:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img2)
                elif atlas[y][x]==6:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img3)
                elif atlas[y][x]==7:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img4)
                elif atlas[y][x]==8:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img5)
                elif atlas[y][x]==9:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=imgW)
        if restart_count==0:
            main_proc()
        canvas_lve.place(x=0,y=0)
        buttonRe.place(x=1000,y=750)
        button1.place(x=1000,y=800)
        label1.place(x=1000,y=700)
        
    def lve8():
        global canvas_lve,stage_lve,atlas,atlas_x,atlas_y,a,yuka_clear,b,c,label1
        stage_lve=8
        if restart_count==0 and reset_count==0:
            preprocessor()
        a=80
        b=12
        c=8
        yuka_clear=0
        atlas_x=5
        atlas_y=3
        label1=tk.Label(root,text="レベル"+str(stage_lve),font=('Mongolian Baiti',20))
        canvas_lve=tk.Canvas(root,width=a*b-b, height=a*c-c,bg="white")
        atlas=[
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,3,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,4,1,1,6,1,1,1,1,0],
                [0,8,1,1,1,1,1,1,1,1,9,0],
                [0,1,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,5,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,9,7,0],
                [0,0,0,0,0,0,0,0,0,0,0,0]
              ]
        canvas_lve.create_image(atlas_x*a+a/2,atlas_y*a+a/2,image=img_s1,tag="MYCHAR")
        for y in range(c):
            for x in range(b):
                if atlas[y][x]!=0:
                    yuka_clear=yuka_clear+1
                if atlas[y][x]==0:
                    canvas_lve.create_rectangle(x*a,y*a,x*a+a-1,y*a+a-1,fill="skyblue",width=0)
                elif atlas[y][x]==3:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img_g)
                elif atlas[y][x]==4:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img1)
                elif atlas[y][x]==5:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img2)
                elif atlas[y][x]==6:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img3)
                elif atlas[y][x]==7:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img4)
                elif atlas[y][x]==8:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img5)
                elif atlas[y][x]==9:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=imgW)
        if restart_count==0:
            main_proc()
        canvas_lve.place(x=0,y=0)
        buttonRe.place(x=1000,y=750)
        button1.place(x=1000,y=800)
        label1.place(x=1000,y=700)
        
    def lve9():
        global canvas_lve,stage_lve,atlas,atlas_x,atlas_y,a,yuka_clear,b,c,label1
        stage_lve=9
        if restart_count==0 and reset_count==0:
            preprocessor()
        a=60
        b=15
        c=11
        yuka_clear=0
        atlas_x=1
        atlas_y=1
        label1=tk.Label(root,text="レベル"+str(stage_lve),font=('Mongolian Baiti',20))
        canvas_lve=tk.Canvas(root,width=a*b-2, height=a*c-2,bg="white")
        atlas=[
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,4,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,6,1,1,1,1,9,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,1,7,1,1,1,0],
                [0,1,1,1,1,5,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,10,1,1,15,1,11,3,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,1,13,11,1,1,0],
                [0,1,1,1,1,1,9,8,1,1,1,1,1,10,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
              ]
        
        canvas_lve.create_image(atlas_x*a+a/2,atlas_y*a+a/2,image=img_s3,tag="MYCHAR")
        for y in range(c):
            for x in range(b):
                if atlas[y][x]!=0:
                    yuka_clear=yuka_clear+1
                if atlas[y][x]==0:
                    canvas_lve.create_rectangle(x*a,y*a,x*a+a-1,y*a+a-1,fill="skyblue",width=0)
                elif atlas[y][x]==3:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img_g3)
                elif atlas[y][x]==4:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img1_2)
                elif atlas[y][x]==5:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img2_2)
                elif atlas[y][x]==6:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img3_2)
                elif atlas[y][x]==7:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img4_2)
                elif atlas[y][x]==8:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img5_2)
                elif atlas[y][x]==9:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=imgW3)
                elif atlas[y][x]==10:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=imgWS)
                elif atlas[y][x]==11:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=imgWC)
                elif atlas[y][x]==12:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=imgN2)
                elif atlas[y][x]==13:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=imgE2)
                elif atlas[y][x]==14:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=imgS2)
                elif atlas[y][x]==15:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=imgW_2)
                
                
        if restart_count==0:
            main_proc()
        canvas_lve.place(x=0,y=0)
        buttonRe.place(x=1000,y=750)
        button1.place(x=1000,y=800)
        label1.place(x=1000,y=700)
        
    def lve10():
        global canvas_lve,stage_lve,atlas,atlas_x,atlas_y,a,yuka_clear,b,c,label1,label2,label3,buttonRe,button1
        stage_lve=10
        if restart_count==0 and reset_count==0:
            preprocessor()
        a=50
        b=24
        c=18
        yuka_clear=0
        atlas_x=1
        atlas_y=1
        canvas_lve=tk.Canvas(root,width=a*b-2, height=a*c-2,bg="white")
        atlas=[
                [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1,14, 1, 1, 1, 1, 1, 9,13,13,13,13,10, 0],
                [ 0, 1,15, 1, 1, 5, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 7, 1, 1, 1, 1, 1, 1, 0],
                [ 0, 1, 1,12, 1, 1, 1, 1,15, 1, 1, 1,12, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [ 0,11, 1, 1, 1, 1, 1, 1, 1, 1, 1,12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1,15,10, 1,12, 8, 0],
                [16,15, 1, 1,13, 1, 1, 1, 1, 1, 1, 6, 1, 1,12, 0,13, 1, 1, 1,18, 1, 1, 0],
                [ 0, 1, 1, 1, 1, 1, 1,14, 1,15, 1, 1,14, 1, 1, 1, 1,15, 0, 1, 1,20, 1, 0],
                [ 0, 1, 1, 1, 1,14, 1, 1, 1, 1, 1, 1, 1,13, 1, 1, 1, 1,14, 1,15, 1, 1, 0],
                [ 0, 1, 1, 1,14, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,15, 1, 1, 1, 1, 0],
                [ 0, 1, 1, 1,11, 1, 1, 1,21, 1,13, 1, 1, 1,13, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [ 0,13, 1, 1,15, 1, 1, 1, 1,14, 1, 1, 1, 1,14, 1, 1, 1, 1,13, 1, 1, 1, 0],
                [ 0,13, 1, 1, 1, 1,12, 1, 1, 1, 1, 1, 1, 1, 1,13, 9, 1, 1, 1, 1,15, 1, 0],
                [ 0, 1, 1, 1, 1, 1, 1,15,12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,19, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [ 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [ 2,14, 2, 2, 2, 2, 2, 2,17, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 1, 2],
                [ 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
              ]
        
        canvas_lve.create_image(atlas_x*a+a/2,atlas_y*a+a/2,image=img_s2,tag="MYCHAR")
        label1=tk.Label(root,text="レベル"+str(stage_lve),font=('Mongolian Baiti',17),bg="white")
        label2=tk.Label(canvas_lve,text="矢印の方向に強制移動",font=('Bodoni MT Poster Compressed',20),bg="white")
        label3=tk.Label(canvas_lve,text="同じ色の所にワープ",font=('Franklin Gothic Medium Cond',20),bg="white")
        buttonRe=tk.Button(root,text="やり直す",font=('Mongolian Baiti',17),bg="royalblue",command=restart)
        button1=tk.Button(root,text="タイトルに戻る",font=('Microsoft New Tai Lue',17),bg="orange",command=loop0)
        for y in range(c):
            for x in range(b):
                if atlas[y][x]!=0 and atlas[y][x]!=2:
                    yuka_clear=yuka_clear+1
                if atlas[y][x]==0:
                    canvas_lve.create_rectangle(x*a,y*a,x*a+a-1,y*a+a-1,fill="skyblue",width=0)
                elif atlas[y][x]==3:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img_g3)
                elif atlas[y][x]==4:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img1_3)
                elif atlas[y][x]==5:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img2_3)
                elif atlas[y][x]==6:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img3_3)
                elif atlas[y][x]==7:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img4_3)
                elif atlas[y][x]==8:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img5_3)
                elif atlas[y][x]==9:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=imgW2)
                elif atlas[y][x]==10:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=imgWS2)
                elif atlas[y][x]==11:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=imgWC2)
                elif atlas[y][x]==12:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=imgN)
                elif atlas[y][x]==13:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=imgE)
                elif atlas[y][x]==14:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=imgS)
                elif atlas[y][x]==15:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=imgW_1)
                elif atlas[y][x]==16:
                    canvas_lve.create_rectangle(x*a,y*a,x*a+a-1,y*a+a-1,fill="skyblue",width=0)
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=imgWB)
                elif atlas[y][x]==17:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=imgW2)
                elif atlas[y][x]==18:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img6)
                elif atlas[y][x]==19:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img7)
                elif atlas[y][x]==20:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img8)
                elif atlas[y][x]==21:
                    canvas_lve.create_image(x*a+a/2,y*a+a/2,image=img9)
                
        if restart_count==0:
            main_proc()
        canvas_lve.place(x=0,y=0)
        label2.place(x=100,y=800,width=300,height=50)
        label3.place(x=450,y=800,width=248,height=50)
        label1.place(x=752,y=800,width=98,height=50)
        buttonRe.place(x=850,y=800,width=100,height=50)
        button1.place(x=950,y=800,width=150,height=50)
        
    def lveR():
        lve_list=[1,2,3,4,5,6,7,8,9,10]
        r=random.choice(lve_list)
        if r==stage_lve:
            lveR()
        if r==1:
            lve1()
        elif r==2:
            lve2()
        elif r==3:
            lve3()
        elif r==4:
            lve4()
        elif r==5:
            lve5()
        elif r==6:
            lve6()
        elif r==7:
            lve7()
        elif r==8:
            lve8()
        elif r==9:
            lve9()
        else:
            lve10()
    
    def clear():
        global button4,button2,button3,frame2,restart_count,num,yuka
        root.after_cancel(after_id)
        buttonRe.place_forget()
        button1.place_forget()
        label1.place_forget()
        canvas_lve.place_forget()
        frame1["bg"]="violet"
        label2["text"]="ありがとう！"
        label3["text"]="たすかったよ！"
        frame1.pack(side=tk.TOP,expand=True,anchor=tk.CENTER)
        frame2=tk.Frame(root,width=700,height=300,bg='orange')
        frame2.pack(side=tk.TOP,expand=True,anchor=tk.N)
        label2.grid(row=0,column=1)
        label3.grid(row=1,column=1)
        canvas1.grid(row=0,column=0,rowspan=2)
        button4=tk.Button(frame2,text="タイトルに戻る",font=('Microsoft New Tai Lue',20),width=18,command=loop)
        button2=tk.Button(frame2,text="次のレベルへ!",font=('Microsoft New Tai Lue',20),width=18,command=next_stage)
        button3=tk.Button(frame2,text="ランダムなレベルへ!",font=('Microsoft New Tai Lue',20),width=18,command=random_stage)
        button4.grid(row=0,column=0)
        button2.grid(row=0,column=1,padx=20)
        button3.grid(row=0,column=2)
        restart_count=0
        num=0
        yuka=0
        if stage_lve==10:
            button2["state"]="disable"
        
    def reset():
        global reset_count,buttonRe,button1
        canvas1.grid_forget()
        label2.grid_forget()
        label3.grid_forget()
        frame1.pack_forget()
        button4.grid_forget()
        button2.grid_forget()
        button3.grid_forget()
        frame2.pack_forget()
        button0.place_forget()
        reset_count=1
        buttonRe=tk.Button(root,text="やり直す",font=('Mongolian Baiti',20),command=restart)
        button1=tk.Button(root,text="タイトルに戻る",font=('Microsoft New Tai Lue',20),command=loop0)
        
    def loop():
        reset()
        start()
    
    def next_stage():
        reset()
        if stage_lve==1:
            lve2()
        elif stage_lve==2:
            lve3()
        elif stage_lve==3:
            lve4()
        elif stage_lve==4:
            lve5()
        elif stage_lve==5:
            lve6()
        elif stage_lve==6:
            lve7()
        elif stage_lve==7:
            lve8()
        elif stage_lve==8:
            lve9()
        elif stage_lve==9:
            lve10()        
        
    def random_stage():
        reset()
        lveR()
    
    start()
    root.mainloop()

def omikuji():
    global root
    root.destroy()
    def click_btn():
        label["text"]=random.choice(["大吉", "中吉", "小吉"," 吉 ", " 凶 ","大凶","福吉"])
        label.update()
    
    def cli():
        root.destroy()
        main_game()
    
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
    button2=tk.Button(root,text="メインに戻る",font=("Times New Roman", 36), command=cli,fg="orange")
    button2.place(x=385,y=450)
    root.mainloop()


def sindan():
    global root
    root.destroy()
    root=tk.Tk()
    root.title("耳年齢")
    root.resizable(False, False)
    root.geometry("880x720")
    root.configure(bg='deepskyblue')
    
    def end():
        root.destroy()
        main_game()
        
    def start():
        global label1,label2,label3,label4,label5,button1,button_end
        label1=tk.Label(root,text="耳年齢診断",font=("",50))
        label2=tk.Label(root,text="周波数を入力してどこまで聞こえるか調べられるよ",font=("",20))
        label3=tk.Label(root,text="イヤホン推奨",font=("",20))
        label4=tk.Label(root,text="音量にはくれぐれも注意してくだい",font=("",20))
        label5=tk.Label(root,text="最悪の場合耳が壊れます",font=("",20))
        label1.pack(pady=30)
        label2.pack(pady=30)
        label3.pack(pady=20)
        label4.pack(pady=20)
        label5.pack(pady=20)
        button1=tk.Button(root,text="スタート！",font=("",20),command=cli1)
        button_end=tk.Button(root,text="ゲームランドに戻る",font=("",20),command=end)
        button1.pack(pady=30)
        button_end.place(x=600,y=600)
    def cli1():
        label1.pack_forget()
        label2.pack_forget()
        label3.pack_forget()
        label4.pack_forget()
        label5.pack_forget()
        button1.pack_forget()
        lev_select()
    def lev_select():
        global label1,label2,bt1,frame1
        label1=tk.Label(root,text="周波数を選んでください",font=("",30))
        label1.pack(pady=30)
        label2=tk.Label(root,text="人の可聴領域は20Hz～20000Hzです。",font=("",20))
        label2.pack(pady=30)
        frame1=tk.Frame(root,bg="deepskyblue")
        bt1=[tk.Button(frame1,text="50Hz",font=("",20),command=Hz50,width=8),
             tk.Button(frame1,text="100Hz",font=("",20),command=Hz100,width=8),
             tk.Button(frame1,text="500Hz",font=("",20),command=Hz500,width=8),
             tk.Button(frame1,text="1000Hz",font=("",20),command=Hz1000,width=8),
             tk.Button(frame1,text="5000Hz",font=("",20),command=Hz5000,width=8),
             tk.Button(frame1,text="10000Hz",font=("",20),command=Hz10000,width=8),
             tk.Button(frame1,text="12500Hz",font=("",20),command=Hz12500,width=8),
             tk.Button(frame1,text="15000Hz",font=("",20),command=Hz15000,width=8),
             tk.Button(frame1,text="17500Hz",font=("",20),command=Hz17500,width=8),
             tk.Button(frame1,text="18000Hz",font=("",20),command=Hz18000,width=8),
             tk.Button(frame1,text="18500Hz",font=("",20),command=Hz18500,width=8),
             tk.Button(frame1,text="19000Hz",font=("",20),command=Hz19000,width=8),
             tk.Button(frame1,text="19500Hz",font=("",20),command=Hz19500,width=8),
             tk.Button(frame1,text="20000Hz",font=("",20),command=Hz20000,width=8)]
        frame1.pack()
        bt1[0].grid(row=0,column=0)
        bt1[1].grid(row=0,column=1)
        bt1[2].grid(row=1,column=0)
        bt1[3].grid(row=1,column=1)
        bt1[4].grid(row=2,column=0)
        bt1[5].grid(row=2,column=1)
        bt1[6].grid(row=3,column=0)
        bt1[7].grid(row=3,column=1)
        bt1[8].grid(row=4,column=0)
        bt1[9].grid(row=4,column=1)
        bt1[10].grid(row=5,column=0)
        bt1[11].grid(row=5,column=1)
        bt1[12].grid(row=6,column=0)
        bt1[13].grid(row=6,column=1)
        
    def Hz50():
        global Hz
        Hz=50
        cli2()
    def Hz100():
        global Hz
        Hz=100
        cli2()
    def Hz500():
        global Hz
        Hz=500
        cli2()
    def Hz1000():
        global Hz
        Hz=1000
        cli2()
    def Hz5000():
        global Hz
        Hz=5000
        cli2()
    def Hz10000():
        global Hz
        Hz=10000
        cli2()
    def Hz12500():
        global Hz
        Hz=12500
        cli2()
    def Hz15000():
        global Hz
        Hz=15000
        cli2()
    def Hz17500():
        global Hz
        Hz=17500
        cli2()
    def Hz18000():
        global Hz
        Hz=18000
        cli2()
    def Hz18500():
        global Hz
        Hz=18500
        cli2()
    def Hz19000():
        global Hz
        Hz=19000
        cli2()
    def Hz19500():
        global Hz
        Hz=19500
        cli2()
    def Hz20000():
        global Hz
        Hz=20000
        cli2()
    def cli2():
        global label1,label2,bt1,kai,kai2,bt_select
        label1.pack_forget()
        label2.pack_forget()
        frame1.pack_forget()
        kai=0
        kai2=0
        listen()
        label1=tk.Label(root,text=str(Hz)+"Hz",font=("",50))
        label1.pack(pady=50)
        bt1=tk.Button(root,text="聞く",font=("",20),command=listen2)
        bt1.pack(pady=10)
        bt_select=tk.Button(root,text="周波数選択に戻る",font=("",20),command=back)
    def back():
        if kai2==0 and kai>0:
            label4.pack_forget()
        bt_select.place_forget()
        label1.pack_forget()
        label2.pack_forget()
        label3.pack_forget()
        bt1.pack_forget()
        frame.pack_forget()
        lev_select()
        
    def listen():
        global rand_num,r
        rand_num=random.randint(1,5)
        rand_sec=[500,1000]
        r=[]
        for i in range(rand_num):
            r.append(None)
            r[i]=random.choice(rand_sec)
    def listen2():
        global label3,frame,bt_num,kai,kai2
        if kai2==0:
            if kai>0:
                label4.pack_forget()
            listen()
        for i in range(rand_num):
            winsound.Beep(int(Hz),r[i])
        if kai==0:
            label3=tk.Label(root,text="何回聞こえましたか？",font=("",20))
            label3.pack(pady=20)
            frame=tk.Frame(root,bg="deepskyblue")
            bt_num=[tk.Button(frame,text="1",font=("",20),width=5,command=ans1),
                    tk.Button(frame,text="2",font=("",20),width=5,command=ans2),
                    tk.Button(frame,text="3",font=("",20),width=5,command=ans3),
                    tk.Button(frame,text="4",font=("",20),width=5,command=ans4),
                    tk.Button(frame,text="5",font=("",20),width=5,command=ans5)]
            for i in range(5):
                bt_num[i].grid(row=0,column=i,padx=5)
            frame.pack(pady=30)
            bt_select.place(x=605,y=500)
        else:
            for i in range(5):
                bt_num[i]["state"]="active"
        kai=1
        kai2=1
    def ans1():
        global ans
        ans=1
        cli3()
    def ans2():
        global ans
        ans=2
        cli3()
    def ans3():
        global ans
        ans=3
        cli3()
    def ans4():
        global ans
        ans=4
        cli3()
    def ans5():
        global ans
        ans=5
        cli3()
    def cli3():
        global label4,kai2
        if ans==rand_num:
            correct()
        else:
            label4=tk.Label(root,text="残念！不正解です\n回数を変えます",font=("",20))
            label4.pack(pady=20)
            kai2=0
            for i in range(5):
                bt_num[i]["state"]="disable"
    def correct():
        global label1,bt_title,bt_select
        label1.pack_forget()
        label2.pack_forget()
        label3.pack_forget()
        bt1.pack_forget()
        button_end.place_forget()
        bt_select.place_forget()
        frame.pack_forget()
        if kai!=0:
            label4.pack_forget()
        label1=tk.Label(root,text="正解です！",font=("",50))
        label1.pack(pady=100)
        bt_title=tk.Button(root,text="タイトルに戻る",font=("",20),command=title)
        bt_select["command"]=select
        bt_title.pack(pady=30)
        bt_select.pack(pady=30)
        button_end.pack(pady=30)
    def reset():
        label1.pack_forget()
        bt_title.pack_forget()
        bt_select.pack_forget()
        button_end.pack_forget()
    def title():
        reset()
        start()
    def select():
        reset()
        lev_select()
    start()
    root.mainloop()

def pazunyan():
    global root,size,key,home,after_id1,after_id2,delete_trigger,up_trigger
    root.destroy()
    root=tk.Tk()
    root.title("パズにゃん")
    root.resizable(False, False)
    root.geometry("880x720")
    root.configure(bg='deepskyblue')
    size=80
    key=""
    home=0
    after_id1=None
    after_id2=None
    delete_trigger=0
    up_trigger=0
    
    def end():
        root.destroy()
        main_game()
    def key_press(e):
        global key,home,ima_x,ima_y,skill_gauge,delete_trigger,up_trigger
        key=e.keysym
        if home==0:
            if key=="Return":
                home=-1
                key_release()
                enter()
            elif key=="Escape":
                key_release()
                end()
        elif home==1:
            if ima_y==8:
                home=2
            if ima_y+1<9:
                if gb[ima_y+1][ima_x]!=0:
                    home=2
            if (key=="Left"  or key=="a") and ima_x-1>=0:
                if gb[ima_y][ima_x-1]==0 and (ima_y<9 or gb[ima_y+1][ima_x]==0):
                    gb[ima_y][ima_x]=0
                    ima_x-=1
                    gb[ima_y][ima_x]=ima
                    canvas1.delete("drop")
                    canvas1.create_image(ima_x*size+size/2,ima_y*size+size/2,image=img2[ima],tag="drop")
                    key_release()
            elif (key=="Right"  or key=="d") and ima_x+1<9:
                if gb[ima_y][ima_x+1]==0 and (ima_y<9 or gb[ima_y+1][ima_x]==0):
                    gb[ima_y][ima_x]=0
                    ima_x+=1
                    gb[ima_y][ima_x]=ima
                    canvas1.delete("drop")
                    canvas1.create_image(ima_x*size+size/2,ima_y*size+size/2,image=img2[ima],tag="drop")
                    key_release()
            elif key=="Up" or key=="w":
                key_release()
                home=-1
                if up_trigger==0:
                    up_trigger=1
                    gb[ima_y][ima_x]=0
                    for y in range(ima_y,9):
                        if gb[y][ima_x]!=0:
                            gb[y-1][ima_x]=ima
                            ima_y=y-1
                            break
                        elif gb[y][ima_x]==0 and y==8:
                            gb[y-1][ima_x]=ima
                            ima_y=y-1
                            break
            elif key=="Shift_L" or key=="Shift_R":
                key_release()
                if skill_gauge>3:
                    delete_trigger=1
                    home=-1
                    skill_gauge=0
                    canvas2.delete("waza")
        elif home==2:
            if ima_y+1<9:
                if gb[ima_y+1][ima_x]!=0:
                    home=2
                else:
                    home=1
    def key_release():
        global key
        key=""
    
    root.bind("<KeyPress>",key_press)
    
    def forgeter():
        label1.pack_forget()
        button1.pack_forget()
        button2.grid_forget()
        button3.grid_forget()
        button4.grid_forget()
        button5.grid_forget()
        button6.grid_forget()
        button7.grid_forget()
        button8.pack_forget()
        frame1.pack_forget()
    def start():
        global label1,frame1,canvas1,img1,label2,label3,label4,label5,home
        home=0
        label1=tk.Label(root,text="パズル&にゃんこ",font=('Microsoft Tai Le',50))
        label1.pack(pady=20)
        frame1=tk.Frame(root,width=1,height=1)
        canvas1=tk.Canvas(frame1,width=184,height=184)
        img1=tk.PhotoImage(file="neko1_184.png")
        canvas1.create_image(184/2,184/2,image=img1)
        label2=tk.Label(frame1,text="謎の生き物ニャフが現れた！",font=('Mistral',20))
        label3=tk.Label(frame1,text="3つそろえて消してみよう！",font=('Mistral',20))
        canvas1.grid(row=0,column=0,rowspan=2)
        label2.grid(row=0,column=1)
        label3.grid(row=1,column=1)
        frame1.pack(pady=20)
        label4=tk.Label(root,text="Please press enter",font=('UD デジタル 教科書体 N-B',20))
        label4.pack(pady=20)
        label5=tk.Label(root,text="Press escape to return to Gameland ",font=('UD デジタル 教科書体 N-B',20))
        label5.pack(pady=20)
    def enter():
        label1.pack_forget()
        canvas1.grid_forget()
        label2.grid_forget()
        label3.grid_forget()
        label4.pack_forget()
        label5.pack_forget()
        frame1.pack_forget()
        enter2()
    def enter2():
        global label1,frame1,button1,button2,button3,button4,button5,button6,button7,button8
        label1=tk.Label(root,text="モードを選択！",font=('UD デジタル 教科書体 NK-R',30))
        label1.pack(pady=20)
        frame1=tk.Frame(root,width=1,height=1,bg="deepskyblue")
        button1=tk.Button(root,text="チュートリアル",font=('Malgun Gothic Semilight',20),command=tutorial)
        button2=tk.Button(frame1,text="60個",font=('Malgun Gothic Semilight',20),command=mode1)
        button3=tk.Button(frame1,text="120個",font=('Malgun Gothic Semilight',20),command=mode2)
        button4=tk.Button(frame1,text="240個",font=('Malgun Gothic Semilight',20),command=mode3)
        button5=tk.Button(frame1,text="480個",font=('Malgun Gothic Semilight',20),command=mode4)
        button6=tk.Button(frame1,text="960個",font=('Malgun Gothic Semilight',20),command=mode5)
        button7=tk.Button(frame1,text="1920個",font=('Malgun Gothic Semilight',20),command=mode6)
        button8=tk.Button(root,text="エンドレス",font=('Malgun Gothic Semilight',20),command=endless)
        button1.pack()
        frame1.pack()
        button2.grid(row=0,column=0)
        button3.grid(row=0,column=1)
        button4.grid(row=0,column=2)
        button5.grid(row=1,column=0)
        button6.grid(row=1,column=1)
        button7.grid(row=1,column=2)
        button8.pack()
    def tutorial():
        global label1,canvas1,img1,zumen,label2,canvas2,button1
        forgeter()
        label1=tk.Label(root,text="ニャフを3つそろえると互いに打ち消しあって消えるよ！",font=('UD デジタル 教科書体 NK-R',30))
        label1.pack(pady=20)
        canvas1=tk.Canvas(root,width=size*3-3,height=size*2-2)
        canvas1.pack()
        img1=[tk.PhotoImage(file="neko1.png"),
              tk.PhotoImage(file="neko_niku.png")]
        zumen=[[0,0,2],
               [1,1,0]]
        backgraund=[[0,1,0],
                    [1,0,1]]
        for y in range(2):
            for x in range(3):
                if backgraund[y][x]==0:
                    canvas1.create_rectangle(x*size,y*size,x*size+size,y*size+size,fill="black",width=0)
                else:
                    canvas1.create_rectangle(x*size,y*size,x*size+size,y*size+size,fill="gray",width=0)
        label2=tk.Label(root,text="3コンボで技ゲージがたまっていくよ！\nシフトを押すと発動できるぞ！",font=('UD デジタル 教科書体 NK-R',30))
        label2.pack(pady=20)
        canvas2=tk.Canvas(root,width=size*2-4,height=size,bg="white")
        canvas2.pack()
        a=0
        tutorial1()
        tutorial5(a)
        button1=tk.Button(root,text="モード選択に戻る",font=("",20),command=tutorial_stop)
        button1.pack(pady=20)
    def tutorial1():
        global root,after_id1
        for y in range(2):
                for x in range(3):
                    if zumen[y][x]==1:
                        canvas1.create_image(x*size+size/2,y*size+size/2,image=img1[0],tag="kieru")
                    elif zumen[y][x]==2:
                        canvas1.create_image(x*size+size/2,y*size+size/2,image=img1[0],tag="otiru")
        after_id1=root.after(800,tutorial2)
    def tutorial2():
        global root,after_id1
        canvas1.delete("otiru")
        canvas1.create_image(size*2+size/2,size+size/2,image=img1[0],tag="kieru")
        after_id1=root.after(800,tutorial3)
    def tutorial3():
        global root,after_id1
        canvas1.delete("kieru")
        for i in range(3):
            canvas1.create_image(i*size+size/2,size+size/2,image=img1[1],tag="niku")
        after_id1=root.after(800,tutorial4)
    def tutorial4():
        global after_id1,root
        canvas1.delete("niku")
        after_id1=root.after(800,tutorial1)
    def tutorial5(a):
        global after_id2,root
        canvas2.create_rectangle(a*size/2,0,a*size/2+size/2-1,size*2,fill="orange",width=0,tag="waza")
        if a==4:
            a=0
            canvas2.delete("waza")
        else:
            a+=1
        after_id2=root.after(800,tutorial5,a)
    def tutorial_stop():
        global root,after_id1,after_id2
        root.after_cancel(after_id1)
        root.after_cancel(after_id2)
        label1.pack_forget()
        label2.pack_forget()
        canvas1.pack_forget()
        canvas2.pack_forget()
        button1.pack_forget()
        enter2()
    def mode1():
        global mode
        forgeter()
        mode="60"
        game()
    def mode2():
        global mode
        forgeter()
        mode="120"
        game()
    def mode3():
        global mode
        forgeter()
        mode="240"
        game()
    def mode4():
        global mode
        forgeter()
        mode="480"
        game()
    def mode5():
        global mode
        forgeter()
        mode="960"
        game()
    def mode6():
        global mode
        forgeter()
        mode="1920"
        game()
    def endless():
        global mode
        forgeter()
        mode="endless"
        game()
    def game():
        global canvas1,r,label2,lev,label3,label4,next_lev,label5,label6,game_clear,label7,canvas2,label8,after_id1,img1,next_lve_basic,r_bace,drop_speed,mode
        tate=9
        yoko=11
        canvas1=tk.Canvas(root,width=size*yoko,height=size*tate)
        canvas1.pack()
        img1=[None,
              tk.PhotoImage(file="neko1_160.png"),
              tk.PhotoImage(file="neko2_160.png"),
              tk.PhotoImage(file="neko3_160.png"),
              tk.PhotoImage(file="neko4_160.png"),
              tk.PhotoImage(file="neko5_160.png"),
              tk.PhotoImage(file="neko6_160.png")]
        r_bace=[[1,2,3],
                [1,2,3],
                [1,2,3],
                [1,2,3,4],
                [1,2,3,4],
                [1,2,3,4],
                [1,2,3,4,5],
                [1,2,3,4,5],
                [1,2,3,4,5],
                [1,2,3,4,5,6]]
        drop_speed=[1000,600,400,200]
        lev=1
        r0=random.choices(r_bace[lev-1],k=5)
        r=random.choice(r0)
        next_lve_basic=[9,18,27,36,45,54,63,72,81]
        next_lev=next_lve_basic[lev-1]
        game_clear=0
        label2=tk.Label(canvas1,text="Lev."+str(lev),font=("",30))
        label3=tk.Label(canvas1,text="次のレベルまで",font=("",17))
        label4=tk.Label(canvas1,text=str(next_lev)+"匹",font=("",30))
        if mode=="endless":
            label5=tk.Label(canvas1,text="消した数",font=("",30))
            label6=tk.Label(canvas1,text=str(game_clear)+"匹",font=("",30))
        else:
            if mode=="60":
                game_clear=60
            elif mode=="120":
                game_clear=120
            elif mode=="240":
                game_clear=240
            elif mode=="480":
                game_clear=480
            elif mode=="960":
                game_clear=960
            elif mode=="1920":
                game_clear=1920
            label5=tk.Label(canvas1,text="クリアまで",font=("",25))
            label6=tk.Label(canvas1,text=str(game_clear)+"匹",font=("",30))
        label7=tk.Label(canvas1,text="技ゲージ",font=("",30))
        canvas2=tk.Canvas(canvas1,width=size*2,height=size)
        background=[[0,1,0,1,0,1,0,1,0,3,2],
                    [1,0,1,0,1,0,1,0,1,2,2],
                    [0,1,0,1,0,1,0,1,0,4,2],
                    [1,0,1,0,1,0,1,0,1,5,2],
                    [0,1,0,1,0,1,0,1,0,6,2],
                    [1,0,1,0,1,0,1,0,1,7,2],
                    [0,1,0,1,0,1,0,1,0,8,2],
                    [1,0,1,0,1,0,1,0,1,9,2],
                    [0,1,0,1,0,1,0,1,0,10,2]]
        for y in range(tate):
                for x in range(yoko):
                    if background[y][x]==0:
                        canvas1.create_rectangle(x*size,y*size,x*size+size,y*size+size,fill="black",width=0)
                    elif background[y][x]==1:
                        canvas1.create_rectangle(x*size,y*size,x*size+size,y*size+size,fill="gray",width=0)
                    elif background[y][x]==3:
                        canvas1.create_image(x*size+size,y*size+size,image=img1[r],tag="next")
                    elif background[y][x]==4:
                        label2.place(x=x*size,y=y*size,width=size*2,height=size)
                    elif background[y][x]==5:
                        label3.place(x=x*size,y=y*size,width=size*2,height=size)
                    elif background[y][x]==6:
                        label4.place(x=x*size,y=y*size,width=size*2,height=size)
                    elif background[y][x]==7:
                        label5.place(x=x*size,y=y*size,width=size*2,height=size)
                    elif background[y][x]==8:
                        label6.place(x=x*size,y=y*size,width=size*2,height=size)
                    elif background[y][x]==9:
                        label7.place(x=x*size,y=y*size,width=size*2,height=size)
                    elif background[y][x]==10:
                        canvas2.place(x=x*size,y=y*size)
        count_down=3
        label8=tk.Label(canvas1,text="",font=("",30))
        label8.place(x=size*3,y=size*4,width=size*3,height=size)
        after_id1=None
        game_start_message(count_down)
    def game_start_message(count_down):
        global after_id1,canvas1
        if count_down>=0:
            if count_down>0:
                label8["text"]=count_down
            elif count_down==0:
                label8["text"]="start!"
            count_down-=1
            after_id1=canvas1.after(1000,game_start_message,count_down)
        else:
            game_start_stop()
    def game_start_stop():
        global after_id1,canvas1,gb,img2,koutei,check,label_rensa,skill_gauge
        canvas1.after_cancel(after_id1)
        label8.place_forget()
        gb=[]
        check=[]
        for i in range(9):
            gb.append([0,0,0,0,0,0,0,0,0])
            check.append([0,0,0,0,0,0,0,0,0])
        img2=[None,
              tk.PhotoImage(file="neko1.png"),
              tk.PhotoImage(file="neko2.png"),
              tk.PhotoImage(file="neko3.png"),
              tk.PhotoImage(file="neko4.png"),
              tk.PhotoImage(file="neko5.png"),
              tk.PhotoImage(file="neko6.png"),
              tk.PhotoImage(file="neko_niku.png")]
        after_id1=None
        koutei=0
        skill_gauge=0
        label_rensa=tk.Label(canvas1,text="",font=("",20),bg="greenyellow")
        game_start()
    def game_start():
        global r,ima,ima_x,ima_y,after_id1,canvas1,home,speed_lev,rensa,up_trigger
        ima_x=4
        ima_y=0
        ima=r
        home=1
        rensa=0
        canvas1.delete("next")
        canvas1.create_image(ima_x*size+size/2,size/2,image=img2[r],tag="drop")
        gb[ima_y][ima_x]=ima
        r0=random.choices(r_bace[lev-1],k=20)
        r=random.choice(r0)
        canvas1.create_image(9*size+size,size,image=img1[r],tag="next")
        up_trigger=0
        if lev==1 or lev==4 or lev==7:
            speed_lev=0
        elif lev==2 or lev==5 or lev==8:
            speed_lev=1
        elif lev==3 or lev==6 or lev==9:
            speed_lev=2
        else:
            speed_lev=3
        if game_clear==0 and mode!="endless":
            clear()
        else:
            after_id1=canvas1.after(800,neko_drop)
    def neko_drop():
        global ima_x,ima_y,canvas1,after_id1
        if ima_y+1>=9:
            canvas1.delete("drop")
            canvas1.create_image(ima_x*size+size/2,ima_y*size+size/2,image=img2[ima],tag="kotei")
            neko_delete()
        elif gb[ima_y+1][ima_x]!=0:
            canvas1.delete("drop")
            canvas1.create_image(ima_x*size+size/2,ima_y*size+size/2,image=img2[ima],tag="kotei")
            neko_delete()
        else:
            gb[ima_y][ima_x]=0
            ima_y+=1
            gb[ima_y][ima_x]=ima
            canvas1.delete("drop")
            canvas1.create_image(ima_x*size+size/2,ima_y*size+size/2,image=img2[ima],tag="drop")
            if key=="Down" or key=="s":
                key_release()
                if lev==10:
                    after_id1=canvas1.after(200,neko_drop)
                else:
                    after_id1=canvas1.after(300,neko_drop)
            else:
                after_id1=canvas1.after(drop_speed[speed_lev],neko_drop)
    def neko_delete():
        global koutei,check,next_lev,lev,game_clear,canvas1,after_id1,rensa,skill_gauge,home,delete_trigger
        if delete_trigger==1:
            delete_trigger=0
            skill_rondom=[]
            z=0
            for y in range(9):
                for x in range(9):
                    if gb[y][x]!=0:
                        skill_rondom.append(None)
                        skill_rondom[z]=gb[y][x]
                        z+=1
            random_delete=random.choice(skill_rondom)
            for y in range(9):
                for x in range(9):
                    if gb[y][x]==random_delete:
                        gb[y][x]=7
        for y in range(9):
            for x in range(9):
                check[y][x]=gb[y][x]
        if koutei<=1:
            koutei+=1
            game_start()
        elif koutei==2:
            home=-1
            for y in range(9):
                for x in range(9):
                    if check[y][x]!=0:
                        if x-1>=0 and x+1<9:
                            if check[y][x-1]==check[y][x] and check[y][x]==check[y][x+1]:
                                gb[y][x-1]=gb[y][x]=gb[y][x+1]=7
                        if x+1<9 and y+1<9:
                            if check[y][x]==check[y][x+1] and check[y][x]==check[y+1][x]:
                                gb[y][x]=gb[y][x+1]=gb[y+1][x]=7
                            if check[y][x]==check[y][x+1] and check[y][x]==check[y+1][x+1]:
                                gb[y][x]=gb[y][x+1]=gb[y+1][x+1]=7
                        if y>0 and x+1<9:
                            if check[y-1][x]==check[y][x] and check[y][x]==check[y][x+1]:
                                gb[y-1][x]=gb[y][x]=gb[y][x+1]=7
                            if check[y-1][x+1]==check[y][x] and check[y][x]==check[y][x+1]:
                                gb[y-1][x+1]=gb[y][x]=gb[y][x+1]=7
                        if y-1>=0 and y+1<9:
                            if check[y][x]!=0 and check[y-1][x]==check[y][x] and check[y][x]==check[y+1][x]:
                                gb[y-1][x]=gb[y][x]=gb[y+1][x]=7
            canvas1.delete("kotei")
            for y in range(9):
                for x in range(9):
                    if gb[y][x]!=0:
                        if gb[y][x]==7:
                            canvas1.create_image(x*size+size/2,y*size+size/2,image=img2[gb[y][x]],tag="kieru")
                        else:
                            canvas1.create_image(x*size+size/2,y*size+size/2,image=img2[gb[y][x]],tag="kotei")
            koutei=3
            after_id1=canvas1.after(800,neko_delete)
        elif koutei==3:
            trigger=0
            canvas1.delete("kieru")
            def rensa_loop(a):
                global after_id1,canvas1
                if rensa%2==1:
                    label_rensa.place(x=size,y=a+size*4,width=160,height=80)
                else:
                    label_rensa.place(x=size*6,y=a+size*3,width=160,height=80)
                if a!=-1:
                    a-=1
                    after_id1=canvas1.after(10,rensa_loop,a)
                else:
                    label_rensa.place_forget()
            for y in range(9):
                for x in range(9):
                    if gb[y][x]==7:
                        gb[y][x]=0
                        next_lev-=1
                        if mode=="endless":
                            game_clear+=1
                        else:
                            game_clear-=1
                        if trigger==0:
                            rensa+=1
                            trigger=1
                            label_rensa["text"]=str(rensa)+"コンボ"
                            a=40
                            rensa_loop(a)
                            if rensa%3==0:
                                skill_gauge+=1
            koutei=2
            if lev<10:
                if next_lev<1:
                    lev+=1
                    label2["text"]="Lev."+str(lev)
                    if lev<10:
                        next_lev=next_lve_basic[lev-1]
                    else:
                        next_lev=0
                label4["text"]=str(next_lev)+"匹"
                if lev>9:
                    label4["text"]="∞"
            else:
                lev=10
                label2["text"]="Lev."+str(lev)
                label4["text"]="∞"
            if game_clear<0:
                game_clear=0
            label6["text"]=str(game_clear)+"匹"
            if skill_gauge>0:
                canvas2.delete("waza")
                if skill_gauge>4:
                    skill_gauge=4
                for i in range(skill_gauge):
                    canvas2.create_rectangle(i*size/2,0,i*size/2+size/2-1,size*2,fill="orange",width=0,tag="waza")
            trigger=0
            for y in range(8,-1,-1):
                for x in range(8,-1,-1):
                    if gb[y][x]==0:
                        for z in range(y,-1,-1):
                            if gb[z][x]!=0:
                                gb[y][x]=gb[z][x]
                                gb[z][x]=0
                                trigger=1
                                break
            canvas1.delete("kotei")
            for y in range(9):
                for x in range(9):
                    canvas1.create_image(x*size+size/2,y*size+size/2,image=img2[gb[y][x]],tag="kotei")
            if trigger==1:
                after_id1=canvas1.after(800,neko_delete)
            else:
                if gb[0][4]!=0:
                    game_over()
                else:
                    game_start()
    def game_over():
        global after_id1,canvas1,label1,button1,button2,frame1,button3
        canvas1.after_cancel(after_id1)
        canvas1.pack_forget()
        label1=tk.Label(root,text="ゲームオーバー",font=("",50),bg="green",fg="red")
        label1.pack(expand=1)
        frame1=tk.Frame(root,width=0,height=0,bg="deepskyblue")
        button1=tk.Button(frame1,text="もう一度同じモードをプレイする",font=("",20),command=replay)
        button2=tk.Button(frame1,text="レベル選択画面に戻る",font=("",20),command=lev_choice)
        button3=tk.Button(frame1,text="タイトルに戻る",font=("",20),command=loop)
        button1.pack()
        button2.pack(pady=50)
        button3.pack()
        frame1.pack(expand=1)
    def clear():
        global after_id1,canvas1,label1,button1,button2,frame1,button3
        canvas1.after_cancel(after_id1)
        canvas1.pack_forget()
        label1=tk.Label(root,text="クリアおめでとう！",font=("",50))
        label1.pack(expand=1)
        frame1=tk.Frame(root,width=0,height=0,bg="deepskyblue")
        button1=tk.Button(frame1,text="もう一度同じモードをプレイする",font=("",20),command=replay)
        button2=tk.Button(frame1,text="レベル選択画面に戻る",font=("",20),command=lev_choice)
        button3=tk.Button(frame1,text="タイトルに戻る",font=("",20),command=loop)
        button1.pack()
        button2.pack(pady=50)
        button3.pack()
        frame1.pack(expand=1)
    def loop_set():
        label1.pack_forget()
        frame1.destroy()
    def replay():
        loop_set()
        game()
    def lev_choice():
        loop_set()
        enter2()
    def loop():
        loop_set()
        start()
    start()
    root.mainloop()

def main_game():
    global root
    root=tk.Tk()
    root.title("ゲームランド")
    root.resizable(False, False)
    root.geometry("1200x900")
    root.configure(bg='DimGray')
    label1=tk.Label(root,text="ゲームランドにようこそ！",font=("System",24),width=25)
    label2=tk.Label(root,text="下からやりたいゲームを押して選んでね",font=("System",20),width=50)
    label1.pack(pady=60)
    label2.pack()
    frame=tk.Frame(root,width=0,height=0,bg='DimGray')
    frame.pack(pady=100)
    button1=tk.Button(frame,text="文字探し",width=14,height=1,font=("Times New Roman",24),command=moji)
    button2=tk.Button(frame,text="数当てゲーム",width=14,height=1,font=("Times New Roman",24),command=kazuate)
    button3=tk.Button(frame,text="迷路",width=14,height=1,font=("Times New Roman",24),command=meiro)
    button4=tk.Button(frame,text="おみくじ",width=14,height=1,font=("Times New Roman",24),command=omikuji)
    button5=tk.Button(frame,text="診断",width=14,height=1,font=("Times New Roman",24),command=sindan)
    button6=tk.Button(frame,text="パズル&にゃんこ",width=14,height=1,font=("Times New Roman",24),command=pazunyan)
    button1.grid(row=0,column=0,padx=50,pady=30)
    button2.grid(row=1,column=0,padx=50,pady=30)
    button3.grid(row=2,column=0,padx=50,pady=30)
    button4.grid(row=0,column=1,padx=50,pady=30)
    button5.grid(row=1,column=1,padx=50,pady=30)
    button6.grid(row=2,column=1,padx=50,pady=30)
    root.mainloop()

main_game()