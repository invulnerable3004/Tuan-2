#!/usr/bin/env python
# coding: utf-8

# In[1]:


from os import system

#xac dinh nuoc di tiep theo la X hay O
def genXorO(p):
    if p==True: return 'X'
    else: return 'O'

#khong cho phep danh vao o nguoi khac da danh
def validMove(l, pos):
    if pos=='1': return l[0][0]=='-'
    if pos=='2': return l[0][2]=='-'
    if pos=='3': return l[0][4]=='-'
    if pos=='4': return l[1][0]=='-'
    if pos=='5': return l[1][2]=='-'
    if pos=='6': return l[1][4]=='-'
    if pos=='7': return l[2][0]=='-'
    if pos=='8': return l[2][2]=='-'
    if pos=='9': return l[2][4]=='-'
    
#xuat san choi ra man hinh
def printOut(l): 
    system('cls')
    for i in range(len(l)):
        for j in range(len(l[0])):
            print(l[i][j], end=''),
        print('\n')

#ham bo tro kiem tra co nguoi thang cuoc hay chua - theo hang ngang
def checkRow(l):
    if (l[0][0]==l[0][2]==l[0][4] and l[0][0]!='-') or (l[1][0]==l[1][2]==l[1][4] and l[1][0]!='-') or (l[2][0]==l[2][2]==l[2][4] and l[2][0]!='-'): return True
    return False

#ham bo tro kiem tra co nguoi thang cuoc hay chua - theo hang doc
def checkCol(l):
    if (l[0][0]==l[1][0]==l[2][0] and l[0][0]!='-') or (l[0][2]==l[1][2]==l[2][2] and l[0][2]!='-') or (l[0][4]==l[1][4]==l[2][4] and l[0][4]!='-'): return True
    return False

#ham bo tro kiem tra co nguoi thang cuoc hay chua - theo duong cheo
def checkCro(l):
    if l[1][2]!='-' and (l[0][0]==l[1][2]==l[2][4] or l[0][4]==l[1][2]==l[2][0]): return True
    return False

#kiem tra xem co nguoi thang cuoc hay chua
def checkWinner(l): 
    if checkRow(l) or checkCol(l) or checkCro(l): return True
    return False

#kiem tra hoa
def checkDraw(l): 
    for i in range(len(l)):
        for j in range(len(l[0])):
            if l[i][j]=='-': return False
            if i==2 and j==4: return True

#ham van hanh tro choi
def main_game():
    L = [['-', '|', '-', '|', '-'] for i in range(3)] #mang 2 chieu xu ly duoc tao bang list comprehension
    player = True
    while True:
        printOut(L)
        if checkWinner(L): #xet luot di tiep theo, neu luot di tiep theo cua p1 thi p2 da thang va nguoc lai
            if player==True: print('PLAYER 2 (O) WON THE GAME, PLAYER 1 (X) IS A CHICKEN')
            else: print('PLAYER 1 (X) WON THE GAME, PLAYER 2 (O) IS A CHICKEN')
            break
        if checkDraw(L):
            print("IT'S A DRAW, CONGRATULATION TO BOTH OF YOU")
            break
        if player: print('LUOT DI CUA PLAYER 1 (X)')
        else: print('LUOT DI CUA PLAYER 2 (O)')
        a = input()
        while not a in '123456789':
            print('Chi duoc nhap tu 1 den 9')
            print('Hay nhap lai: ', end='')
            a=input()
        while not validMove(L, a):
            print('Vi tri',a,'da co mot nuoc co')
            print('Hay chon vi tri khac: ', end='')
            a=input()
        if a=='1' and validMove(L, a): L[0][0]=genXorO(player)
        elif a=='2' and validMove(L, a): L[0][2]=genXorO(player)
        elif a=='3' and validMove(L, a): L[0][4]=genXorO(player)
        elif a=='4' and validMove(L, a): L[1][0]=genXorO(player)
        elif a=='5' and validMove(L, a): L[1][2]=genXorO(player)
        elif a=='6' and validMove(L, a): L[1][4]=genXorO(player)
        elif a=='7' and validMove(L, a): L[2][0]=genXorO(player)
        elif a=='8' and validMove(L, a): L[2][2]=genXorO(player)
        elif a=='9' and validMove(L, a): L[2][4]=genXorO(player)
        player = (not player)
        
#chuong trinh chinh
while True:
    print('Tic Tac Toe - Made by Vo Dong Cac - 59136296')
    print('Nhap 1 de bat dau tro choi')
    print('Nhap 0 de ket thuc')
    n=input()
    while n!='0' and n!='1':
        print('Chi duoc nhap 0 va 1')
        print('Hay nhap lai: ', end='')
        n=input()
    if n=='0':
        system('cls')
        print('GAME OVER')
        break
    elif n=='1':
        system('cls')
        main_game()
        print('\n')


# In[ ]:





# In[ ]:




