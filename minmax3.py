from Puissance4_testcolonne import *
from random import *

#aaaa

def func_eval(A):
    A.test()
    nb_coups_R=A.nb_coup//2+A.nb_coup%2
    nb_coups_J=A.nb_coup//2
    if A.gJ==True:
        return 10**12
    if A.gR==True:
        return -10**12
    if A.nb_coup==49:
        return 0
    else:
        return 10*A.nb_3pions_ali_J_via()-10*A.nb_3pions_ali_R_via()+A.nb_2pions_ali_J_via()-A.nb_2pions_ali_R_via()

def MIN(a):
    l=[]
    for elem in a:
        l+=[elem[0]]
    m=min(l)
    ind=-1
    for i in range(len(a)):
        if a[i][0]==m:
            ind=i
    indice=a[ind][1]
    return m,indice

def MAX(a):
    l=[]
    for elem in a:
        l+=[elem[0]]
    m=max(l)
    ind=-1
    for i in range(len(a)):
        if a[i][0]==m:
            ind=i
    indice=a[ind][1]
    return m,indice

def minmax(A):
    l=[]
    for i in range(1,8):
        a=[]
        if A.c_remplie[i-1]==False:
            A.joue(i,A.joueur)
            for j in range(1,8):
                if A.c_remplie[j-1]==False:
                    A.joue(j,A.joueur)
                    a+=[(func_eval(A),i)]
                    #print(A)
                    A.undo()
            #print("a=",a)
            l+=[MIN(a)]
            A.undo()
    #print("l=",l)
    m=MAX(l)
    return (A.joue(m[1],A.joueur),m[1])


def jouer(self):
        for i in range(49):
            CR=input("rentrer la colonne ou on veut jouer")
            self.joue(CR,"R")
            self.test()
            if self.gR==True:
                break
            print(self)
            print("----------------------------------")

            minmax(self)
            self.test()
            if self.gJ==True:
                break
            print(self)
            print("----------------------------------")
        print("----------------------------------")
        print(self)
        if self.gR==True:
            print("Joueur rouge gagne")
        elif self.gJ==True:
            print("Joueur jaune gagne")
        else:
            print("Egalite")