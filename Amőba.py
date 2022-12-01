from tkinter import *
import random

def kovetkezo_fordulo(sor, oszlop):
    global jatekos

    if gombok[sor][oszlop]['text'] == "" and gyoztes() is False:
        if jatekos == jatekosok[0]:
            gombok[sor][oszlop]['text']=jatekos
            if gyoztes() is False:
                jatekos=jatekosok[1]
                szoveg.config(text=(jatekosok[1]+" játékos jön"))
            elif gyoztes() is True:
                szoveg.config(text=(jatekosok[0]+ " győztes"))
            elif gyoztes() == "Döntetlen":
                szoveg.config(text="Döntetlen!")
        else:
            gombok[sor][oszlop]['text'] = jatekos

            if gyoztes() is False:
                jatekos=jatekosok[0]
                szoveg.config(text=(jatekos[0]+ " következik"))
            elif gyoztes() is True:
                szoveg.config(text=(jatekosok[1]+" győztes"))
            elif gyoztes() == "Döntetlen":
                szoveg.config(text="Döntetlen")

def gyoztes():
    for sor in range(3):
        if gombok[sor][0]['text'] == gombok[sor][1]['text'] == gombok[sor][2]['text'] != "":
            gombok[sor][0].config(bg="green")
            gombok[sor][1].config(bg="green")
            gombok[sor][2].config(bg="green")
            return True

    for oszlop in range(3):
        if gombok[0][oszlop]['text'] == gombok[1][oszlop]['text'] == gombok[2][oszlop]['text'] != "":
            gombok[0][oszlop].config(bg="green")
            gombok[1][oszlop].config(bg="green")
            gombok[2][oszlop].config(bg="green")
            return True

    if gombok[0][0]['text'] == gombok[1][1]['text'] == gombok[2][2]['text'] != "":
        gombok[0][0].config(bg="green")
        gombok[1][1].config(bg="green")
        gombok[2][2].config(bg="green")
        return True

    elif gombok[0][2]['text'] == gombok[1][1]['text'] == gombok[2][0]['text'] != "":
        gombok[0][2].config(bg="green")
        gombok[1][1].config(bg="green")
        gombok[2][0].config(bg="green")
        return True
    elif ures_helyek() is False:

        for sor in range(3):
            for oszlop in range(3):
                gombok[sor][oszlop].config(bg="yellow")
        return "Döntetlen"

    else:
        return False

def ures_helyek():
    spaces = 9

    for sor in range(3):
        for oszlop in range(3):
            if gombok[sor][oszlop]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def uj_jatek():
    global jatekos
    jatekos = random.choice(jatekosok)
    szoveg.config(text=jatekos + " következik")
    for sor in range(3):
        for oszlop in range(3):
            gombok[sor][oszlop].config(text="", bg="#F0F0F0")


#játéktábla

window = Tk()
window.title("Amőba")
jatekosok=["x","o"]
jatekos=random.choice(jatekosok)
gombok=[[0,0,0],
        [0,0,0],
        [0,0,0]]

szoveg=Label(text=jatekos+" játékos jön", font=('consolas',40))
szoveg.pack(side="top")

reset_button = Button(text="restart", font=('consolas',20), command=uj_jatek)
reset_button.pack(side="top")

keret=Frame(window)
keret.pack()

for sor in range(3):
    for oszlop in range(3):
        gombok[sor][oszlop] = Button(keret,text="",font=('consolas',40),width=5, height=2, command=lambda sor=sor, oszlop=oszlop:kovetkezo_fordulo(sor,oszlop))
        gombok[sor][oszlop].grid(row=sor,column=oszlop)

window.mainloop()


