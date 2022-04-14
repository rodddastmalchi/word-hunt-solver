from random import randint
from numpy.random import choice

class Alphabet:
    consonant = 'bcdfghjklmnpqrstvwxyz'
    vowel = 'aeiou'
    pConsonant = 0.3
    pVowel = 0.7
    def __init__(self) -> None:
        pass
    
    def randomLetter():

        probs = [Alphabet.pConsonant, Alphabet.pVowel]

        randInd = choice(range(len(probs)), p=probs)
        if randInd == 1:
            return Alphabet.consonant[randint(0, len(Alphabet.consonant)-1)]
        return Alphabet.vowel[randint(0, len(Alphabet.vowel)-1)]