def check(hand):
    return hand <= 2 and hand >= 0

def choice(hand, name):
    hands = ['Rock','Paper','Scissors']
    return print(f'{name} Pick : {hands[hand]}')

def result(player,computer):
    if computer == player:
        return 'Draw!'
    elif (
        computer == 0
        and player == 1
        or computer == 1
        and player == 2
        or computer == 2
        and player == 0
    ):
        return 'You Win!'
    else:
        return 'You Lose!'