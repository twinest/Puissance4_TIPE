# Créé par thomas, le 04/10/2016 en Python 3.2
#b
from tkinter import *
from Puissance4_testcolonne import *
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
    bouton_undo.pack(side=BOTTOM,pady=5)
    bouton1.pack(side=LEFT,padx=27)
    bouton2.pack(side=LEFT ,padx=27)
    bouton3.pack(side=LEFT ,padx=27)
    bouton4.pack(side=LEFT ,padx=27)
    bouton5.pack(side=LEFT ,padx=27)
    bouton6.pack(side=LEFT ,padx=27)
    bouton7.pack(side=LEFT ,padx=27)
    bouton_undo.config(state=DISABLED)

def detruire():
    fenetre.destroy()

def pion_col1(j):
    bouton_undo.config(state=ACTIVE)

    i=A.joue("1",j)
    A.test()
    global joueur
    if j=="R":
        photo=Photo3
        joueur="J"
    else:
        photo=Photo2
        joueur="R"
    canvas.itemconfig(canvas.create_image(35,35+70*i,image=photo))
    if A.gR==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()
        bouton_undo.destroy()
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
        bouton_undo.destroy()
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
        bouton_undo.destroy()
        bouton_eg.pack()
    elif A.c_remplie[0]==True:
        bouton1.config(state=DISABLED)


def pion_col2(j):
    bouton_undo.config(state=ACTIVE)

    i=A.joue("2",j)
    global joueur
    if j=="R":
        photo=Photo3
        joueur="J"
    else:
        photo=Photo2
        joueur="R"
    canvas.itemconfig(canvas.create_image(35+70,35+70*i,image=photo))
    A.test()
    if A.gR==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()
        bouton_undo.destroy()
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
        bouton_undo.destroy()
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
        bouton_undo.destroy()
        bouton_eg.pack()
    elif A.c_remplie[1]==True:
        bouton2.config(state=DISABLED)

def pion_col3(j):
    bouton_undo.config(state=ACTIVE)

    i=A.joue("3",j)
    global joueur

    if j=="R":
        photo=Photo3
        joueur="J"
    else:
        photo=Photo2
        joueur="R"
    canvas.itemconfig(canvas.create_image(35+70*2,35+70*i,image=photo))
    A.test()
    if A.gR==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()
        bouton_undo.destroy()
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
        bouton_undo.destroy()
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
        bouton_undo.destroy()
        bouton_eg.pack()
    elif A.c_remplie[2]==True:
        bouton3.config(state=DISABLED)

def pion_col4(j):
    bouton_undo.config(state=ACTIVE)

    i=A.joue("4",j)
    global joueur
    if j=="R":
        photo=Photo3
        joueur="J"
    else:
        photo=Photo2
        joueur="R"
    canvas.itemconfig(canvas.create_image(35+70*3,35+70*i,image=photo))
    A.test()
    if A.gR==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()
        bouton_undo.destroy()
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
        bouton_undo.destroy()
        bouton_gg=Button(fenetre,text="Bravo le joueur jaune a gagné",command=detruire)
        bouton_gg.pack()
        bouton_undo.destroy()
    elif A.nb_coup==49:
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()
        bouton_undo.destroy()
        bouton_eg.pack()
    elif A.c_remplie[3]==True:
        bouton4.config(state=DISABLED)

def pion_col5(j):
    bouton_undo.config(state=ACTIVE)

    i=A.joue("5",j)
    global joueur
    if j=="R":
        photo=Photo3
        joueur="J"
    else:
        photo=Photo2
        joueur="R"
    canvas.itemconfig(canvas.create_image(35+70*4,35+70*i,image=photo))
    A.test()
    if A.gR==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()
        bouton_undo.destroy()
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
        bouton_undo.destroy()
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
        bouton_undo.destroy()
        bouton_eg.pack()
    elif A.c_remplie[4]==True:
        bouton5.config(state=DISABLED)

def pion_col6(j):
    bouton_undo.config(state=ACTIVE)

    i=A.joue("6",j)
    global joueur
    if j=="R":
        photo=Photo3
        joueur="J"
    else:
        photo=Photo2
        joueur="R"
    canvas.itemconfig(canvas.create_image(35+70*5,35+70*i,image=photo))
    A.test()
    if A.gR==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()
        bouton_undo.destroy()
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
        bouton_undo.destroy()
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
        bouton_undo.destroy()
        bouton_eg.pack()
    elif A.c_remplie[5]==True:
        bouton6.config(state=DISABLED)

def pion_col7(j):
    bouton_undo.config(state=ACTIVE)

    i=A.joue("7",j)
    global joueur
    if j=="R":
        photo=Photo3
        joueur="J"
    else:
        photo=Photo2
        joueur="R"
    canvas.itemconfig(canvas.create_image(35+70*6,35+70*i,image=photo))
    A.test()
    if A.gR==True :
        bouton1.destroy()
        bouton2.destroy()
        bouton3.destroy()
        bouton4.destroy()
        bouton5.destroy()
        bouton6.destroy()
        bouton7.destroy()
        bouton_undo.destroy()
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
        bouton_undo.destroy()
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
        bouton_undo.destroy()
        bouton_eg.pack()
    elif A.c_remplie[6]==True:
        bouton7.config(state=DISABLED)
def annule():
    global joueur
    cood=A.memoire[-1]
    if A.c_remplie[cood[0]]==True:
        if cood[0]==0:
            bouton1.config(state=ACTIVE)
        if cood[0]==1:
            bouton2.config(state=ACTIVE)
        if cood[0]==2:
            bouton3.config(state=ACTIVE)
        if cood[0]==3:
            bouton4.config(state=ACTIVE)
        if cood[0]==4:
            bouton5.config(state=ACTIVE)
        if cood[0]==5:
            bouton6.config(state=ACTIVE)
        if cood[0]==6:
            bouton7.config(state=ACTIVE)
    A.undo()
    canvas.itemconfig(canvas.create_image(35+70*cood[0],35+70*cood[1],image=Photo1))
    if joueur=="J":
        joueur="R"
    elif joueur=="R":
        joueur="J"
    if A.memoire==[]:
        bouton_undo.config(state=DISABLED)

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
bouton_undo=Button(fenetre,text="annuler le coup précedent",command=annule)
bouton_eg=Button(fenetre,text="Partie nulle",command=detruire)
fenetre.mainloop()


