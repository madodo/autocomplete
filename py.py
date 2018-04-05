import nltk
import random

nltk.download('abc')

nltk.corpus.abc.words()

print(' ')
AllTheCounts = {}
delete = 0
for i in nltk.corpus.abc.words():
    if i in AllTheCounts.keys():
        AllTheCounts[i] += 1
    else:
        AllTheCounts[i] = 1
for f in AllTheCounts:
    if int(AllTheCounts[f]) > delete:
        delete = AllTheCounts[f]
print('the most common word in the text is:')
print(AllTheCounts.get(delete))
print('it occurs:')
print(delete)
print('times')
print('  ')

nextwords = []
def look():
    word = input('pick a word')
    place1 = 0
    for i,f in enumerate(nltk.corpus.abc.words()):
        if f == word:
            nextwords.append(nltk.corpus.abc.words()[i+1])
    print(word)
    auto = random.choice(nextwords)
    print(auto)
    word = auto
look()
look()
look()
look()
look()
look()
