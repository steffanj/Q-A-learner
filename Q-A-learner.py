#!/usr/bin/python3
# -*-coding=utf-8 -*-

import random
import time

def main():
    '''
    This script will ask you to give the correct translation of a letter/word/
    sentence or a correct answer to a question. It was initially created to 
    learn the Korean alphabet - the Jamo characters. Questions and Answers are
    imported from a csv file which has to have the following structure:
        question1, answer1
        # This is a comment: lines in your csv file starting with a '#' are not 
        # considered to be questions or answers and are therefore ignored
        question2, answer2
        ...
    Questions can be scrambled before rehearsal, and the user can specify if 
    he/she wants to start over if a mistaske is made. If unicode characters are
    not shown correctly, please be aware that the csv file is read using utf-8 
    encoding. If utf-8 characters are not shown correctly, please check if your
    terminal supports them (Windows' CMD terminal does not by default).
    
    To do:
        * Make it possible to have multiple valid Answers to a Question; the 
          program could ask for all correct Answers
        * Create statistics to keep account of Questions that appear to be 
          harder/easier to answer
        * Make a GUI/web interface 
    '''

    fname = input('Enter name of the csv file containing the Questions and Answers: ')
    fh = open(fname, encoding='utf-8')
    objects = []
    try:
        for line in fh:
            if not line[0] == '#':
                objects.append([x.strip() for x in line.split(',')])
        fh.close()        
    except ValueError:
        print('Something went wrong while reading the csv file')
   
    # Ask if the user wants to answer the Questions in a randomized order or 
    # not
    randFlag = input('Would you like to scramble the Questions? (y/n): ')
   
    # Randomize the Questions if requested
    if randFlag == 'y':
#        objects = list(objects)
        random.shuffle(objects)
        print('Questions are scrambled')
    elif randFlag == 'n':
        print('Questions will not be scrambled')
    else:
        print("You did not specify 'y' or 'n'. The Questions will not be "
        "scrambled")
        
    # Ask if the user wants to start all over from the beginning if an 
    # incorrect Answer was given. This preserves the order in which the 
    # Questions were asked
    startAllOverFlag = input('Would you like to start all over when you give '
                             'an incorrect Answer? \nThe order in which the '
                             'Questions are asked will be preserved (y/n): ')
    if startAllOverFlag == 'y':
        startAllOverFlag = True
        print('Script will start over if you make a mistake')
    elif startAllOverFlag == 'n':
        startAllOverFlag = False
        print('Script will stay at the same Question if you make a mistake')
    else:
        startAllOverFlag = False
        print("You did not specify 'y' or 'n'. The script will stay at the "
              "same Question if you make a mistake") 
        
    if not startAllOverFlag:        
        for object in range(0, len(objects)):
            currFinished = False
            correct_cntr = 1
            while currFinished == False:
                answer = check_answer(objects[object][0], objects[object][1])
                if answer == True:
                    currFinished = True
                    print('Correct!')
                    if correct_cntr > 2:
                        print('But you needed no less than {} tries before ' 
                        'getting it correctly though'.format(correct_cntr))    
                    elif correct_cntr > 1:
                        print('You tried {} times before getting it correctly'
                              .format(correct_cntr))
                    print('Moving on to the next Question...')
                    break
                elif answer == False:
                    print('Incorrect!\nTry again...')
                    correct_cntr += 1
        print('You have correctly answered all Questions!')
    elif startAllOverFlag:
        finished = False
        while finished == False:
            for object in range(0, len(objects)):
                answer = check_answer(objects[object][0], objects[object][1])
                if answer == False:
                    print('Incorrect! The correct answer was {}'
                          .format(objects[object][1]))
                    print('Starting over in...')
                    print(3)
                    time.sleep(1)
                    print(2)
                    time.sleep(1)
                    print(1)
                    time.sleep(1)
                    # Perhaps not thhe best way to clear the terminal screen 
                    # but it is effective in preventing the user from seeing
                    # previous, correct answers in their terminal
                    print('\n'*100)
                    break
                elif answer == True:
                    if object == len(objects)-1:
                        print('You have correctly answered all Questions!')
                        finished = True
                    else:
                        print('Correct!\nMoving on to the next Question')                  

# Check the Answer to a Question 
def check_answer(key, solution):
    answer = input('{} corresponds to: '.format(key))
    if answer == solution:
        correct = True
        return correct
    else:
        correct = False
        return correct
        
if __name__ == "__main__": main()