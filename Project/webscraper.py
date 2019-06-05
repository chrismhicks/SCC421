import xlrd
import json

from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

language = "english"
sentence_count = 4

# File holding the URLs to summarise
URLFile = "./Data/dataGathering/URLsOfInterest.xlsx"
# List of the URLs that are to be summarized
URLList = []
# JSON file location
dataFileJSON = "./Data/dataGathering/rawData.json"

# Load data from the crawlerFile
URLWorkbook = xlrd.open_workbook(URLFile)
URLSheet = URLWorkbook.sheet_by_index(0)
for index in range(1, URLSheet.nrows):
    URLList.append(URLSheet.cell_value(index, 1))

if __name__ == "__main__":
    for url in URLList:

        tempSentenceList = []
        try:
            parser = HtmlParser.from_url(url, Tokenizer(language))
            stemmer = Stemmer(language)
            summazier = Summarizer(stemmer)
            summazier.stop_words = get_stop_words(language)

            for sentence in summazier(parser.document, sentence_count):
                tempSentenceList.append(str(sentence))

            rawData = {}
            rawData["Data"] = []

            rawData["Data"].append({
                "URL": url,
                "Summary": tempSentenceList
            })

            print(rawData)

        except Exception as e:
            print("Failed to load: " + url)

        with open(dataFileJSON, "a") as appendJSON:
            json.dump(rawData, appendJSON)
            appendJSON.write("\n")



