import random
#to generate word to be guessed randomly

def random_word():
    file=open("hangman_word")
    word=file.readlines()
    randomwords=random.choice(word)
    randomwords = str(randomwords).strip("")
    randomwords = str(randomwords).strip("\n")
    randomwords=randomwords.lower()
    return randomwords

def hangman_photo(guess,x):
    if (guess==0):
        print("________________\n"
              "|          |\n"
              "|\n"
              "|\n"
              "|\n"
              "|\n"
              "|\n"
              "|\n"
              "|\n"
              "|________________\n")
    if (guess==1):
        print("________________\n"
              "|          |\n"
              "|          |\n"
              "|\n"
              "|\n"
              "|\n"
              "|\n"
              "|\n"
              "|\n"
              "|________________\n")
    if (guess==2):
        print("________________\n"
              "|          |\n"
              "|          |\n"
              "|          O\n"
              "|\n"
              "|\n"
              "|\n"
              "|\n"
              "|\n"
              "|________________\n")
    if (guess==3):
        print("________________\n"
              "|          |\n"
              "|          |\n"
              "|          0\n"
              "|           /\n"
              "|\n"
              "|\n"
              "|\n"
              "|\n"
              "|________________\n")
    if (guess==4):
        print("________________\n"
              "|          |\n"
              "|          |\n"
              "|          0\n"
              "|          \/\n"
              "|\n"
              "|\n"
              "|\n"
              "|\n"
              "|________________\n")
    if (guess==5):
        print("________________\n"
              "|          |\n"
              "|          |\n"
              "|          0\n"
              "|          \/\n"
              "|          |\n"
              "|\n"
              "|\n"
              "|\n"
              "|________________\n")
    if (guess==6):
        print("________________\n"
              "|          |\n"
              "|          |\n"
              "|          0\n"
              "|          \/\n"
              "|          |\n"
              "|          /\n"
              "|\n"
              "|\n"
              "|________________\n")
    if (guess==7):
        print("________________\n"
              "|          |\n"
              "|          |\n"
              "|          0\n"
              "|          \/\n"
              "|          |\n"
              "|          /\ \n"
              "|\n"
              "|\n"
              "|________________\n")
        print("\nYOU LOST,TRY AGAIN")
        print("CORRECT WORD IS: %s.\n"%str(x))
        print("\nDO YOU WANT TO PLAY AGAIN- PRESS + FOR YES OR - FOR NO")
        secondtry = input('')
        if secondtry == '+':
           game()
        quit()

def game():

    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load('musicfinal.MP3')
    pygame.mixer.music.play()

    guess=0
    x=random_word()
    xlist=list(x)
    dash="_"*len(x)
    dashlist=list(dash)
    lettergiven=[]
    new=list(dash)
    print("HANGMAN BEGINS!\n" )
    hangman_photo(guess,x)
    print("\n"+''.join(dashlist))
    print("GUESS A LETTER:")
    while guess<8:
        letter=input(">>> ")
        letter=letter.lower()

        if len(letter)>1:
            print("OOPS!ONLY ONE LETTER ALLOWED.")

        elif len(letter) == 0:
            print("ERROR!NO INPUT GIVEN.")

        elif letter in lettergiven:
            print("OOPS!THE LETTER IS REPEATED.")
            print(''.join(lettergiven))

        else:
            lettergiven.append(letter)
            i=0
            while i<len(x):
                if letter==x[i]:
                    new[i]=xlist[i]
                i+=1

        if new==dashlist:
            print("WRONG GUESS")
            guess=guess+1
            hangman_photo(guess,x)

            if guess<8:
                print("GUESS AGAIN!")
                print(''.join(dashlist))
        elif xlist!=dashlist:
            dashlist=new[:]
            print("".join(dashlist))
            if xlist==dashlist:
                print("\nHURRAY,YOU WON")
                print("DO YOU WANT TO PLAY AGAIN- PRESS + FOR YES OR - FOR NO")
                secondtry=input('')
                if secondtry=='+':
                    game()
                    pygame.mixer.music.stop()
                quit()
            else:
                print('YOU LOOK CHAMPION,GUESS THE NEXT')
                guess+=1
                continue

game()










