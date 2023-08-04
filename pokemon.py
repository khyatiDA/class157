from tkinter import *
from PIL import Image , ImageTk
import random
window = Tk()

window.title("Pokemon Game")
window.geometry("600x600")
window.config(background="orange2")


img1 = ImageTk.PhotoImage(Image.open("squirtle.jpg"))
img2 = ImageTk.PhotoImage(Image.open("abra.jpg"))
img3 = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
img4 = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
img5 = ImageTk.PhotoImage(Image.open("button.jpg"))
img6 = ImageTk.PhotoImage(Image.open("charmender.jpg"))
img7 = ImageTk.PhotoImage(Image.open("lyvasour.jpg"))
img8 = ImageTk.PhotoImage(Image.open("kadabra.jpg"))
img9 = ImageTk.PhotoImage(Image.open("meowth.jpg"))
img10 = ImageTk.PhotoImage(Image.open("nidoking.jpg"))
img11 = ImageTk.PhotoImage(Image.open("paras.jpg"))
img12 = ImageTk.PhotoImage(Image.open("persion.jpg"))
img13 = ImageTk.PhotoImage(Image.open("pickachu.jpg"))
img14 = ImageTk.PhotoImage(Image.open("ratata.jpg"))


label1 = Label(window , text = "Player1")
label1.place(relx = 0.1 , rely = 0.3 , anchor = CENTER)


label2 = Label(window , text = "Player2")
label2.place(relx = 0.1 , rely = 0.3 , anchor = CENTER)


score1 = Label(window)
score1.place(relx = 0.1 , rely =0.4 , anchor = CENTER)


score2 = Label(window)
score2.place(relx = 0.9 , rely =0.4 , anchor = CENTER)


Cscore = Label(window)
Cscore.place(relx = 0.5 , rely =0.5 , anchor = CENTER)

list = [squirtle,abra,jigglypuff,bulbasour,charmender,lyvasour,kadabra,meowth,nidoking,paras.jpg,persion,pickachu,ratata]

power_list = [60,100,200,50,40,110,58,70,80,90,230,250,240]

score1 = 0
def player1():
    global score1
    random_no1 = random.randint(0,13)
    random_pok = list[random_no1]
    label["image"] = random_pok

    random_power = power_list[random_no1]
    score1 = score1 + random_power
    score1['text'] = str(player1)

player1_btn = Button(window , image = img5 )    
player1_btn.place(relx = 0.1 , rely = 0.6 , anchor=CENTER)

score2 = 0
def player2():
    global score2
    random_no2 = random.randint(0,13)
    random_pok = list[random_no2]
    label["image"] = random_pok

    random_power = power_list[random_no2]
    score2 = score2 + random_power
    score2['text'] = str(player1)

player2_btn = Button(window , image = img5 )    
player2_btn.place(relx = 0.9 , rely = 0.6 , anchor=CENTER)



window.mainloop()