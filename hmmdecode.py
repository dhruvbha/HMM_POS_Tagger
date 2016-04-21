import sys
import pickle
import re

inputFile = open(sys.argv[1], 'r')
outputFile = open('hmmoutput.txt', 'w')

with open('hmmmodel.txt', 'r') as file:
	wordCount, transitionProbability, emissionProbability = pickle.load(file)
startTag = 'start'
probability = -1
maxProbability = 0
maxProbabilityTag = 'NC'

for lines in inputFile:

	sentence = lines.rstrip('\n')
	words = sentence.split(" ")
	for testWord in words:
		if testWord in wordCount:
			for probableTag in emissionProbability[testWord]:
					actualTransitionProbability = emissionProbability[testWord][probableTag]
					if probableTag in emissionProbability[testWord]:
						probability = actualTransitionProbability * emissionProbability[testWord][probableTag]

					if probability > maxProbability:
						maxProbability = probability
						maxProbabilityTag = probableTag
			outputFile.write(testWord + '/' + maxProbabilityTag + " ")
			startTag = maxProbabilityTag
			maxProbability = 0
			maxProbabilityTag = 'NC'
			probability = -1

		else:
			if re.match(r'.*[A-Z].*', testWord):
				outputFile.write(testWord + '/' + 'NP' + " ")
				startTag = "NP"
			elif re.match(r'.*[0-9].*', testWord):
				outputFile.write(testWord + '/' + 'ZZ' + " ")
				startTag = "ZZ"
			elif re.match(r'.*[,.()%].*', testWord):
				outputFile.write(testWord + '/' + 'FF' + " ")
				startTag = "FF"
			else:
				outputFile.write(testWord + '/' + 'NC' + " ")
				startTag = "NC"

            # if :
				# print 'asd'
            # else:
				# outputFile.write(testWord + '/' + 'NC' + " ")
				# startTag = 'NC'
	outputFile.write('\n')
outputFile.close()
#/Users/dhruvbhatia/Documents/HMM_POS_Tagger/hw6-dev-train/catalan_corpus_dev_raw.txt
