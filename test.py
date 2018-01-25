from get import *

# initialize the potential guess list
# fulfill it with 0000 to 9999 in string
def initial():
    po = []
    for a in range(0, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                for d in range(0, 10):
                    guess = str(a) + str(b) + str(c) + str(d)
                    po.append(guess)
    return po

# evaluate the effect of the algorithm
# play the game multiple times
# get the average times the algorithm used
def main():
    total_counter = 0 # used to calculate average times
    played_times = 0 # total played times
    while played_times < 100:
        played_times += 1
        counter = 1
        po = initial() # store the potential guess
        guessed_list = [] # store what already guessed
        answer = get_answer(po)
        print('The answer is: ' + answer)
        guess = get_guess(po)
        print('My guess is: ' + guess)
        while guess != answer:
            guessed_list.append(guess)
            po = getRemain(po, guess, getC(guess, answer), getB(guess, answer))
            guess = get_guess(po)
            print('My guess is: ' + guess)
            while guess in guessed_list:
                if len(po) == 1:
                    break
                else:
                    guess = get_guess(po)
            counter += 1
        print(counter)
        total_counter += counter
    average = total_counter / (played_times)
    print(average)

main()



