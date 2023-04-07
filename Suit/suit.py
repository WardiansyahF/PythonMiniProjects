import random 
import judge

    
print('================================================')
print('======Welcome to Rock,Paper,Scissors Game!======')
print('================================================')  

ask = input('Do you want to play this game? (Y/N): ')

while ask == 'Y':
    print('Lets play this game!')
    player = input('What is your name? ')
    print('Select one : (Rock : 0, Scissors : 1, Paper : 2)')
    player_pick = int(input('Input the number (0-2): '))
    
    if judge.check(player_pick) :
        judge.choice(player_pick, player)
        computer_pick = random.randint(0,2)
        judge.choice(computer_pick, 'Computer')
        print('The result is : ' + judge.result(player_pick, computer_pick))
    else :
        print('You enter the wrong number, please try again!')
        
    ask = input('Do you want to play again? (Y/N): ')

if ask == 'N' :
    print('Thanks for coming!')
    quit()
elif ask != 'N' and ask != 'Y':
    print("Wrong Input!")
    quit()
    