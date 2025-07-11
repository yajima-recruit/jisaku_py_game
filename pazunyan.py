#ぷよぷよもどき
import tkinter as tk
import random
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
    frame1=tk.Frame(root,width=1,height=1,bg="yellow")
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