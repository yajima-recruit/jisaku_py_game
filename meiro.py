#迷路
import tkinter as tk
import random
root=tk.Tk()
root.title("一筆書き迷路")
root.resizable(False, False)
root.geometry("1200x900")
root.configure(bg='orange')
after_id=None

def end():
    root.destroy()

def start():
    global frame1,canvas1,img,label1,label2,label3,label4,button1,button0,key,label5
    label1=tk.Label(root,text="一7筆書き迷路！",font=("ＭＳ Ｐ明朝",50))
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
    label5.pack()
    label4.pack()
    button1.pack()
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
    buttonR.pack()
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