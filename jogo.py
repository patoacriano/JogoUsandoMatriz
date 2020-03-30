import random as rd

jogando = True

tab = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#1
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#2    #16x16
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#3
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#4
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#5
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#6
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#7
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#8
       [1,1,1,1,1,1,1,2,30,1,1,1,1,1,1,1],#9
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#10
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#11
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#12
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#13
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#14
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#15
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]#16

def rendertab(rodadas,pontos,bicho):
    for i in range(len(tab)):
        for j in range(len(tab)):
            if tab[i][j] == 1:
                print("█",end='')
            elif tab[i][j] == 2:
                print("●",end='')
            elif tab[i][j] == 3:
                print("♦",end='')
            elif tab[i][j] == 30:
                print("/",end='')
        if tab[i][j] == 1:
            print("█",end='')
        print()
    print("\t\tRodadas:{}".format(rodadas))
    print("\t\tPontos:{}".format(pontos))
    print("\t\tBichos:{}".format(bicho))

def andar():
    pontos = 0
    rodadas = 0
    jogando = True
    andou = False
    bicho = 0
    bichosx = []
    bichosy = []

    bx = int()
    by = int()
    while jogando == True:
        pdnsc = False
        rendertab(rodadas,pontos,bicho)
        for i in range(len(tab)):
            for j in range(len(tab)):
                if tab[i][j] == 2:
                    px = j
                    py = i
        mov=input(">")
        if mov == 'w':
            npx = px
            npy = py-1
            if py == 0:
                npy = len(tab) -1
            if 0<=npy<=len(tab): #nesse caso, pode andar
                if tab[npy][npx] == 3:
                    print("\n\t\tTu morreu!")
                    jogando = False
                tab[npy][npx] = 2
                if tab[npy][npx+1] == 3:
                    bicho-=1
                    pontos+=1
                tab[npy][npx+1] = 30
                tab[py][px+1]=1
                tab[py][px] = 1
            else:
                tab[py][px] == 2

        if mov == 's':
            npx = px
            npy = py+1
            if py == len(tab)-1:
                npy = 0
            if 0<=py<=len(tab): #nesse caso, pode andar
                if tab[npy][npx] == 3:
                    print("\n\t\tTu morreu!")
                    jogando = False
                tab[npy][npx] = 2
                if tab[npy][npx+1] == 3:
                    bicho-=1
                    pontos+=1
                tab[npy][npx+1] = 30
                tab[py][px+1]=1
                tab[py][px] = 1

            else:
                tab[py][px] == 2

        if mov == 'a':
            npx = px-1
            npy = py
            if px == 0:
                npx= len(tab)-2
                pex =len(tab)-1
                mdlado = True
            else:
                pex = npx+1
                mdlado = False
            if 0<=npx<=len(tab): #nesse caso, pode andar
                if tab[npy][npx] == 3:
                    print("\n\t\tTu morreu!")
                    jogando = False
                tab[npy][npx] = 2
                if tab[npy][npx] == 3:
                    bicho-=1
                    pontos+=1
                tab[npy][pex] = 30
                if mdlado == True:
                    tab[py][1] = 1
                    tab[py][0] = 1
                else:
                    tab[py][px+1]=1
#                tab[py][px] = 1

            else:
                tab[py][px] == 2

        if mov == 'd':
            npx = px+1
            npy = py
            if px == len(tab)-2:
                npx = 0
                pex = 1
                mdlado = True
            else:
                pex = npx+1
                mdlado = False
            if 0<=px<=len(tab): #nesse caso, pode andar
                if tab[npy][npx] == 3 and mdlado == False:
                    print("\n\t\tTu morreu!")
                    jogando = False
                if mdlado == True:
                    bicho-=1
                    pontos+=1
                tab[npy][npx] = 2
                if tab[npy][npx+1] == 3:
                    bicho-=1
                    pontos+=1
                tab[npy][pex] = 30
                #tab[py][px+1]=1
                if mdlado == True:
                    tab[py][len(tab)-2] = 1
                    tab[py][len(tab)-1] = 1
                else:
                    tab[py][px] = 1

            else:
                tab[py][px] == 2
        
        bisx = int()
        bisy = int()
        if pdnsc == False and bicho<=10:
            bix = rd.randrange(len(tab))
            biy = rd.randrange(len(tab))
            tab[biy][bix] = 3
#            bichosx[bicho] = bix
            bichosx.append(bix)
#            bichosy[bicho] = biy
            bichosy.append(biy)
            bicho+=1







        if jogando == True:
            rodadas+=1


andar()
