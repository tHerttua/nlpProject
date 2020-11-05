import os
import dailyParser.dailyMailparser as dp

parser = dp.DailyMailParser()

articles = []
dailyArticles = []

with open ('all_test.txt', 'r') as f:
    articles = f.read()
articlelist = articles.strip().split()

for article in articlelist:
    if "dailymail" in article:
        dailyArticles.append(article)

parser.openURL(dailyArticles[0])
initial = parser.findContent()
minAndMax = [initial, initial]
longestShortest = [dailyArticles[0], dailyArticles[0]]

for dailyA in dailyArticles:
    parser.openURL(dailyA)
    content = parser.findContent()
    if len(content) > len(minAndMax[0]):
        minAndMax[0] = content
        longestShortest[0] = dailyA
    if len(content) < len(minAndMax[1]):
        minAndMax[1] = content
        longestShortest[1] = dailyA

with open("longestShortest.txt", 'w+') as o:
    for entry in longestShortest:
        o.write(entry)
        
