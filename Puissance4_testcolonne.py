import numpy as np
from minmax3 import *

def inverser_ch(a):
    ch=""
    for i in range(1,len(a)+1):
        ch+=a[-i]
    return ch

class Puissance4(object):
    def __init__(self):
        self.jeu=np.array([["." for i in range(7)] for j in range(7)])
        #self.cases_restantes=[(i,j) for i in range(7) for j in range(7)]
        self.gR=False
        self.gJ=False
        self.c_remplie=[False for i in range(7)]
        self.nb_coup=0
        self.memoire=[]
        self.joueur="R"
    def __repr__(self):
        return str(np.transpose(self.jeu))

    def joue(self,col,joueur):#col=colonne
        self.nb_coup+=1
        if self.joueur=="R":
            self.joueur="J"
        else:
            self.joueur="R"

        if self.jeu[int(col)-1][0]=="." and self.jeu[int(col)-1][1]!=".":
                self.c_remplie[int(col)-1]=True
                if joueur =="R":
                    self.jeu[int(col)-1][0]="R"

                else:
                    self.jeu[int(col)-1][0]="J"
                self.memoire+=[(int(col)-1,0)]
                return 0
        if self.jeu[int(col)-1][1]=="." and self.jeu[int(col)-1][2]!=".":
                if joueur =="R":
                   self.jeu[int(col)-1][1]="R"
                else:
                    self.jeu[int(col)-1][1]="J"
                self.memoire+=[(int(col)-1,1)]
                return 1
        if self.jeu[int(col)-1][2]=="." and self.jeu[int(col)-1][3]!=".":
                if joueur =="R":
                    self.jeu[int(col)-1][2]="R"
                else:
                    self.jeu[int(col)-1][2]="J"
                self.memoire+=[(int(col)-1,2)]
                return 2
        if self.jeu[int(col)-1][3]=="." and self.jeu[int(col)-1][4]!=".":
                if joueur =="R":
                    self.jeu[int(col)-1][3]="R"
                else:
                    self.jeu[int(col)-1][3]="J"
                self.memoire+=[(int(col)-1,3)]
                return 3
        if self.jeu[int(col)-1][4]=="." and self.jeu[int(col)-1][5]!=".":
                if joueur =="R":
                    self.jeu[int(col)-1][4]="R"
                else:
                    self.jeu[int(col)-1][4]="J"
                self.memoire+=[(int(col)-1,4)]
                return 4
        if self.jeu[int(col)-1][5]=="." and self.jeu[int(col)-1][6]!=".":
                if joueur =="R":
                    self.jeu[int(col)-1][5]="R"
                else:
                    self.jeu[int(col)-1][5]="J"
                self.memoire+=[(int(col)-1,5)]
                return 5
        if self.jeu[int(col)-1][6]==".":

                if joueur =="R":
                    self.jeu[int(col)-1][6]="R"
                else:
                    self.jeu[int(col)-1][6]="J"
                self.memoire+=[(int(col)-1,6)]
                return 6

    def undo(self):
        if self.joueur=="R":
            self.joueur="J"
        else :
            self.joueur="R"
        cood=self.memoire.pop()
        self.jeu[cood]='.'
        if self.c_remplie[cood[0]]==True:
            self.c_remplie[cood[0]]=False
        if self.gJ==True:
            self.gJ=False
        if self.gR==True:
            self.gR=False
        self.nb_coup-=1

    def test(self):
        A=self.jeu
        B=np.transpose(A)
        c0,c1,c2="","",""
        c3,c4,c5="","",""
        c6=""
        l0,l1,l2="","",""
        l3=""
        l4,l5,l6="","",""

        for i in range(7):
            c0+=str(A[0,i])
            c1+=str(A[1,i])
            c2+=str(A[2,i])
            c3+=str(A[3,i])
            c4+=str(A[4,i])
            c5+=str(A[5,i])
            c6+=str(A[6,i])

            l0+=str(B[0,i])
            l1+=str(B[1,i])
            l2+=str(B[2,i])
            l3+=str(B[3,i])
            l4+=str(B[4,i])
            l5+=str(B[5,i])
            l6+=str(B[6,i])

        d0=str(A[0,3])+str(A[1,4])+str(A[2,5])+str(A[3,6])
        d1=str(A[0,2])+str(A[1,3])+str(A[2,4])+str(A[3,5])+str(A[4,6])
        d2=str(A[0,1])+str(A[1,2])+str(A[2,3])+str(A[3,4])+str(A[4,5])+str(A[5,6])
        d3=str(A[0,0])+str(A[1,1])+str(A[2,2])+str(A[3,3])+str(A[4,4])+str(A[5,5])+str(A[6,6])
        d4=str(A[1,0])+str(A[2,1])+str(A[3,2])+str(A[4,3])+str(A[5,4])+str(A[6,5])
        d5=str(A[2,0])+str(A[3,1])+str(A[4,2])+str(A[5,3])+str(A[6,4])
        d6=str(A[3,0])+str(A[4,1])+str(A[5,2])+str(A[6,3])
        d7=str(A[0,3])+str(A[1,2])+str(A[2,1])+str(A[3,0])
        d8=str(A[0,4])+str(A[1,3])+str(A[2,2])+str(A[3,1])+str(A[4,0])
        d9=str(A[0,5])+str(A[1,4])+str(A[2,3])+str(A[3,2])+str(A[4,1])+str(A[5,0])
        d10=str(A[0,6])+str(A[1,5])+str(A[2,4])+str(A[3,3])+str(A[4,2])+str(A[5,1])+str(A[6,0])
        d11=str(A[1,6])+str(A[2,5])+str(A[3,4])+str(A[4,3])+str(A[5,2])+str(A[6,1])
        d12=str(A[2,6])+str(A[3,5])+str(A[4,4])+str(A[5,3])+str(A[6,2])
        d13=str(A[3,6])+str(A[4,5])+str(A[5,4])+str(A[6,3])


        if "RRRR" in l0 or "RRRR" in l1 or "RRRR" in l2 or "RRRR" in l3 or "RRRR" in l4 or "RRRR"in l5 or "RRRR" in l6 or "RRRR" in c0 or"RRRR" in c1 or "RRRR" in c2 or "RRRR"in c3 or "RRRR" in c4 or "RRRR" in c5 or "RRRR" in c6 or "RRRR" in d0 or "RRRR" in d1 or "RRRR" in d2 or "RRRR" in d3 or "RRRR" in d4 or "RRRR" in d5 or "RRRR" in d6 or "RRRR" in d7 or "RRRR" in d8 or "RRRR" in d9 or "RRRR" in d10 or "RRRR" in d11 or "RRRR" in d12 or "RRRR" in d13:
            self.gR=True
        if "JJJJ" in l0 or "JJJJ" in l1 or "JJJJ" in l2 or "JJJJ" in l3 or "JJJJ" in l4 or "JJJJ" in l5 or "JJJJ" in l6 or "JJJJ"in c0 or "JJJJ" in c1 or "JJJJ" in c2 or "JJJJ" in c3 or "JJJJ" in c4 or "JJJJ" in c5 or "JJJJ" in c6 or "JJJJ" in d0 or "JJJJ" in d1 or "JJJJ" in d2 or "JJJJ" in d3 or "JJJJ" in d4 or "JJJJ" in d5 or "JJJJ" in d6 or "JJJJ" in d7 or "JJJJ" in d8 or "JJJJ" in d9 or "JJJJ" in d10 or "JJJJ" in d11 or "JJJJ" in d12 or "JJJJ" in d13:
            self.gJ=True


    def jouer(self):
        for i in range(49):
            CR=input("rentrer la colonne ou on veut jouer")
            self.joue(CR,"R")
            self.test()
            if self.gR==True:
                break
            print(self)
            print("----------------------------------")
            CJ=input("rentre la colonne ou on veut jouer")
            self.joue(CJ,"J")
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

    def nb_3pions_ali_R_via(self):
        A=self.jeu
        B=np.transpose(A)
        nb=0

        c0,c1,c2="","",""
        c3,c4,c5="","",""
        c6=""
        l0,l1,l2="","",""
        l3=""
        l4,l5,l6="","",""

        for i in range(7):
            c0+=str(A[0,i])
            c1+=str(A[1,i])
            c2+=str(A[2,i])
            c3+=str(A[3,i])
            c4+=str(A[4,i])
            c5+=str(A[5,i])
            c6+=str(A[6,i])

            l0+=str(B[0,i])
            l1+=str(B[1,i])
            l2+=str(B[2,i])
            l3+=str(B[3,i])
            l4+=str(B[4,i])
            l5+=str(B[5,i])
            l6+=str(B[6,i])

        d0=str(A[0,3])+str(A[1,4])+str(A[2,5])+str(A[3,6])
        d1=str(A[0,2])+str(A[1,3])+str(A[2,4])+str(A[3,5])+str(A[4,6])
        d2=str(A[0,1])+str(A[1,2])+str(A[2,3])+str(A[3,4])+str(A[4,5])+str(A[5,6])
        d3=str(A[0,0])+str(A[1,1])+str(A[2,2])+str(A[3,3])+str(A[4,4])+str(A[5,5])+str(A[6,6])
        d4=str(A[1,0])+str(A[2,1])+str(A[3,2])+str(A[4,3])+str(A[5,4])+str(A[6,5])
        d5=str(A[2,0])+str(A[3,1])+str(A[4,2])+str(A[5,3])+str(A[6,4])
        d6=str(A[3,0])+str(A[4,1])+str(A[5,2])+str(A[6,3])
        d7=str(A[0,3])+str(A[1,2])+str(A[2,1])+str(A[3,0])
        d8=str(A[0,4])+str(A[1,3])+str(A[2,2])+str(A[3,1])+str(A[4,0])
        d9=str(A[0,5])+str(A[1,4])+str(A[2,3])+str(A[3,2])+str(A[4,1])+str(A[5,0])
        d10=str(A[0,6])+str(A[1,5])+str(A[2,4])+str(A[3,3])+str(A[4,2])+str(A[5,1])+str(A[6,0])
        d11=str(A[1,6])+str(A[2,5])+str(A[3,4])+str(A[4,3])+str(A[5,2])+str(A[6,1])
        d12=str(A[2,6])+str(A[3,5])+str(A[4,4])+str(A[5,3])+str(A[6,2])
        d13=str(A[3,6])+str(A[4,5])+str(A[5,4])+str(A[6,3])

        C0=inverser_ch(c0)
        C1=inverser_ch(c1)
        C2=inverser_ch(c2)
        C3=inverser_ch(c3)
        C4=inverser_ch(c4)
        C5=inverser_ch(c5)
        C6=inverser_ch(c6)
        L0=l0
        L1=l1
        L2=l2
        L3=l3
        L4=l4
        L5=l5
        L6=l6
        D0=inverser_ch(d0)
        D1=inverser_ch(d1)
        D2=inverser_ch(d2)
        D3=inverser_ch(d3)
        D4=inverser_ch(d4)
        D5=inverser_ch(d5)
        D6=inverser_ch(d6)
        D7=d7
        D8=d8
        D9=d9
        D10=d10
        D11=d11
        D12=d12
        D13=d13

        if "RRR." in C0:
            nb+=1

        if "RRR." in C1:
            nb+=1

        if "RRR." in C2:
            nb+=1

        if "RRR." in C3:
            nb+=1

        if "RRR." in C4:
            nb+=1

        if "RRR." in C5:
            nb+=1

        if "RRR." in C6:
            nb+=1

        if "RRR." in L0:
            if ".RRR." in L0:
                nb+=2
            else :nb+=1

        if "RRR." in L1:
            if ".RRR." in L1:
                nb+=2
            else :nb+=1

        if "RRR." in L2:
            if ".RRR." in L2:
                nb+=2
            else :nb+=1

        if "RRR." in L3:
            if ".RRR." in L3:
                nb+=2
            else :nb+=1

        if "RRR." in L4:
            if ".RRR." in L4:
                nb+=2
            else :nb+=1

        if "RRR." in L5:
            if ".RRR." in L5:
                nb+=2
            else :nb+=1

        if "RRR." in L6:
            if ".RRR." in L6:
                nb+=2
            else :nb+=1

        if "RRR." in D0:
            if ".RRR." in D0:
                nb+=2
            else :nb+=1

        if "RRR." in D1:
            if ".RRR." in D1:
                nb+=2
            else :nb+=1

        if "RRR." in D2:
            if ".RRR." in D2:
                nb+=2
            else :nb+=1

        if "RRR." in D3:
            if ".RRR." in D3:
                nb+=2
            else :nb+=1

        if "RRR." in D4:
            if ".RRR." in D4:
                nb+=2
            else :nb+=1

        if "RRR." in D5:
            if ".RRR." in D5:
                nb+=2
            else :nb+=1

        if "RRR." in D6:
            if ".RRR." in D6:
                nb+=2
            else :nb+=1

        if "RRR." in D7:
            if ".RRR." in D7:
                nb+=2
            else :nb+=1

        if "RRR." in D8:
            if ".RRR." in D8:
                nb+=2
            else :nb+=1

        if "RRR." in D9:
            if ".RRR." in D9:
                nb+=2
            else :nb+=1

        if "RRR." in D10:
            if ".RRR." in D10:
                nb+=2
            else :nb+=1

        if "RRR." in D11:
            if ".RRR." in D11:
                nb+=2
            else :nb+=1

        if "RRR." in D12:
            if ".RRR." in D12:
                nb+=2
            else :nb+=1

        if "RRR." in D13:
            if ".RRR." in D13:
                nb+=2
            else :nb+=1

        if "RR.R" in L0:
            nb+=1
        if "RR.R" in L1:
            nb+=1
        if "RR.R" in L2:
            nb+=1
        if "RR.R" in L3:
            nb+=1
        if "RR.R" in L4:
            nb+=1
        if "RR.R" in L5:
            nb+=1
        if "RR.R" in L6:
            nb+=1
        if "R.RR" in L0:
            nb+=1
        if "R.RR" in L1:
            nb+=1
        if "R.RR" in L2:
            nb+=1
        if "R.RR" in L3:
            nb+=1
        if "R.RR" in L4:
            nb+=1
        if "R.RR" in L5:
            nb+=1
        if "R.RR" in L6:
            nb+=1
        if "RR.R" in D0:
            nb+=1
        if "RR.R" in D1:
            nb+=1
        if "RR.R" in D2:
            nb+=1
        if "RR.R" in D3:
            nb+=1
        if "RR.R" in D4:
            nb+=1
        if "RR.R" in D5:
            nb+=1
        if "RR.R" in D6:
            nb+=1
        if "RR.R" in D7:
            nb+=1
        if "RR.R" in D8:
            nb+=1
        if "RR.R" in D9:
            nb+=1
        if "RR.R" in D10:
            nb+=1
        if "RR.R" in D11:
            nb+=1
        if "RR.R" in D12:
            nb+=1
        if "RR.R" in D13:
            nb+=1
        if "R.RR" in D0:
            nb+=1
        if "R.RR" in D1:
            nb+=1
        if "R.RR" in D2:
            nb+=1
        if "R.RR" in D3:
            nb+=1
        if "R.RR" in D4:
            nb+=1
        if "R.RR" in D5:
            nb+=1
        if "R.RR" in D6:
            nb+=1
        if "R.RR" in D7:
            nb+=1
        if "R.RR" in D8:
            nb+=1
        if "R.RR" in D9:
            nb+=1
        if "R.RR" in D10:
            nb+=1
        if "R.RR" in D11:
            nb+=1
        if "R.RR" in D12:
            nb+=1
        if "R.RR" in D13:
            nb+=1
        return nb

    def nb_3pions_ali_J_via(self):
        A=self.jeu
        B=np.transpose(A)
        nb=0

        c0,c1,c2="","",""
        c3,c4,c5="","",""
        c6=""
        l0,l1,l2="","",""
        l3=""
        l4,l5,l6="","",""

        for i in range(7):
            c0+=str(A[0,i])
            c1+=str(A[1,i])
            c2+=str(A[2,i])
            c3+=str(A[3,i])
            c4+=str(A[4,i])
            c5+=str(A[5,i])
            c6+=str(A[6,i])

            l0+=str(B[0,i])
            l1+=str(B[1,i])
            l2+=str(B[2,i])
            l3+=str(B[3,i])
            l4+=str(B[4,i])
            l5+=str(B[5,i])
            l6+=str(B[6,i])

        d0=str(A[0,3])+str(A[1,4])+str(A[2,5])+str(A[3,6])
        d1=str(A[0,2])+str(A[1,3])+str(A[2,4])+str(A[3,5])+str(A[4,6])
        d2=str(A[0,1])+str(A[1,2])+str(A[2,3])+str(A[3,4])+str(A[4,5])+str(A[5,6])
        d3=str(A[0,0])+str(A[1,1])+str(A[2,2])+str(A[3,3])+str(A[4,4])+str(A[5,5])+str(A[6,6])
        d4=str(A[1,0])+str(A[2,1])+str(A[3,2])+str(A[4,3])+str(A[5,4])+str(A[6,5])
        d5=str(A[2,0])+str(A[3,1])+str(A[4,2])+str(A[5,3])+str(A[6,4])
        d6=str(A[3,0])+str(A[4,1])+str(A[5,2])+str(A[6,3])
        d7=str(A[0,3])+str(A[1,2])+str(A[2,1])+str(A[3,0])
        d8=str(A[0,4])+str(A[1,3])+str(A[2,2])+str(A[3,1])+str(A[4,0])
        d9=str(A[0,5])+str(A[1,4])+str(A[2,3])+str(A[3,2])+str(A[4,1])+str(A[5,0])
        d10=str(A[0,6])+str(A[1,5])+str(A[2,4])+str(A[3,3])+str(A[4,2])+str(A[5,1])+str(A[6,0])
        d11=str(A[1,6])+str(A[2,5])+str(A[3,4])+str(A[4,3])+str(A[5,2])+str(A[6,1])
        d12=str(A[2,6])+str(A[3,5])+str(A[4,4])+str(A[5,3])+str(A[6,2])
        d13=str(A[3,6])+str(A[4,5])+str(A[5,4])+str(A[6,3])

        C0=inverser_ch(c0)
        C1=inverser_ch(c1)
        C2=inverser_ch(c2)
        C3=inverser_ch(c3)
        C4=inverser_ch(c4)
        C5=inverser_ch(c5)
        C6=inverser_ch(c6)
        L0=l0
        L1=l1
        L2=l2
        L3=l3
        L4=l4
        L5=l5
        L6=l6
        D0=inverser_ch(d0)
        D1=inverser_ch(d1)
        D2=inverser_ch(d2)
        D3=inverser_ch(d3)
        D4=inverser_ch(d4)
        D5=inverser_ch(d5)
        D6=inverser_ch(d6)
        D7=d7
        D8=d8
        D9=d9
        D10=d10
        D11=d11
        D12=d12
        D13=d13

        if "JJJ." in C0:
            nb+=1

        if "JJJ." in C1:
            nb+=1

        if "JJJ." in C2:
            nb+=1

        if "JJJ." in C3:
            nb+=1

        if "JJJ." in C4:
            nb+=1

        if "JJJ." in C5:
            nb+=1

        if "JJJ." in C6:
            nb+=1

        if "JJJ." in L0:
            if ".JJJ." in L0:
                nb+=2
            else :nb+=1

        if "JJJ." in L1:
            if ".JJJ." in L1:
                nb+=2
            else :nb+=1

        if "JJJ." in L2:
            if ".JJJ." in L2:
                nb+=2
            else :nb+=1

        if "JJJ." in L3:
            if ".JJJ." in L3:
                nb+=2
            else :nb+=1

        if "JJJ." in L4:
            if ".JJJ." in L4:
                nb+=2
            else :nb+=1

        if "JJJ." in L5:
            if ".JJJ." in L5:
                nb+=2
            else :nb+=1

        if "JJJ." in L6:
            if ".JJJ." in L6:
                nb+=2
            else :nb+=1

        if "JJJ." in D0:
            if ".JJJ." in D0:
                nb+=2
            else :nb+=1

        if "JJJ." in D1:
            if ".JJJ." in D1:
                nb+=2
            else :nb+=1

        if "JJJ." in D2:
            if ".JJJ." in D2:
                nb+=2
            else :nb+=1

        if "JJJ." in D3:
            if ".JJJ." in D3:
                nb+=2
            else :nb+=1

        if "JJJ." in D4:
            if ".JJJ." in D4:
                nb+=2
            else :nb+=1

        if "JJJ." in D5:
            if ".JJJ." in D5:
                nb+=2
            else :nb+=1

        if "JJJ." in D6:
            if ".JJJ." in D6:
                nb+=2
            else :nb+=1

        if "JJJ." in D7:
            if ".JJJ." in D7:
                nb+=2
            else :nb+=1

        if "JJJ." in D8:
            if ".JJJ." in D8:
                nb+=2
            else :nb+=1

        if "JJJ." in D9:
            if ".JJJ." in D9:
                nb+=2
            else :nb+=1

        if "JJJ." in D10:
            if ".JJJ." in D10:
                nb+=2
            else :nb+=1

        if "JJJ." in D11:
            if ".JJJ." in D11:
                nb+=2
            else :nb+=1

        if "JJJ." in D12:
            if ".JJJ." in D12:
                nb+=2
            else :nb+=1

        if "JJJ." in D13:
            if ".JJJ." in D13:
                nb+=2
            else :nb+=1

        if "JJ.J" in L0:
            nb+=1
        if "JJ.J" in L1:
            nb+=1
        if "JJ.J" in L2:
            nb+=1
        if "JJ.J" in L3:
            nb+=1
        if "JJ.J" in L4:
            nb+=1
        if "JJ.J" in L5:
            nb+=1
        if "JJ.J" in L6:
            nb+=1
        if "J.JJ" in L0:
            nb+=1
        if "J.JJ" in L1:
            nb+=1
        if "J.JJ" in L2:
            nb+=1
        if "J.JJ" in L3:
            nb+=1
        if "J.JJ" in L4:
            nb+=1
        if "J.JJ" in L5:
            nb+=1
        if "J.JJ" in L6:
            nb+=1
        if "JJ.J" in D0:
            nb+=1
        if "JJ.J" in D1:
            nb+=1
        if "JJ.J" in D2:
            nb+=1
        if "JJ.J" in D3:
            nb+=1
        if "JJ.J" in D4:
            nb+=1
        if "JJ.J" in D5:
            nb+=1
        if "JJ.J" in D6:
            nb+=1
        if "JJ.J" in D7:
            nb+=1
        if "JJ.J" in D8:
            nb+=1
        if "JJ.J" in D9:
            nb+=1
        if "JJ.J" in D10:
            nb+=1
        if "JJ.J" in D11:
            nb+=1
        if "JJ.J" in D12:
            nb+=1
        if "JJ.J" in D13:
            nb+=1
        if "J.JJ" in D0:
            nb+=1
        if "J.JJ" in D1:
            nb+=1
        if "J.JJ" in D2:
            nb+=1
        if "J.JJ" in D3:
            nb+=1
        if "J.JJ" in D4:
            nb+=1
        if "J.JJ" in D5:
            nb+=1
        if "J.JJ" in D6:
            nb+=1
        if "J.JJ" in D7:
            nb+=1
        if "J.JJ" in D8:
            nb+=1
        if "J.JJ" in D9:
            nb+=1
        if "J.JJ" in D10:
            nb+=1
        if "J.JJ" in D11:
            nb+=1
        if "J.JJ" in D12:
            nb+=1
        if "J.JJ" in D13:
            nb+=1
        return nb

    def nb_2pions_ali_R_via(self):
        A=self.jeu
        B=np.transpose(A)
        nb=0

        c0,c1,c2="","",""
        c3,c4,c5="","",""
        c6=""
        l0,l1,l2="","",""
        l3=""
        l4,l5,l6="","",""

        for i in range(7):
            c0+=str(A[0,i])
            c1+=str(A[1,i])
            c2+=str(A[2,i])
            c3+=str(A[3,i])
            c4+=str(A[4,i])
            c5+=str(A[5,i])
            c6+=str(A[6,i])

            l0+=str(B[0,i])
            l1+=str(B[1,i])
            l2+=str(B[2,i])
            l3+=str(B[3,i])
            l4+=str(B[4,i])
            l5+=str(B[5,i])
            l6+=str(B[6,i])

        d0=str(A[0,3])+str(A[1,4])+str(A[2,5])+str(A[3,6])
        d1=str(A[0,2])+str(A[1,3])+str(A[2,4])+str(A[3,5])+str(A[4,6])
        d2=str(A[0,1])+str(A[1,2])+str(A[2,3])+str(A[3,4])+str(A[4,5])+str(A[5,6])
        d3=str(A[0,0])+str(A[1,1])+str(A[2,2])+str(A[3,3])+str(A[4,4])+str(A[5,5])+str(A[6,6])
        d4=str(A[1,0])+str(A[2,1])+str(A[3,2])+str(A[4,3])+str(A[5,4])+str(A[6,5])
        d5=str(A[2,0])+str(A[3,1])+str(A[4,2])+str(A[5,3])+str(A[6,4])
        d6=str(A[3,0])+str(A[4,1])+str(A[5,2])+str(A[6,3])
        d7=str(A[0,3])+str(A[1,2])+str(A[2,1])+str(A[3,0])
        d8=str(A[0,4])+str(A[1,3])+str(A[2,2])+str(A[3,1])+str(A[4,0])
        d9=str(A[0,5])+str(A[1,4])+str(A[2,3])+str(A[3,2])+str(A[4,1])+str(A[5,0])
        d10=str(A[0,6])+str(A[1,5])+str(A[2,4])+str(A[3,3])+str(A[4,2])+str(A[5,1])+str(A[6,0])
        d11=str(A[1,6])+str(A[2,5])+str(A[3,4])+str(A[4,3])+str(A[5,2])+str(A[6,1])
        d12=str(A[2,6])+str(A[3,5])+str(A[4,4])+str(A[5,3])+str(A[6,2])
        d13=str(A[3,6])+str(A[4,5])+str(A[5,4])+str(A[6,3])

        C0=inverser_ch(c0)
        C1=inverser_ch(c1)
        C2=inverser_ch(c2)
        C3=inverser_ch(c3)
        C4=inverser_ch(c4)
        C5=inverser_ch(c5)
        C6=inverser_ch(c6)
        L0=l0
        L1=l1
        L2=l2
        L3=l3
        L4=l4
        L5=l5
        L6=l6
        D0=inverser_ch(d0)
        D1=inverser_ch(d1)
        D2=inverser_ch(d2)
        D3=inverser_ch(d3)
        D4=inverser_ch(d4)
        D5=inverser_ch(d5)
        D6=inverser_ch(d6)
        D7=d7
        D8=d8
        D9=d9
        D10=d10
        D11=d11
        D12=d12
        D13=d13

        if "RR." in C0:
            nb+=1

        if "RR." in C1:
            nb+=1

        if "RR." in C2:
            nb+=1

        if "RR." in C3:
            nb+=1

        if "RR." in C4:
            nb+=1

        if "RR." in C5:
            nb+=1

        if "RR." in C6:
            nb+=1

        if "RR." in L0:
            if ".RR." in L0:
                nb+=2
            else :nb+=1

        if "RR." in L1:
            if ".RR." in L1:
                nb+=2
            else :nb+=1

        if "RR." in L2:
            if ".RR." in L2:
                nb+=2
            else :nb+=1

        if "RR." in L3:
            if ".RR." in L3:
                nb+=2
            else :nb+=1

        if "RR." in L4:
            if ".RR." in L4:
                nb+=2
            else :nb+=1

        if "RR." in L5:
            if ".RR." in L5:
                nb+=2
            else :nb+=1

        if "RR." in L6:
            if ".RR." in L6:
                nb+=2
            else :nb+=1

        if "RR." in D0:
            if ".RR." in D0:
                nb+=2
            else :nb+=1

        if "RR." in D1:
            if ".RR." in D1:
                nb+=2
            else :nb+=1

        if "RR." in D2:
            if ".RR." in D2:
                nb+=2
            else :nb+=1

        if "RR." in D3:
            if ".RR." in D3:
                nb+=2
            else :nb+=1

        if "RR." in D4:
            if ".RR." in D4:
                nb+=2
            else :nb+=1

        if "RR." in D5:
            if ".RR." in D5:
                nb+=2
            else :nb+=1

        if "RR." in D6:
            if ".RR." in D6:
                nb+=2
            else :nb+=1

        if "RR." in D7:
            if ".RR." in D7:
                nb+=2
            else :nb+=1

        if "RR." in D8:
            if ".RR." in D8:
                nb+=2
            else :nb+=1

        if "RR." in D9:
            if ".RR." in D9:
                nb+=2
            else :nb+=1

        if "RR." in D10:
            if ".RR." in D10:
                nb+=2
            else :nb+=1

        if "RR." in D11:
            if ".RR." in D11:
                nb+=2
            else :nb+=1

        if "RR." in D12:
            if ".RR." in D12:
                nb+=2
            else :nb+=1

        if "RR." in D13:
            if ".RR." in D13:
                nb+=2
            else :nb+=1

        if "R.R" in L0:
            nb+=1
        if "R.R" in L1:
            nb+=1
        if "R.R" in L2:
            nb+=1
        if "R.R" in L3:
            nb+=1
        if "R.R" in L4:
            nb+=1
        if "R.R" in L5:
            nb+=1
        if "R.R" in L6:
            nb+=1
        if "R.R" in L0:
            nb+=1
        if "R.R" in L1:
            nb+=1
        if "R.R" in L2:
            nb+=1
        if "R.R" in L3:
            nb+=1
        if "R.R" in L4:
            nb+=1
        if "R.R" in L5:
            nb+=1
        if "R.R" in L6:
            nb+=1
        if "R.R" in D0:
            nb+=1
        if "R.R" in D1:
            nb+=1
        if "R.R" in D2:
            nb+=1
        if "R.R" in D3:
            nb+=1
        if "R.R" in D4:
            nb+=1
        if "R.R" in D5:
            nb+=1
        if "R.R" in D6:
            nb+=1
        if "R.R" in D7:
            nb+=1
        if "R.R" in D8:
            nb+=1
        if "R.R" in D9:
            nb+=1
        if "R.R" in D10:
            nb+=1
        if "R.R" in D11:
            nb+=1
        if "R.R" in D12:
            nb+=1
        if "R.R" in D13:
            nb+=1
        if "R.R" in D0:
            nb+=1
        if "R.R" in D1:
            nb+=1
        if "R.R" in D2:
            nb+=1
        if "R.R" in D3:
            nb+=1
        if "R.R" in D4:
            nb+=1
        if "R.R" in D5:
            nb+=1
        if "R.R" in D6:
            nb+=1
        if "R.R" in D7:
            nb+=1
        if "R.R" in D8:
            nb+=1
        if "R.R" in D9:
            nb+=1
        if "R.R" in D10:
            nb+=1
        if "R.R" in D11:
            nb+=1
        if "R.R" in D12:
            nb+=1
        if "R.R" in D13:
            nb+=1
        return nb

    def nb_2pions_ali_J_via(self):
        A=self.jeu
        B=np.transpose(A)
        nb=0

        c0,c1,c2="","",""
        c3,c4,c5="","",""
        c6=""
        l0,l1,l2="","",""
        l3=""
        l4,l5,l6="","",""

        for i in range(7):
            c0+=str(A[0,i])
            c1+=str(A[1,i])
            c2+=str(A[2,i])
            c3+=str(A[3,i])
            c4+=str(A[4,i])
            c5+=str(A[5,i])
            c6+=str(A[6,i])

            l0+=str(B[0,i])
            l1+=str(B[1,i])
            l2+=str(B[2,i])
            l3+=str(B[3,i])
            l4+=str(B[4,i])
            l5+=str(B[5,i])
            l6+=str(B[6,i])

        d0=str(A[0,3])+str(A[1,4])+str(A[2,5])+str(A[3,6])
        d1=str(A[0,2])+str(A[1,3])+str(A[2,4])+str(A[3,5])+str(A[4,6])
        d2=str(A[0,1])+str(A[1,2])+str(A[2,3])+str(A[3,4])+str(A[4,5])+str(A[5,6])
        d3=str(A[0,0])+str(A[1,1])+str(A[2,2])+str(A[3,3])+str(A[4,4])+str(A[5,5])+str(A[6,6])
        d4=str(A[1,0])+str(A[2,1])+str(A[3,2])+str(A[4,3])+str(A[5,4])+str(A[6,5])
        d5=str(A[2,0])+str(A[3,1])+str(A[4,2])+str(A[5,3])+str(A[6,4])
        d6=str(A[3,0])+str(A[4,1])+str(A[5,2])+str(A[6,3])
        d7=str(A[0,3])+str(A[1,2])+str(A[2,1])+str(A[3,0])
        d8=str(A[0,4])+str(A[1,3])+str(A[2,2])+str(A[3,1])+str(A[4,0])
        d9=str(A[0,5])+str(A[1,4])+str(A[2,3])+str(A[3,2])+str(A[4,1])+str(A[5,0])
        d10=str(A[0,6])+str(A[1,5])+str(A[2,4])+str(A[3,3])+str(A[4,2])+str(A[5,1])+str(A[6,0])
        d11=str(A[1,6])+str(A[2,5])+str(A[3,4])+str(A[4,3])+str(A[5,2])+str(A[6,1])
        d12=str(A[2,6])+str(A[3,5])+str(A[4,4])+str(A[5,3])+str(A[6,2])
        d13=str(A[3,6])+str(A[4,5])+str(A[5,4])+str(A[6,3])

        C0=inverser_ch(c0)
        C1=inverser_ch(c1)
        C2=inverser_ch(c2)
        C3=inverser_ch(c3)
        C4=inverser_ch(c4)
        C5=inverser_ch(c5)
        C6=inverser_ch(c6)
        L0=l0
        L1=l1
        L2=l2
        L3=l3
        L4=l4
        L5=l5
        L6=l6
        D0=inverser_ch(d0)
        D1=inverser_ch(d1)
        D2=inverser_ch(d2)
        D3=inverser_ch(d3)
        D4=inverser_ch(d4)
        D5=inverser_ch(d5)
        D6=inverser_ch(d6)
        D7=d7
        D8=d8
        D9=d9
        D10=d10
        D11=d11
        D12=d12
        D13=d13

        if "JJ." in C0:
            nb+=1

        if "JJ." in C1:
            nb+=1

        if "JJ." in C2:
            nb+=1

        if "JJ." in C3:
            nb+=1

        if "JJ." in C4:
            nb+=1

        if "JJ." in C5:
            nb+=1

        if "JJ." in C6:
            nb+=1

        if "JJ." in L0:
            if ".JJ." in L0:
                nb+=2
            else :nb+=1

        if "JJ." in L1:
            if ".JJ." in L1:
                nb+=2
            else :nb+=1

        if "JJ." in L2:
            if ".JJ." in L2:
                nb+=2
            else :nb+=1

        if "JJ." in L3:
            if ".JJ." in L3:
                nb+=2
            else :nb+=1

        if "JJ." in L4:
            if ".JJ." in L4:
                nb+=2
            else :nb+=1

        if "JJ." in L5:
            if ".JJ." in L5:
                nb+=2
            else :nb+=1

        if "JJ." in L6:
            if ".JJ." in L6:
                nb+=2
            else :nb+=1

        if "JJ." in D0:
            if ".JJ." in D0:
                nb+=2
            else :nb+=1

        if "JJ." in D1:
            if ".JJ." in D1:
                nb+=2
            else :nb+=1

        if "JJ." in D2:
            if ".JJ." in D2:
                nb+=2
            else :nb+=1

        if "JJ." in D3:
            if ".JJ." in D3:
                nb+=2
            else :nb+=1

        if "JJ." in D4:
            if ".JJ." in D4:
                nb+=2
            else :nb+=1

        if "JJ." in D5:
            if ".JJ." in D5:
                nb+=2
            else :nb+=1

        if "JJ." in D6:
            if ".JJ." in D6:
                nb+=2
            else :nb+=1

        if "JJ." in D7:
            if ".JJ." in D7:
                nb+=2
            else :nb+=1

        if "JJ." in D8:
            if ".JJ." in D8:
                nb+=2
            else :nb+=1

        if "JJ." in D9:
            if ".JJ." in D9:
                nb+=2
            else :nb+=1

        if "JJ." in D10:
            if ".JJ." in D10:
                nb+=2
            else :nb+=1

        if "JJ." in D11:
            if ".JJ." in D11:
                nb+=2
            else :nb+=1

        if "JJ." in D12:
            if ".JJ." in D12:
                nb+=2
            else :nb+=1

        if "JJ." in D13:
            if ".JJ." in D13:
                nb+=2
            else :nb+=1

        if "J.J" in L0:
            nb+=1
        if "J.J" in L1:
            nb+=1
        if "J.J" in L2:
            nb+=1
        if "J.J" in L3:
            nb+=1
        if "J.J" in L4:
            nb+=1
        if "J.J" in L5:
            nb+=1
        if "J.J" in L6:
            nb+=1
        if "J.J" in L0:
            nb+=1
        if "J.J" in L1:
            nb+=1
        if "J.J" in L2:
            nb+=1
        if "J.J" in L3:
            nb+=1
        if "J.J" in L4:
            nb+=1
        if "J.J" in L5:
            nb+=1
        if "J.J" in L6:
            nb+=1
        if "J.J" in D0:
            nb+=1
        if "J.J" in D1:
            nb+=1
        if "J.J" in D2:
            nb+=1
        if "J.J" in D3:
            nb+=1
        if "J.J" in D4:
            nb+=1
        if "J.J" in D5:
            nb+=1
        if "J.J" in D6:
            nb+=1
        if "J.J" in D7:
            nb+=1
        if "J.J" in D8:
            nb+=1
        if "J.J" in D9:
            nb+=1
        if "J.J" in D10:
            nb+=1
        if "J.J" in D11:
            nb+=1
        if "J.J" in D12:
            nb+=1
        if "J.J" in D13:
            nb+=1
        if "J.J" in D0:
            nb+=1
        if "J.J" in D1:
            nb+=1
        if "J.J" in D2:
            nb+=1
        if "J.J" in D3:
            nb+=1
        if "J.J" in D4:
            nb+=1
        if "J.J" in D5:
            nb+=1
        if "J.J" in D6:
            nb+=1
        if "J.J" in D7:
            nb+=1
        if "J.J" in D8:
            nb+=1
        if "J.J" in D9:
            nb+=1
        if "J.J" in D10:
            nb+=1
        if "J.J" in D11:
            nb+=1
        if "J.J" in D12:
            nb+=1
        if "J.J" in D13:
            nb+=1
        return nb