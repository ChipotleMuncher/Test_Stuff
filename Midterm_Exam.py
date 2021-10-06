print()
print ('Welcome to "Rock, Paper, Scisors, Lizard, Spock"')
print ()
print ('1 = Rock')
print ('2 = Paper')
print ('3 = Scissors')
print ('4 = Lizard')
print ('5 = Spock')
print()

import random
computer_choice = random.randint(1,5)
human_choice = int (input ('Please make a number selection: '))
print ()

if computer_choice == 1:
    print ('The computer chose rock.')

    if human_choice == 1:
        print ('You chose rock.')
        print ('Its a tie!')

    elif human_choice == 3 or human_choice == 4:
        if human_choice == 3:
            print ('You chose scissors.')
            print ('Rock crushes scissors.')
        if human_choice == 4:
            print('You chose lizard.')
            print ('Rock crushes lizard.')
        print ('You lose!')

    elif human_choice == 2 or human_choice == 5:
        if human_choice == 2:
            print ('You chose paper.')
            print ('Paper covers rock.')
        if human_choice == 5:
            print ('You chose Spock.')
            print ('Spock vaproizes rock.')
        print ('You win!')
if computer_choice == 2:
    print ('The computer chose paper.')

    if human_choice == 2:
        print ('You chose paper.')
        print ('Its a tie!')

    elif human_choice == 1 or human_choice == 5:
        if human_choice == 1:
            print ('You chose rock.')
            print ('Paper covers rock.')
        if human_choice == 5:
            print('You chose Spock.')
            print ('Paper disproves Spock.')
        print ('You lose!')

    elif human_choice == 3 or human_choice == 4:
        if human_choice == 3:
            print ('You chose scissors.')
            print ('Scissors cut paper.')
        if human_choice == 4:
            print ('You chose lizard.')
            print ('Lizard eats paper.')
        print ('You win!')
if computer_choice == 3:
    print ('The computer chose scissors.')

    if human_choice == 3:
        print ('You chose scissors.')
        print ('Its a tie!')

    elif human_choice == 4 or human_choice == 2:
        if human_choice == 4:
            print ('You chose lizard.')
            print ('Scissors decapitates lizard.')
        if human_choice == 2:
            print('You chose paper.')
            print ('Scissors cut paper.')
        print ('You lose!')

    elif human_choice == 1 or human_choice == 5:
        if human_choice == 1:
            print ('You chose rock.')
            print ('Rock crushes scissor.')
        if human_choice == 5:
            print ('You chose Spock.')
            print ('Spock smashes scissors.')
        print ('You win!')
if computer_choice == 4:
    print ('The computer chose lizard.')

    if human_choice == 4:
        print ('You chose lizard.')
        print ('Its a tie!')

    elif human_choice == 2 or human_choice == 5:
        if human_choice == 2:
            print ('You chose paper.')
            print ('Lizard eats paper.')
        if human_choice == 5:
            print('You chose Spock.')
            print ('Lizard poisons Spock.')
        print ('You lose!')

    elif human_choice == 1 or human_choice == 3:
        if human_choice == 1:
            print ('You chose rock.')
            print ('Rock crushes lizard.')
        if human_choice == 3:
            print ('You chose scisors.')
            print ('Scissors decapitate lizard.')
        print ('You win!')
if computer_choice == 5:
    print ('The computer chose Spock.')

    if human_choice == 2:
        print ('You chose Spock.')
    print ('Its a tie!')

    if human_choice == 1 or human_choice == 3:
        if human_choice == 1:
            print ('You chose rock.')
            print ('Spock vaproizes rock.')
        if human_choice == 3:
            print('You chose scissors.')
            print ('Spock smashes scissors.')
        print ('You lose!')

    elif human_choice == 2 or human_choice == 4:
        if human_choice == 2:
            print ('You chose paper.')
            print ('Paper disproves Spock.')
        if human_choice == 4:
            print ('You chose lizard.')
            print ('Lizard poisons Spock.')
        print ('You win!')