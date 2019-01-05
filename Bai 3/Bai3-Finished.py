from os import system

#create a list of tuples to store players' names and their scores
#used as leader board
scores = [('Default', -1) for i in range(10)]

#only allow 10 people with the highest scores to be in the leader board
#input: player's name and his/her score
#output: leader board with their name inside or not
def fixLeaderBoard(name, score):
    scores.append((name, score))
    scores.sort(key = lambda x: x[1], reverse = True)
    del scores[-1]

#print out the leader board
def printLeaderBoard():
    system('cls')
    for ind, (name, score) in enumerate(scores):
        print(ind+1, '\t', name, '\t\t', score)
    print('\n')
    input('PRESS <ENTER> TO BACK TO MENU')
    
#the main game
#input: file's name
#output: the game runs based on that file
def main_game(name):
    system('cls')
    score = 0
    player_name = input('Your name: ')
    if player_name == '':
        print("OK, you don't want to play with a name.")
        print("Your name will be saved as 'Cac dep trai' in the leader board.")
        player_name = 'Cac dep trai'
        input('PRESS <ENTER> TO CONTINUE')
    f = open(name, 'r')
    while True:
        system('cls')
        cauhoi=f.readline()
        if not cauhoi: break
        dapanA=f.readline()
        dapanB=f.readline()
        dapanC=f.readline()
        dapanD=f.readline()
        dapan=f.readline()
        print(cauhoi)
        print(dapanA)
        print(dapanB)
        print(dapanC)
        print(dapanD)
        answer = input('Your answer: ')
        while not answer in 'ABCD':
            print('Just take one of the 4 choices, you idiot.')
            answer = input('Your choice: ')
        if answer + '\n' == dapan or answer == dapan:
            print("Good job, you've just earned 1 point.")
            score = score + 1
        else: print("Too bad, the answer was ", dapan)
        input('Press <Enter> to go to next question.')
    fixLeaderBoard(player_name, score)
    f.close()
    
#main program
while True:
    system('cls')
    print('Welcome to da Quiz made by Vo Dong Cac.')
    print('0. Exit.')
    print('1. Start playing.')
    print('2. See leader board.')
    control = input('Your choice: ')
    while (not control in '012'):
        print('Please choose a number within the menu.')
        control = input('Your choice: ')
    if control=='0':
        print('GAME OVER')
        input('PRESS <ENTER> TO CLOSE WINDOW')
        break
    if control=='1':
        n = input('Please choose your questions pack by typing a number in range from 1 to 4: ')
        while not n in '1234' or n=='':
            print('Please choose a number within the range.')
            n = input('Your choice: ')
        file_name = 'bode' + n + '.txt'
        main_game(file_name)
    if control=='2': printLeaderBoard()