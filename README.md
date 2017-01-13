# Q-A-learner
Python script to practise giving correct translations or correct answers to questions. Somewhat like flash cards. 

## Description
This script will ask you to give the correct translation of a letter/word/sentence or a correct answer to a question. It was initially created to learn the Korean alphabet - the Jamo characters. In a future version, Questions and Answers may be imported from an external file, but for now they have to be defined inside this script. Questions can be scrambled before rehearsal, and the user can specify if he/she wants to start over if a mistaske is made. The user's terminal should support Unicode characters.

## How to use
In the code, replace the tuples inside the 'objects' tuple with Questions and Answers of your own. Each Q/A couple is defined as a tuple in the format ('Question', 'Answer'). Upon execution, the user will be asked if he/she wants to answer the Questions in a randomized order or not. The user will also be asked if he/she wants to start all over from the beginning if an incorrect Answer was given. This does preserve the order in which the Questions were asked. If the user specifies 'No' ('n') to this question, he/she can try multiple times to answer a Question correctly. 

## To do:
- [ ] Make it possible to load Questions and Answers from an external file
- [ ] Make it possible to have multiple valid Answers to a Question; the program could ask for all correct Answers
- [ ] Create statistics to keep account of Questions that appear to be harder/easier to answer
- [ ] Check if the Unicode characters are correctly displayed
- [ ] Make a GUI/web interface 
