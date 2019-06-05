import json
import nltk
from nltk.tag.stanford import StanfordNERTagger
import os

#nltk.download("maxent_ne_chunker")

java_path = "C:\Program Files\Java\jre1.8.0_211\\bin\java.exe"
os.environ["JAVAHOME"] = java_path

jsonFileLocation = "./Data/dataGathering/rawData.json"

dataList = []

with open(jsonFileLocation, "r") as jsonFile:
    for line in jsonFile:
        rawData = json.loads(line)
        for sentence in rawData["Data"][0]["Summary"]:
            dataList.append(sentence)

nerModel = StanfordNERTagger("./stanford-ner-tagger/english.all.3class.distsim.crf.ser.gz", "./stanford-ner-tagger/stanford-ner-3.9.2.jar")

# Use this for Stanford NER
for sentence in dataList:
    tokenisedSentence = nltk.word_tokenize(sentence)
    print(sentence)
    print(nerModel.tag(tokenisedSentence))

# Use this for NLTK NER
#for sentence in dataList:
#    tokenizedSentence = nltk.word_tokenize(sentence)
#    for chunk in nltk.ne_chunk(nltk.pos_tag(tokenizedSentence)):
#        #print(chunk.label())
#        print(chunk)