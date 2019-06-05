import xlrd
import openpyxl

from openpyxl import Workbook
import os

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider

# Location of file which holds information required to crawl webpages
crawlerFile = "./Data/dataGathering/crawlingInformation.xlsx"
# List of URLs already found from previous crawls
foundURLsFile = "./Data/dataGathering/URLsOfInterest.xlsx"
# File to save crawls to, appends to end of existing or creates new file
saveFileName = "./Data/dataGathering/URLsOfInterest.xlsx"

# The URL that the crawler will start from
# The domain the crawler must stay within
# The domain that must exist in the URL in order to save it
startURLs, allowedDomains, mustIncludeDomains = [], [], []
# A list of URLs already in the file
existingURLs = []

# Load data from the crawlerFile
openCrawlList = xlrd.open_workbook(crawlerFile)
crawlSheet = openCrawlList.sheet_by_index(0)
for index in range(1, crawlSheet.nrows):
    startURLs.append(crawlSheet.cell_value(index, 0))
    allowedDomains.append(crawlSheet.cell_value(index, 1))
    mustIncludeDomains.append(crawlSheet.cell_value(index, 2))

# Check to see if the file with existing URLs exists already
# If not, then create it with the necessary columns
if (os.path.exists(foundURLsFile)):
    foundURLs = xlrd.open_workbook(foundURLsFile)
    usedSheet = foundURLs.sheet_by_index(0)
    for urlIndex in range(1, usedSheet.nrows):
        existingURLs.append(usedSheet.cell_value(urlIndex, 1))
else:
    book = Workbook()
    sheet = book.active
    sheet["A1"], sheet["B1"] = "Domain", "URL"
    book.save(saveFileName)

bookToSave = openpyxl.load_workbook(saveFileName)
sheetToSave = bookToSave.active

print(existingURLs)
# Create spider using scrapy
class Spider(CrawlSpider):
    name = "Spider"

    start_urls = startURLs
    allowedDomains = allowedDomains

    def parse(self, response):
        le = LinkExtractor()
        for link in le.extract_links(response):
            for domain in mustIncludeDomains:
                if(domain in link.url):
                    if not(link.url in existingURLs):
                        print(link.url)
                        sheetToSave.append((domain, link.url))
                        bookToSave.save(saveFileName)
