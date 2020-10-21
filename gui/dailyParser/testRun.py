
"""
FUNCTIONS DEMONSTRATION
"""

import dailyMailparser as dp

parser = dp.DailyMailParser()

#OpenUrl works only with the daily mail articles and has only been tested with the links provided in the dataset
#parser.openURL('http://web.archive.org/web/20150731153506id_/http://www.dailymail.co.uk/news/article-3055646/Did-exaggerated-records-make-global-warming-look-worse-Scientists-investigate-adjusted-temperatures-skewed-data.html')
parser.openURL('http://web.archive.org/web/20150603183746id_/http://www.dailymail.co.uk/sciencetech/article-3060883/Hackers-MEDICAL-equipment-Security-experts-discover-telesurgery-robots-risk-cyber-attacks.html')
#parser.openURL('http://web.archive.org/web/20150409081411id_/http://www.dailymail.co.uk/sport/boxing/article-3023768/Jack-Johnson-100-years-story-race-hate-fight-split-America.html')
#parser.openURL('http://web.archive.org/web/20150423100224id_/http://www.dailymail.co.uk/sport/football/article-3049659/Former-Premier-League-referee-Mark-Halsey-says-decision-overlook-Mark-Clattenburg-FA-Cup-final-joke.html')
#parser.openURL('http://web.archive.org/web/20150401162709id_/http://www.dailymail.co.uk/sport/football/article-3021359/Scotland-s-Euro-2016-qualifier-Georgia-place-closed-doors-following-pitch-invasions-Tbilisi.html')

#Title can be extracted easily with beautiful soup built-in method:
print("\n")
print("TITLE")
print(parser.soup.title.text)
print("\n")

#Note that the object returned is list of bullet points
print("BULLET POINTS")
facets = parser.find_facets()
print("\n")
for facet in facets:
    print(facet)
    print("\n")

#Note that the contents of the article is one string object
print("ARTICLE")
article = parser.find_content()
print(article)