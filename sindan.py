#診断
import tkinter as tk
import random
import winsound
    root=tk.Tk()
    root.title("耳年齢")
    root.resizable(False, False)
    root.geometry("880x720")
    root.configure(bg='deepskyblue')
    
    def end():
        root.destroy()
        
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
        global label1,label2,bt1,bt2,bt3,bt4,bt5
        label1=tk.Label(root,text="周波数を選んでください",font=("",30))
        label1.pack(pady=30)
        label2=tk.Label(root,text="人の可聴領域は20Hz～20000Hzです。",font=("",20))
        label2.pack(pady=30)
        frame1=tk.Frame(root,width=600,height=0)
        bt1=[tk.Button(frame1,text="50Hz",font=("",20),command=Hz50),
             tk.Button(frame1,text="100Hz",font=("",20),command=Hz100),
             tk.Button(frame1,text="500Hz",font=("",20),command=Hz500),
             tk.Button(frame1,text="1000Hz",font=("",20),command=Hz1000),
             tk.Button(frame1,text="5000Hz",font=("",20),command=Hz5000),
             tk.Button(frame1,text="10000Hz",font=("",20),command=Hz10000),
             tk.Button(frame1,text="12500Hz",font=("",20),command=Hz12500),
             tk.Button(frame1,text="15000Hz",font=("",20),command=Hz15000),
             tk.Button(frame1,text="17500Hz",font=("",20),command=Hz17500),
             tk.Button(frame1,text="18000Hz",font=("",20),command=Hz18000),
             tk.Button(frame1,text="18500Hz",font=("",20),command=Hz18500),
             tk.Button(frame1,text="19000Hz",font=("",20),command=Hz19000),
             tk.Button(frame1,text="19500Hz",font=("",20),command=Hz19500),
             tk.Button(frame1,text="20000Hz",font=("",20),command=Hz20000)]
        frame1.pack()
        for i in range(7):
            for j in range(2):
                if j%2==0:
                    bt1[i].grid(row=i,column=0)
                else:
                    bt1[i].grid(row=i,column=1)
    def Hz50():
        global Hz
        Hz=50
        listen()
    def Hz100():
        global Hz
        Hz=100
        listen()
    def Hz500():
        global Hz
        Hz=500
        listen()
    def Hz1000():
        global Hz
        Hz=1000
        listen()
    def Hz5000():
        global Hz
        Hz=5000
        listen()
    def Hz10000():
        global Hz
        Hz=10000
        listen()
    def Hz12500():
        global Hz
        Hz=12500
        listen()
    def Hz15000():
        global Hz
        Hz=15000
        listen()
    def Hz17500():
        global Hz
        Hz=17500
        listen()
    def Hz18000():
        global Hz
        Hz=18000
        listen()
    def Hz18500():
        global Hz
        Hz=18500
        listen()
    def Hz19000():
        global Hz
        Hz=19000
        listen()
    def Hz19500():
        global Hz
        Hz=19500
        listen()
    def Hz20000():
        global Hz
        Hz=20000
        listen()
    def listen():
        global rand_num,r
        rand_num=random.randint(1,5)
        rand_sec=[500,600,700,800,900,1000]
        r=[]
        for i in range(rand_num):
            r.append(None)
            r[i]=random.choice(rand_sec)
        listen2()
    def listen2():
        for i in range(rand_num):
            winsound.Beep(int(Hz),r[i])
        
    start()
    root.mainloop()