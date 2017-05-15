import random
# 1 is rock
# 2 is paper
# 3 is scissors

def main():
    x = 1
    while (x == 1):
            destiny = (random.randint(1, 3))
            print("Rock Paper Scissors! 1 is a rock, 2 is paper, 3 is scissors!\n")
            rps = int(input("Pick a number between 1 and 3! Beat the computer! Or Press 0 to quit \n"))


            if (rps > 3):
                print("Incorrect number, try again.")
            elif(rps == 1 and destiny == 1):
                print('The Computer has played', destiny, ' and you played ', rps)
                print("Draw!")
            elif(rps == 2 and destiny == 1) or (rps == 3 and destiny == 2) or (rps == 1 and destiny == 3):
                print('The Computer has played', destiny, ' and you played ', rps)
                print("You win!")
            elif(rps == 0):
                x = 0
                break
            else:
                print('The Computer has played', destiny, ' and you played ', rps)
                print("You lose :(")
    print("That was fun!")
main()
        
        

    
