import nltk

nltk.download('abc')

nltk.corpus.abc.words()



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
print(delete)