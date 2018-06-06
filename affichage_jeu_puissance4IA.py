# Créé par thomas, le 04/10/2016 en Python 3.2

from tkinter import *
from Puissance4_testcolonne import *
from minmax3 import *

fenetre=Tk()

Photo1=PhotoImage(file="pasdepion.gif")
Photo2=PhotoImage(file="pion_jaune.gif")
Photo3=PhotoImage(file="pion_rouge.gif")

A=Puissance4()
joueur="R"

canvas=Canvas(fenetre,width=490,height=490)
#creation des commandes
def jouer():
    bouton_jouer.destroy()

    bouton1.pack(side=LEFT,padx=27)
    bouton2.pack(side=LEFT ,padx=27)
    bouton3.pack(side=LEFT ,padx=27)
    bouton4.pack(side=LEFT ,padx=27)
    bouton5.pack(side=LEFT ,padx=27)
    bouton6.pack(side=LEFT ,padx=27)
    bouton7.pack(side=LEFT ,padx=27)


def detruire():
    fenetre.destroy()

def pion_col1(j):


    i=A.joue("1","R")
    A.test()

    if j=="R":
        photo=Photo3


    canvas.itemconfig(canvas.create_image(35,35+70*i,image=photo))
    if A.gR==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()
        bouton_gg=Button(fenetre,text="Bravo le joueur rouge a gagné",command=detruire)
        bouton_gg.pack()
    elif A.gJ==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur jaune a gagné",command=detruire)
        bouton_gg.pack()

    elif A.nb_coup==49:
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_eg.pack()
    elif A.c_remplie[0]==True:
        bouton1.config(state=DISABLED)

    (i,p)=minmax(A)
    A.test()
    photo=Photo2
    canvas.itemconfig(canvas.create_image(35+70*(p-1),35+70*i,image=photo))
    if A.gR==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur rouge a gagné",command=detruire)
        bouton_gg.pack()
    elif A.gJ==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur jaune a gagné",command=detruire)
        bouton_gg.pack()

    elif A.nb_coup==49:
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_eg.pack()
    elif A.c_remplie[0]==True:
        bouton1.config(state=DISABLED)
    elif A.c_remplie[1]==True:
        bouton2.config(state=DISABLED)
    elif A.c_remplie[2]==True:
        bouton3.config(state=DISABLED)
    elif A.c_remplie[3]==True:
        bouton4.config(state=DISABLED)
    elif A.c_remplie[4]==True:
        bouton5.config(state=DISABLED)
    elif A.c_remplie[5]==True:
        bouton6.config(state=DISABLED)
    elif A.c_remplie[6]==True:
        bouton7.config(state=DISABLED)




def pion_col2(j):


    i=A.joue("2","R")
    A.test()

    if j=="R":
        photo=Photo3


    canvas.itemconfig(canvas.create_image(35+70,35+70*i,image=photo))
    if A.gR==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur rouge a gagné",command=detruire)
        bouton_gg.pack()
    elif A.gJ==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur jaune a gagné",command=detruire)
        bouton_gg.pack()

    elif A.nb_coup==49:
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_eg.pack()
    elif A.c_remplie[1]==True:
        bouton2.config(state=DISABLED)

    (i,p)=minmax(A)
    A.test()
    photo=Photo2
    canvas.itemconfig(canvas.create_image(35+70*(p-1),35+70*i,image=photo))
    if A.gR==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur rouge a gagné",command=detruire)
        bouton_gg.pack()
    elif A.gJ==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur jaune a gagné",command=detruire)
        bouton_gg.pack()

    elif A.nb_coup==49:
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_eg.pack()
    elif A.c_remplie[0]==True:
        bouton1.config(state=DISABLED)
    elif A.c_remplie[1]==True:
        bouton2.config(state=DISABLED)
    elif A.c_remplie[2]==True:
        bouton3.config(state=DISABLED)
    elif A.c_remplie[3]==True:
        bouton4.config(state=DISABLED)
    elif A.c_remplie[4]==True:
        bouton5.config(state=DISABLED)
    elif A.c_remplie[5]==True:
        bouton6.config(state=DISABLED)
    elif A.c_remplie[6]==True:
        bouton7.config(state=DISABLED)

def pion_col3(j):


    i=A.joue("3","R")
    A.test()

    if j=="R":
        photo=Photo3


    canvas.itemconfig(canvas.create_image(35+70*2,35+70*i,image=photo))
    if A.gR==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur rouge a gagné",command=detruire)
        bouton_gg.pack()
    elif A.gJ==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur jaune a gagné",command=detruire)
        bouton_gg.pack()

    elif A.nb_coup==49:
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_eg.pack()
    elif A.c_remplie[1]==True:
        bouton2.config(state=DISABLED)

    (i,j)=minmax(A)
    A.test()
    photo=Photo2
    canvas.itemconfig(canvas.create_image(35+70*(j-1),35+70*i,image=photo))
    if A.gR==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur rouge a gagné",command=detruire)
        bouton_gg.pack()
    elif A.gJ==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur jaune a gagné",command=detruire)
        bouton_gg.pack()

    elif A.nb_coup==49:
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_eg.pack()
    elif A.c_remplie[0]==True:
        bouton1.config(state=DISABLED)
    elif A.c_remplie[1]==True:
        bouton2.config(state=DISABLED)
    elif A.c_remplie[2]==True:
        bouton3.config(state=DISABLED)
    elif A.c_remplie[3]==True:
        bouton4.config(state=DISABLED)
    elif A.c_remplie[4]==True:
        bouton5.config(state=DISABLED)
    elif A.c_remplie[5]==True:
        bouton6.config(state=DISABLED)
    elif A.c_remplie[6]==True:
        bouton7.config(state=DISABLED)

def pion_col4(j):
    i=A.joue("4","R")
    A.test()

    if j=="R":
        photo=Photo3


    canvas.itemconfig(canvas.create_image(35+70*3,35+70*i,image=photo))
    if A.gR==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur rouge a gagné",command=detruire)
        bouton_gg.pack()
    elif A.gJ==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur jaune a gagné",command=detruire)
        bouton_gg.pack()

    elif A.nb_coup==49:
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_eg.pack()
    elif A.c_remplie[0]==True:
        bouton1.config(state=DISABLED)

    (i,p)=minmax(A)
    A.test()
    photo=Photo2
    canvas.itemconfig(canvas.create_image(35+70*(p-1),35+70*i,image=photo))
    if A.gR==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur rouge a gagné",command=detruire)
        bouton_gg.pack()
    elif A.gJ==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur jaune a gagné",command=detruire)
        bouton_gg.pack()

    elif A.nb_coup==49:
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_eg.pack()
    elif A.c_remplie[0]==True:
        bouton1.config(state=DISABLED)
    elif A.c_remplie[1]==True:
        bouton2.config(state=DISABLED)
    elif A.c_remplie[2]==True:
        bouton3.config(state=DISABLED)
    elif A.c_remplie[3]==True:
        bouton4.config(state=DISABLED)
    elif A.c_remplie[4]==True:
        bouton5.config(state=DISABLED)
    elif A.c_remplie[5]==True:
        bouton6.config(state=DISABLED)
    elif A.c_remplie[6]==True:
        bouton7.config(state=DISABLED)
def pion_col5(j):
    i=A.joue("5","R")
    A.test()

    if j=="R":
        photo=Photo3


    canvas.itemconfig(canvas.create_image(35+70*4,35+70*i,image=photo))
    if A.gR==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur rouge a gagné",command=detruire)
        bouton_gg.pack()
    elif A.gJ==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur jaune a gagné",command=detruire)
        bouton_gg.pack()

    elif A.nb_coup==49:
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_eg.pack()
    elif A.c_remplie[0]==True:
        bouton1.config(state=DISABLED)

    (i,p)=minmax(A)
    A.test()
    photo=Photo2
    canvas.itemconfig(canvas.create_image(35+70*(p-1),35+70*i,image=photo))
    if A.gR==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur rouge a gagné",command=detruire)
        bouton_gg.pack()
    elif A.gJ==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur jaune a gagné",command=detruire)
        bouton_gg.pack()

    elif A.nb_coup==49:
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_eg.pack()
    elif A.c_remplie[0]==True:
        bouton1.config(state=DISABLED)
    elif A.c_remplie[1]==True:
        bouton2.config(state=DISABLED)
    elif A.c_remplie[2]==True:
        bouton3.config(state=DISABLED)
    elif A.c_remplie[3]==True:
        bouton4.config(state=DISABLED)
    elif A.c_remplie[4]==True:
        bouton5.config(state=DISABLED)
    elif A.c_remplie[5]==True:
        bouton6.config(state=DISABLED)
    elif A.c_remplie[6]==True:
        bouton7.config(state=DISABLED)

def pion_col6(j):
    i=A.joue("6","R")
    A.test()

    if j=="R":
        photo=Photo3


    canvas.itemconfig(canvas.create_image(35+70*5,35+70*i,image=photo))
    if A.gR==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur rouge a gagné",command=detruire)
        bouton_gg.pack()
    elif A.gJ==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur jaune a gagné",command=detruire)
        bouton_gg.pack()

    elif A.nb_coup==49:
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_eg.pack()
    elif A.c_remplie[0]==True:
        bouton1.config(state=DISABLED)

    (i,p)=minmax(A)
    A.test()
    photo=Photo2
    canvas.itemconfig(canvas.create_image(35+70*(p-1),35+70*i,image=photo))
    if A.gR==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur rouge a gagné",command=detruire)
        bouton_gg.pack()
    elif A.gJ==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur jaune a gagné",command=detruire)
        bouton_gg.pack()

    elif A.nb_coup==49:
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_eg.pack()
    elif A.c_remplie[0]==True:
        bouton1.config(state=DISABLED)
    elif A.c_remplie[1]==True:
        bouton2.config(state=DISABLED)
    elif A.c_remplie[2]==True:
        bouton3.config(state=DISABLED)
    elif A.c_remplie[3]==True:
        bouton4.config(state=DISABLED)
    elif A.c_remplie[4]==True:
        bouton5.config(state=DISABLED)
    elif A.c_remplie[5]==True:
        bouton6.config(state=DISABLED)
    elif A.c_remplie[6]==True:
        bouton7.config(state=DISABLED)
def pion_col7(j):
    i=A.joue("7","R")
    A.test()

    if j=="R":
        photo=Photo3


    canvas.itemconfig(canvas.create_image(35+70*6,35+70*i,image=photo))
    if A.gR==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur rouge a gagné",command=detruire)
        bouton_gg.pack()
    elif A.gJ==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur jaune a gagné",command=detruire)
        bouton_gg.pack()

    elif A.nb_coup==49:
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_eg.pack()
    elif A.c_remplie[0]==True:
        bouton1.config(state=DISABLED)

    (i,p)=minmax(A)
    A.test()
    photo=Photo2
    canvas.itemconfig(canvas.create_image(35+70*(p-1),35+70*i,image=photo))
    if A.gR==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur rouge a gagné",command=detruire)
        bouton_gg.pack()
    elif A.gJ==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_gg=Button(fenetre,text="Bravo le joueur jaune a gagné",command=detruire)
        bouton_gg.pack()

    elif A.nb_coup==49:
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()

        bouton_eg.pack()
    elif A.c_remplie[0]==True:
        bouton1.config(state=DISABLED)
    elif A.c_remplie[1]==True:
        bouton2.config(state=DISABLED)
    elif A.c_remplie[2]==True:
        bouton3.config(state=DISABLED)
    elif A.c_remplie[3]==True:
        bouton4.config(state=DISABLED)
    elif A.c_remplie[4]==True:
        bouton5.config(state=DISABLED)
    elif A.c_remplie[5]==True:
        bouton6.config(state=DISABLED)
    elif A.c_remplie[6]==True:
        bouton7.config(state=DISABLED)

#creation grille
for i in range(7):
    for j in range(7):

        image1=canvas.create_image(35+70*i,35+70*j,image=Photo1)

canvas.pack()
#creation dse boutons
bouton_jouer=Button(fenetre,text="Appuyer pour jouer",command=jouer)
bouton_jouer.pack()

bouton1=Button(fenetre,text="1",command= lambda : pion_col1(joueur))
bouton2=Button(fenetre,text="2",command=lambda : pion_col2(joueur))
bouton3=Button(fenetre,text="3",command=lambda : pion_col3(joueur))
bouton4=Button(fenetre,text="4",command=lambda : pion_col4(joueur))
bouton5=Button(fenetre,text="5",command=lambda : pion_col5(joueur))
bouton6=Button(fenetre,text="6",command=lambda : pion_col6(joueur))
bouton7=Button(fenetre,text="7",command=lambda : pion_col7(joueur))

bouton_eg=Button(fenetre,text="Partie nulle",command=detruire)
fenetre.mainloop()


