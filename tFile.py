import operator
import sys

listOfWordsAndSigs = []

for line in open('words'):
	lineStripped = (line.rstrip()).lower()
	listOfWordsAndSigs.append([''.join(sorted(lineStripped)), lineStripped])

sortedList = sorted(listOfWordsAndSigs, key=operator.itemgetter(0))
finalWords = []

for x in sortedList:
	if sortedList.count(x[0]) > 1:
		finalWords.append(x)

prevSig = ['']

for item in finalWords:
	if prevSig[0] != item[0]:
		print('\n')
		sys.stdout.write(item[1] + ' ')
	else:
		sys.stdout.write(item[1] + ' ')
	prevSig = item[0]
