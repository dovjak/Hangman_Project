# Hangman Project

This project simulates 'Hangman' game by iteratively asking a player for a letter, checking if a letter is valid and existing in a randomly picked word. Written in Python using Visual Studio Code.

## Milestone 1

Completed the ask_letter method. The user is asked to insert a letter and the method checks if a letter is valid in terms of if it is only 1 character, if it a valid letter and if the letter has not been tried in this game session before. If the letter passes the check, the following method of check_letter is called.

'''python
def ask_letter(self):
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
'''

## Milestone 2

Using Object Oriented Programming (OOP) the attributes were intialised. OOP was chosen to due to a number of variables to be updated repeatedly.

'''python
def __init__(self, word_guessed, num_lives=5):
        self.word_list=word_list
        self.num_lives=num_lives
        self.word=random.choice(word_list)
        
        print(f'The mystery word has {len(self.word)} characters')
        
        self.word_guessed=list('_'*len(self.word))
        self.num_letter=len(self.word)
        
        print(f'{self.word_guessed}')

        self.list_letters=[]
'''python

## Milestone 3

Completed a check_letter method. It checks if the letter guessed by the user is in the word, if not reduces the number of lives left and adds a drawing of a hangman.

'''python
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
'''

