import os
import dailyParser.dailyMailparser as dp
from memory_profiler import profile

parser = dp.DailyMailParser()

#URLS.txt must exist for this script to work:
#simply add a daily mail URL per line without other characters
#Appends to extractedOutput.txt file
with open("URLS.txt", "r") as f:
    URLS = f.read()

URLlist = URLS.strip().split()
URLlist.append("https://www.dailymail.co.uk/news/article-8911739/Georgia-QAnon-supporter-Marjorie-Taylor-Greene-elected-Congress.html")

def writeBps(BPs):
    BPstring = ""
    for BP in BPs:
        BPstring += (BP+"\n")
    return BPstring


for articleURL in URLlist:
    parser.openURL(articleURL)
    articleText = parser.findContent()
    articleBPs = parser.findFacets()
    with open('extractedOutput.txt', 'a+') as o:
        o.write(
            "-"*20 +
            "\n" +
            articleURL +
            "\n\n" +
            writeBps(articleBPs) +
            "\n\n" +
            articleText +
            "\n\n"    
        )