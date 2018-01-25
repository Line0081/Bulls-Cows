import copy
import random
from math import *

# core algorithm for Bulls and Cows
# the idea of this algorithm is to find the next guess
# that can reduce the number of potential guesses the most
def get_guess(po):
    if len(po) == 1:
        guess = po[0]
        return guess
    #generate next guess
    elif len(po) == 10000:
        return po[(random.randint(0, 9999))]
    elif len(po) > 100:
        # index affects the size of sample pool
        # greater index produce more thoughtful guess
        index = 2
        eff = []
        for g in po:
            reduced = 0
            for i in range(0, int((log2(len(po)) ** index) * (10000 / len(po)))):
                a = po[random.randint(0, len(po) - 1)]
                re = po[random.randint(0, len(po) - 1)]
                if getB(g, a) != getB(g, re) or getC(g, a) != getB(g, re):
                    reduced += 1
            eff.append([g, reduced])
        g, efficiency = max(eff, key=lambda item: item[1])
        return g
    else:
        eff = []
        for g in po:
            reduced = 0
            for a in po:
                for re in po:
                    if getB(g, a) != getB(g, re) or getC(g, a) != getB(g, re):
                        reduced += 1
            eff.append([g, reduced])
        g, efficiency = max(eff, key=lambda item: item[1])
        return g

# get the number of cows
# smae position and same number
def getC(guess, answer):
    same_position = 0 # number of cows
    for pointer in range(0, 4):
        if guess[pointer] == answer[pointer]:
            same_position += 1
    return same_position

# get the number of bulls
# same number but different position
def getB(guess, answer):
    answerPointer = []
    guessPointer = []
    same_number = 0
    for pointer in range(0, 4):
        if guess[pointer] == answer[pointer]:
            guessPointer.append(pointer)
            answerPointer.append(pointer)
    for pointer in range(0,4):
        for pointer_guess in range(0,4):
            if guess[pointer_guess] == answer[pointer] \
                    and pointer_guess != pointer \
                    and pointer not in answerPointer\
                    and pointer_guess not in guessPointer:
                same_number += 1
                answerPointer.append(pointer)
                guessPointer.append(pointer_guess)
                break
    return same_number

def getRemain(po, g, c, b):
    # po is potential guess, g is current guess; c and b are cows and bulls
    ls = copy.copy(po)
    for e in po:
        if getB(g, e) != b or getC(g, e) != c:
            ls.remove(e)
    return ls

def get_answer(po):
    randomNumber = random.randint(1000, 10000)
    return po[random.randint(0, 9999)]

