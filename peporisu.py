#テトリス
import tkinter as tk
import random
root=tk.Tk()
root.title("ぺポリス")
root.resizable(False, False)
root.geometry("1000x800")
root.configure(bg='yellowgreen')
#ミノの大きさは35x35
mino_size=35
home=-1
key=""
after_id1=None
mino_color=[None,
            "red",
            "violet",
            "blue",
            "green",
            "orange",
            "gray",
            "gold"]
mino=[None,
      [[[0,0,0,0],# Tミノ
        [0,1,0,0],
        [1,1,1,0],
        [0,0,0,0]],# 0°
       [[0,0,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,1,0,0]],# 90°
       [[0,0,0,0],
        [0,0,0,0],
        [1,1,1,0],
        [0,1,0,0]],# 180°
       [[0,0,0,0],
        [0,1,0,0],
        [1,1,0,0],
        [0,1,0,0]]],# 270°
      [[[0,0,0,0],# Sミノ
        [0,2,2,0],
        [2,2,0,0],
        [0,0,0,0]],# 0°
       [[0,0,0,0],
        [0,2,0,0],
        [0,2,2,0],
        [0,0,2,0]],# 90°
       [[0,0,0,0],
        [0,0,0,0],
        [0,2,2,0],
        [2,2,0,0]],# 180°
       [[0,0,0,0],
        [2,0,0,0],
        [2,2,0,0],
        [0,2,0,0]]],# 270°
      [[[0,0,0,0],# Zミノ
        [3,3,0,0],
        [0,3,3,0],
        [0,0,0,0]],# 0°
       [[0,0,0,0],
        [0,0,3,0],
        [0,3,3,0],
        [0,3,0,0]],# 90°
       [[0,0,0,0],
        [0,0,0,0],
        [3,3,0,0],
        [0,3,3,0]],# 180°
       [[0,0,0,0],
        [0,3,0,0],
        [3,3,0,0],
        [3,0,0,0]]],# 270°
      [[[0,0,0,0],# Lミノ
        [0,0,4,0],
        [4,4,4,0],
        [0,0,0,0]],# 0°
       [[0,0,0,0],
        [0,4,0,0],
        [0,4,0,0],
        [0,4,4,0]],# 90°
       [[0,0,0,0],
        [0,0,0,0],
        [4,4,4,0],
        [4,0,0,0]],# 180°
       [[0,0,0,0],
        [4,4,0,0],
        [0,4,0,0],
        [0,4,0,0]]],# 270°
      [[[0,0,0,0],# Jミノ
        [5,0,0,0],
        [5,5,5,0],
        [0,0,0,0]],# 0°
       [[0,0,0,0],
        [0,5,5,0],
        [0,5,0,0],
        [0,5,0,0]],# 90°
       [[0,0,0,0],
        [0,0,0,0],
        [5,5,5,0],
        [0,0,5,0]],# 180°
       [[0,0,0,0],
        [0,5,0,0],
        [0,5,0,0],
        [5,5,0,0]]],# 270°
      [[[0,0,0,0],# Oミノ
        [0,6,6,0],
        [0,6,6,0],
        [0,0,0,0]],#　0°
       [[0,0,0,0],
        [0,6,6,0],
        [0,6,6,0],
        [0,0,0,0]],#　90°
       [[0,0,0,0],
        [0,6,6,0],
        [0,6,6,0],
        [0,0,0,0]],#　180°
       [[0,0,0,0],
        [0,6,6,0],
        [0,6,6,0],
        [0,0,0,0]]],#　270°
      [[[0,0,0,0],# Iミノ
        [0,0,0,0],
        [7,7,7,7],
        [0,0,0,0]],# 0°
       [[0,7,0,0],
        [0,7,0,0],
        [0,7,0,0],
        [0,7,0,0]],# 90°
       [[0,0,0,0],
        [7,7,7,7],
        [0,0,0,0],
        [0,0,0,0]],# 180°
       [[0,0,7,0],
        [0,0,7,0],
        [0,0,7,0],
        [0,0,7,0]]]]# 270°

def end():
    root.destroy()
def key_press(e):
    global key,home,ima_x,ima_y,gb,cv1,kakudo,ima_mino
    key=e.keysym
    if home==0:
        if key=="Return":
            home=-1
            key=""
            hamu_forget()
        elif key=="Escape":
            key=""
            end()
    if home==1:
        pass
root.bind("<KeyPress>",key_press)

def start():
    global label1,frame1,cv1,img1,label2,label3,label4,home
    home=0
    label1=tk.Label(root,text="ぺポリス",font=('Microsoft Tai Le',50))
    label1.pack(pady=20)
    frame1=tk.Frame(root,width=1,height=1)
    cv1=tk.Canvas(frame1,width=mino_size*3,height=mino_size*2)
    sumple=[[1,1,1],
          [0,1,0]]
    for y in range(2):
        for x in range(3):
            if sumple[y][x]==1:
                cv1.create_rectangle(x*mino_size,y*mino_size,x*mino_size+mino_size-1,y*mino_size+mino_size-1,fill=mino_color[1],width=0)
            else:
                cv1.create_rectangle(x*mino_size,y*mino_size,x*mino_size+mino_size,y*mino_size+mino_size,fill="white",width=0)
    label2=tk.Label(frame1,text="落ちてくるぺポリミノを一列そろえて消そう",font=("",20))
    cv1.grid(row=0,column=0)
    label2.grid(row=0,column=1)
    frame1.pack(pady=20)
    label3=tk.Label(root,text="Please press enter",font=('UD デジタル 教科書体 N-B',20))
    label3.pack(pady=20)
    label4=tk.Label(root,text="Press escape to return to Gameland ",font=('UD デジタル 教科書体 N-B',20))
    label4.pack(pady=20)
def hamu_forget():
    label1.destroy()
    label2.destroy()
    label3.destroy()
    label4.destroy()
    frame1.destroy()
    cv1.destroy()
    hamu()
def hamu():
    global cv1,gb,frame1,cv2,cv3,gb_next,gb_hold,label2,label3,after_id1,next_mino,num
    
    frame1=tk.Frame(root,bg="yellowgreen")
    frame1.pack(expand=1)
    cv1=tk.Canvas(frame1,width=mino_size*12,height=mino_size*21-1,highlightthickness=0)
    cv2=tk.Canvas(frame1,width=mino_size*5,height=mino_size*6-1,highlightthickness=0)
    cv3=tk.Canvas(frame1,width=mino_size*5,height=mino_size*17-1,highlightthickness=0)
    cv2.pack(side=tk.LEFT,anchor=tk.N,expand=1)
    cv1.pack(side=tk.LEFT,anchor=tk.N,expand=1)
    cv3.pack(side=tk.LEFT,anchor=tk.N,expand=1)
    gb=[[9,0,0,0,0,0,0,0,0,0,0,9],
        [9,0,0,0,0,0,0,0,0,0,0,9],
        [9,0,0,0,0,0,0,0,0,0,0,9],
        [9,0,0,0,0,0,0,0,0,0,0,9],
        [9,0,0,0,0,0,0,0,0,0,0,9],
        [9,0,0,0,0,0,0,0,0,0,0,9],
        [9,0,0,0,0,0,0,0,0,0,0,9],
        [9,0,0,0,0,0,0,0,0,0,0,9],
        [9,0,0,0,0,0,0,0,0,0,0,9],
        [9,0,0,0,0,0,0,0,0,0,0,9],
        [9,0,0,0,0,0,0,0,0,0,0,9],
        [9,0,0,0,0,0,0,0,0,0,0,9],
        [9,0,0,0,0,0,0,0,0,0,0,9],
        [9,0,0,0,0,0,0,0,0,0,0,9],
        [9,0,0,0,0,0,0,0,0,0,0,9],
        [9,0,0,0,0,0,0,0,0,0,0,9],
        [9,0,0,0,0,0,0,0,0,0,0,9],
        [9,0,0,0,0,0,0,0,0,0,0,9],
        [9,0,0,0,0,0,0,0,0,0,0,9],
        [9,0,0,0,0,0,0,0,0,0,0,9],
        [9,9,9,9,9,9,9,9,9,9,9,9]]
    for y in range(21):
        for x in range(12):
            if gb[y][x]==9:
                cv1.create_rectangle(x*mino_size,y*mino_size,x*mino_size+mino_size-1,y*mino_size+mino_size-1,fill="deepskyblue",width=0)
            if gb[y][x]==0:
                cv1.create_rectangle(x*mino_size,y*mino_size,x*mino_size+mino_size-1,y*mino_size+mino_size-1,fill="white",width=0)
    gb_hold=[[1,2,1,1,1],
             [1,0,0,0,0],
             [1,0,0,0,0],
             [1,0,0,0,0],
             [1,0,0,0,0],
             [1,1,1,1,1]]
    label1=tk.Label(cv2,text="HOLD",font=("",25),bg="deepskyblue")
    for y in range(6):
        for x in range(5):
            if gb_hold[y][x]==1:
                cv2.create_rectangle(x*mino_size,y*mino_size,x*mino_size+mino_size-1,y*mino_size+mino_size-1,fill="deepskyblue",width=0)
            elif gb_hold[y][x]==2:
                label1.place(x=x*mino_size,y=y*mino_size,width=mino_size*4-1,height=mino_size-1)
    gb_next=[[2,1,1,1,1],
             [0,0,0,0,1],
             [0,0,0,0,1],
             [0,0,0,0,1],
             [0,0,0,0,1],
             [0,0,0,0,1],
             [0,0,0,0,1],
             [0,0,0,0,1],
             [0,0,0,0,1],
             [0,0,0,0,1],
             [0,0,0,0,1],
             [0,0,0,0,1],
             [0,0,0,0,1],
             [0,0,0,0,1],
             [0,0,0,0,1],
             [0,0,0,0,1],
             [1,1,1,1,1]]
    label2=tk.Label(cv3,text="NEXT",font=("",25),bg="deepskyblue")
    for y in range(17):
        for x in range(5):
            if gb_next[y][x]==1:
                cv3.create_rectangle(x*mino_size,y*mino_size,x*mino_size+mino_size-1,y*mino_size+mino_size-1,fill="deepskyblue",width=0)
            elif gb_next[y][x]==2:
                label2.place(x=x*mino_size,y=y*mino_size,width=mino_size*4-1,height=mino_size-1)
    next_mino=[]
    num=[1,2,3,4,5,6,7]
    for i in range(2):
        random.shuffle(num)
        next_mino+=num
    ima_y=0
    for i in range(5):
        for y in range(1,4):
            for x in range(4):
                gb_next[y+ima_y][x]=mino[next_mino[i]][0][y][x]
        ima_y+=3
        if ima_y<15:
            cv3.create_rectangle(0,mino_size*(ima_y+1)-2,mino_size*4,mino_size*(ima_y+1)+2,fill="black")
    for y in range(1,15):
        for x in range(4):
            if 0<gb_next[y][x] and gb_next[y][x]<6:
                cv3.create_rectangle(mino_size*x+mino_size/2,mino_size*y+mino_size/2, mino_size*x+mino_size+mino_size/2-1,mino_size*y+mino_size+mino_size/2-1,fill=mino_color[gb_next[y][x]],width=0,tag="next")
            elif gb_next[y][x]==6:
                cv3.create_rectangle(mino_size*x,mino_size*y+mino_size/2, mino_size*x+mino_size-1,mino_size*y+mino_size+mino_size/2-1,fill=mino_color[gb_next[y][x]],width=0,tag="next")
            elif gb_next[y][x]==7:
                cv3.create_rectangle(mino_size*x,mino_size*y, mino_size*x+mino_size-1,mino_size*y+mino_size-1,fill=mino_color[gb_next[y][x]],width=0,tag="next")
            
    count_down=3
    label3=tk.Label(cv1,text="",font=("",30))
    label3.place(x=mino_size*4,y=mino_size*10,width=mino_size*4,height=mino_size)
    after_id1=None
    game_start_message(count_down)
def game_start_message(count_down):
    global after_id1,cv1
    if count_down>=0:
        if count_down>0:
            label3["text"]=count_down
        else:
            label3["text"]="start!"
        count_down-=1
        after_id1=cv1.after(1000,game_start_message,count_down)
    else:
        game_message_stop()
def game_message_stop():
    global after_id1,cv1,gb,check
    cv1.after_cancel(after_id1)
    label3.place_forget()
    check=[]
    for i in range(20):
        check.append([9,0,0,0,0,0,0,0,0,0,0,9])
    check.append([9 for i in range(12)])
    after_id1=None
    game_start()
def game_start():
    global ima_y,ima_x,ima,home,next_mino,after_id1,cv1,kakudo,ima_mino
    def mino_check():
        for i in range(4,8):
            if gb[0][i]!=0:
                return False
        return True
    ima_x=5
    ima_y=0
    home=1
    kakudo=0
    ima=next_mino[0]
    ima_mino=mino[ima][kakudo]
    for i in range(len(next_mino)-1):
        next_mino[i]=next_mino[i+1]
    del next_mino[-1]
    if len(next_mino)<8:
        random.shuffle(num)
        next_mino+=num
    cv3.delete("next")
    for y in range(1,15):
        for x in range(4):
            gb_next[y][x]=0
    a=0
    for i in range(5):
        for y in range(1,4):
            for x in range(4):
                gb_next[y+a][x]=mino[next_mino[i]][0][y][x]
        a+=3
    for y in range(1,15):
        for x in range(4):
            if 0<gb_next[y][x] and gb_next[y][x]<6:
                cv3.create_rectangle(mino_size*x+mino_size/2,mino_size*y+mino_size/2, mino_size*x+mino_size+mino_size/2-1,mino_size*y+mino_size+mino_size/2-1,fill=mino_color[gb_next[y][x]],width=0,tag="next")
            elif gb_next[y][x]==6:
                cv3.create_rectangle(mino_size*x,mino_size*y+mino_size/2, mino_size*x+mino_size-1,mino_size*y+mino_size+mino_size/2-1,fill=mino_color[gb_next[y][x]],width=0,tag="next")
            elif gb_next[y][x]==7:
                cv3.create_rectangle(mino_size*x,mino_size*y, mino_size*x+mino_size-1,mino_size*y+mino_size-1,fill=mino_color[gb_next[y][x]],width=0,tag="next")
    if mino_check():
        i=0
        for x in range(ima_x-1,ima_x+3):
            check[0][x]=mino[ima][kakudo][2][i]
            i+=1
        for y in range(20):
            for x in range(1,11):
                if check[y][x]>0:
                    cv1.create_rectangle(mino_size*x,mino_size*y, mino_size*x+mino_size-1,mino_size*y+mino_size-1,fill=mino_color[check[y][x]],width=0,tag="drop")
        for i in range(21):
            print(check[i])
        print()
        after_id1=cv1.after(1000,mino_drop)
    else:
        print("ゲームオーバー")
def mino_drop():
    global gb,ima_y,ima_x,after_id1,cv1,delete_trigger
    def height_check():
        if ima_y-2<0:
            return 2-ima_y
        else:
            return 0
    cv1.delete("drop")
    a=0
    for y in range(20):
        for x in range(1,11):
            if check[y][x]!=0 and gb[y+1][x]!=0:
                a=1
    if a==1:
        #1秒後に発動
        mino_lock()
    else:
        for y in range(20):
            for x in range(1,11):
                if check[y][x]!=0:
                    check[y][x]=0
        ima_y+=1
        for y in range(height_check(),4):
            a=0
            for x in range(ima_x-1,ima_x+3):
                if ima_mino[y][a]!=0:
                    check[ima_y+(y-2)][x]=ima_mino[y][a]
                a+=1
        for y in range(20):
            for x in range(1,11):
                if check[y][x]>0:
                    cv1.create_rectangle(mino_size*x,mino_size*y, mino_size*x+mino_size-1,mino_size*y+mino_size-1,fill=mino_color[check[y][x]],width=0,tag="drop")
        for i in range(21):
            print(check[i])
        after_id1=cv1.after(1000,mino_drop)
def mino_lock():
    pass
def mino_delete():
    global home,gb,after_id1,cv1
    home=-1
    cv1.delete("drop")
    gb[ima_y][ima_x]=0
    if ima==7:
        if kakudo==0:
            y=0
            for x in range(-1,3):
                gb[ima_y+y][ima_x+x]=ima
        elif kakudo==90:
            x=0
            for y in range(-1,3):
                gb[ima_y+y][ima_x]=ima
    elif ima<6:
        if kakudo==0:
            for y in range(2):
                for x in range(3):
                    if ima_mino[y][x]!=0:
                        gb[ima_y+y][ima_x+x-1]=ima_mino[y][x]
        elif kakudo==90:
            for y in range(3):
                for x in range(2):
                    if ima_mino[y][x]!=0:
                        gb[ima_y+y][ima_x+x-1]=ima_mino[y][x]
    else:
        for y in range(2):
            for x in range(2):
                gb[ima_y+y][ima_x+x]=ima
    for y in range(20):
        for x in range(1,11):
            if gb[y][x]!=0:
                cv1.create_rectangle(x*mino_size,y*mino_size,x*mino_size+mino_size-1,y*mino_size+mino_size-1,width=0,tag="kotei",fill=mino_color[gb[y][x]-1])
    after_id1=cv1.after(500,game_start)
start()
root.mainloop()
cv1.after_cancel(after_id1)