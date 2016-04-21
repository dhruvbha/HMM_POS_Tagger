import sys
from collections import defaultdict
import pickle

# def writeOutput():
#     output = open("hmmmodel.txt","w")
#     for word,listOfTags in transitionProbability.iteritems():
#         for posTag,probability in listOfTags.iteritems():
#             if len(word) > 0:
#                 output.writelines(word+" "+posTag+" "+str(probability)+"\n")
#                 output.writelines('\n')
#     for word,listOfTags in emissionProbability.iteritems():
#         for posTag,probability in listOfTags.iteritems():
#             if len(word) > 0:
#                 output.writelines(word+" "+posTag+" "+str(probability)+"\n")


allPOSForWord = defaultdict(list)
wordCount = {}
posCount = {}
transitionProbabilityCount = defaultdict(list)
transitionProbability = defaultdict(dict)
emissionProbability = defaultdict(dict)


trainingData = open(sys.argv[1], 'r')
for data in trainingData:

    startPOS = 'start'
    if startPOS in posCount:
        posCount[startPOS] += 1
    else:
        posCount[startPOS] = 1

    if data.strip():
        list1 = data.split(" ")
        for element in list1:
            index = element.rfind('/')
            word = element[:index]
            pos = element[index+1:].strip()
            allPOSForWord[word].append(pos)
            if word not in wordCount:
                wordCount[word] = 1
            else:
                wordCount[word] += 1
            if pos not in posCount:
                posCount[pos] = 1
            else:
                posCount[pos] +=1

            transitionProbabilityCount[startPOS].append(pos)
            startPOS = pos

for tag in transitionProbabilityCount:
    for tag1 in set(transitionProbabilityCount[tag]):
        transitionProbability[tag][tag1] = float(transitionProbabilityCount[tag].count(tag1)+1)/float(posCount[tag])

for word in allPOSForWord:
      for tagUsed in set(allPOSForWord[word]):
              if allPOSForWord[word].count(tagUsed) != 0:
                      emissionProbability[word][tagUsed] = float(allPOSForWord[word].count(tagUsed))/float(wordCount[word])

with open('hmmmodel.txt', 'w') as file:
    pickle.dump([wordCount,transitionProbability, emissionProbability],file)
#writeOutput()
