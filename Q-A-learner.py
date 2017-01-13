#!/usr/bin/python3
# -*-coding=utf-8 -*-

import random
import time

def main():
    '''
    This script will ask you to give the correct translation of a letter/word/
    sentence or a correct answer to a question. It was initially created to 
    learn the Korean alphabet - the Jamo characters. In a future version, 
    Questions and Answers may be imported from an external file, but for now 
    they have to be defined inside this script. Questions can be scrambled 
    before rehearsal, and the user can specify if he/she wants to start over 
    if a mistaske is made. The user's terminal should support Unicode 
    characters.
    
    To do:
        * Make it possible to load Questions and Answers from an external file
        * Make it possible to have multiple valid Answers to a Question; the 
          program could ask for all correct Answers
        * Create statistics to keep account of Questions that appear to be 
          harder/easier to answer
        * Check if the Unicode characters are correctly displayed
        * Make a GUI/web interface 
    '''
    
    # Questions and Answers are defined here, inside a tuple. Each Q/A couple 
    # is defined as a tuple in the format ('Question', 'Answer'). 
    objects = (# The 51 Korean Jamo characters defined as non-obsolete on 
              # https://en.wikipedia.org/wiki/Hangul#Letters
              # Consonants
              ('\u1100','g'), ('\u1102', 'n'), ('\u1103', 'd'), 
              ('\u1105 (1)', 'l'), ('\u1105 (2)', 'r'), ('\u1106', 'm'), 
              ('\u1107', 'b'), ('\u1109', 's'), ('\u110B when used as the '
              'first character in a syllable', 'null'), ('\u110B when used as '
              'the last character in a syllable', 'ng'), ('\u110C', 'j'), 
              ('\u110E', 'ch'), ('\u110F', 'k'), ('\u1110', 't'), 
              ('\u1111', 'p'), ('\u1112', 'h'),
              # Vowels
              ('\u1161', 'a'), ('\u1165', 'eo'), ('\u1169', 'o'), 
              ('\u116E', 'u'), ('\u1173', 'eu'), ('\u1175', 'i'),
              # Iotized vowels (with a 'y')
              ('\u1163', 'ya'), ('\u1167', 'yeo'), ('\u116D', 'yo'), 
              ('\u1172', 'yu'),
              # Double consonants
              ('\u1101', 'kk'), ('\u1104', 'tt'), ('\u1108', 'pp'), 
              ('\u11BB', 'ss'), ('\u110D', 'jj'), 
              # Consonant clusters
              ('\u3133', 'gs'), ('\u3135', 'nj'), ('\u3136', 'nh'), 
              ('\u313A', 'lg'), ('\u313B', 'lm'), ('\u313C', 'lb'), 
              ('\u313D', 'ls'), ('\u313E', 'lt'), ('\u313F', 'lp'), 
              ('\u3140', 'lh'), ('\u3144', 'bs'), 
              # (Iotized) diphthongs
              ('\u3150', 'ae'), ('\u3152', 'yae'), ('\u3154', 'e'), 
              ('\u3156', 'ye'), ('\u3162', 'ui'), 
              # Vowels and diphthongs with a w
              ('\u3158', 'wa'), ('\u3159', 'wae'), ('\u315A', 'oe'), 
              ('\u315D', 'wo'), ('\u315E', 'we'), ('\u315F', 'wi'), 
              )
    
    # Ask if the user wants to answer the Questions in a randomized order or 
    # not
    randFlag = input('Would you like to scramble the Questions? (y/n): ')
   
    # Randomize the Questions if requested
    if randFlag == 'y':
        objects = list(objects)
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