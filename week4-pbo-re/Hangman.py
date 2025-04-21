import random

class Hangman:
    def __init__(self):
        self.words = ['algorithm', 'binary', 'boolean', 'byte', 'cache', 'compiler', 'debugger',
                    'encryption', 'framework', 'function', 'garbage', 'hash', 'index', 'iterator',
                    'javascript', 'json', 'library', 'loop', 'namespace', 'object', 'operator',
                    'overload', 'polymorphism', 'queue', 'recursion', 'serialization', 'stack',
                    'template', 'variable', 'virtual', 'web', 'xml', 'yaml', 'zip']
        
        self.stages = ["""
            ------
            |    |
            |
            |
            |
            |
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |
            |
            |
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |    |
            |    |
            |
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |    |
            |    |
            |   /
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |    |
            |    |
            |   / \\
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |  --|
            |    |
            |   / \\
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |  --|--
            |    |
            |   / \\
            |
        ------------
        """]
        self.attempts = 0
    
    def start(self):
        word = random.choice(self.words)
        guessed = '_' * len(word)
        print("Welcome to Hangman!")
        print("The word is:", guessed)
        while self.attempts < len(self.stages) - 1 and '_' in guessed:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
                continue
            
            if guess in word:
                guessed = ''.join([guess if word[i] == guess else guessed[i] for i in range(len(word))])
                print("Good guess:", guessed)
            else:
                self.attempts += 1
                print(self.stages[self.attempts])
                print("Wrong guess. Try again :", guessed)

        if '_' not in guessed:
            print("Congratulations! You've guessed the word:", word)
        else:
            print("Game Over! The word was:", word)
            print(self.stages[self.attempts])

game = Hangman()
game.start()
