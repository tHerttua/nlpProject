import os
import dailyParser.dailyMailparser as dp

parser = dp.DailyMailParser()

with open("URLS.txt", "r") as f:
    URLS = f.read()

URLlist = URLS.strip().split()

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