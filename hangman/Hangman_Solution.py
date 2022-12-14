# %%
'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random
from turtle import position

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.
    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried
    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_guessed, num_lives=5):
        self.word_list=word_list
        self.num_lives=num_lives
        self.word=random.choice(word_list)
        
        print(f'The mystery word has {len(self.word)} characters')
        
        self.word_guessed=list('_'*len(self.word))
        self.num_letter=len(self.word)
        
        print(f'{self.word_guessed}')

        self.list_letters=[]

    def check_letter(self) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.
        Parameters:
        ----------
        letter: str
            The letter to be checked
        '''
        while self.num_lives > 0:
            inputs=self.ask_letter()
            inputs.lower()
            self.list_letters.append(inputs)
            print(self.list_letters)
            for i, l in enumerate(self.word):
                if inputs == l:
                    self.word_guessed[i] = l
                    self.num_letter -=1
                    print(f"Nice! {inputs} is in the word!")
                    print("".join(self.word_guessed))
                        
                elif inputs not in self.word:
                    print(f"Sorry, {inputs} is not in the word.")
                    #self.list_letters.append(inputs)
                    self.num_lives -= 1
                    print(f'You have {self.num_lives} lives left')
                    if self.num_lives == 4:
                        print('____')
                        print('|   |')
                        print('|    ')
                        print('|    ')
                        print('|    ')
                        print('|____')
                    if self.num_lives == 3:
                        print('____')
                        print('|   |')
                        print('|   o')
                        print('|    ')
                        print('|    ')
                        print('|____')
                    if self.num_lives == 2:
                        print('____')
                        print('|   |')
                        print('|   o')
                        print('|   |')
                        print('|    ')
                        print('|____')
                    if self.num_lives == 1:
                        print('____')
                        print('|   |')
                        print('|   o')
                        print('|  \|/')
                        print('|    ')
                        print('|____')
                    if self.num_lives == 0:
                        print(f'You ran out of lives. The word was {self.word}')
                        print('____')
                        print('|   |')
                        print('|   o')
                        print('|  \|/')
                        print('|  / \ ')
                        print('|____')
                    break
                    
        
                if '_' not in self.word_guessed:
                    print("Congratulations, you won")
                    break
                
            
    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        while True:
            letter=input('Enter a single character:')
            if len(letter)!=1:
                print('Please, enter just one character')
            elif letter.isalpha() is False:
                print('Only English letters please')
            elif letter in self.list_letters:
                print(f'{letter} was already tried, choose again')
            elif len(letter)==1:
                break
            else: print('Please enter a character')
        return letter

def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    #game.ask_letter()
    game.check_letter()
if __name__ == '__main__':
    word_list = ['apple', 'bannana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%


