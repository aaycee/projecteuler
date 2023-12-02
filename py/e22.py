# Akachukwu Obi
# Project Euler #22 - Names
# solved Nov 23, 2023

def wordScore(word = 'WORD'):
    """ returns word score of any given word """
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']
    word = word.upper() # convert to upper case if necessary
    score = sum([letters.index(letter) + 1 for letter in word if letter in letters])
    return score

print(wordScore('COLIN')) # 53

def nameScoreFromFile(fileName = 'e22names.txt'):
    """ returns total value of name scores from a file """
    totalScore = 0
    with open(fileName, 'r') as file:
        names = file.read() # assuming all names are in the same line
    names = [name.strip('"') for name in names.split(",")]
    names = sorted(names) # sort into alphabetical order
    namesLength = len(names)
    for i in range(namesLength):
        totalScore += wordScore(names[i])*(i+1)
    return totalScore

print(nameScoreFromFile()) # 871198282