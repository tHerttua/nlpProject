import os
import cProfile
import pstats
import dailyParser.dailyMailparser as dp

URLS = [
            'http://web.archive.org/web/20150731153506id_/http://www.dailymail.co.uk/news/article-3055646/Did-exaggerated-records-make-global-warming-look-worse-Scientists-investigate-adjusted-temperatures-skewed-data.html',
            'http://web.archive.org/web/20150603183746id_/http://www.dailymail.co.uk/sciencetech/article-3060883/Hackers-MEDICAL-equipment-Security-experts-discover-telesurgery-robots-risk-cyber-attacks.html',
            'http://web.archive.org/web/20150409081411id_/http://www.dailymail.co.uk/sport/boxing/article-3023768/Jack-Johnson-100-years-story-race-hate-fight-split-America.html',
            'http://web.archive.org/web/20150423100224id_/http://www.dailymail.co.uk/sport/football/article-3049659/Former-Premier-League-referee-Mark-Halsey-says-decision-overlook-Mark-Clattenburg-FA-Cup-final-joke.html',
            'http://web.archive.org/web/20150401162709id_/http://www.dailymail.co.uk/sport/football/article-3021359/Scotland-s-Euro-2016-qualifier-Georgia-place-closed-doors-following-pitch-invasions-Tbilisi.html'
        ]

OUTDIR = "performanceOutputs/"
parser = dp.DailyMailParser()
    
def findContent():
    parser.findContent()

def findFacets():
    parser.findFacets()

def evaluateParserPerformance(URL, n=0):
    #Initialize
    n = str(n)
    parser.openURL(URL)

    #Run the profiler
    cProfile.run("parser.findContent()", "parserFindContentResults.dat")
    cProfile.run("findFacets()", "parserFindFacetsResults.dat")

    #Write the data for FindContent
    with open(OUTDIR+"parserFindContent_timeOutput"+n+".txt", "w") as f:
        p = pstats.Stats("parserFindContentResults.dat", stream=f)
        p.sort_stats("time").print_stats()
    with open(OUTDIR+"parserFindContent_callsOutput"+n+".txt", "w") as f:
        p = pstats.Stats("parserFindContentResults.dat", stream=f)
        p.sort_stats("calls").print_stats()
    
    with open(OUTDIR+"parserFindFacets_timeOutput"+n+".txt", "w") as f:
        p = pstats.Stats("parserFindFacetsResults.dat", stream=f)
        p.sort_stats("time").print_stats()
    with open(OUTDIR+"parserFindFacets_callsOutput"+n+".txt", "w") as f:
        p = pstats.Stats("parserFindFacetsResults.dat", stream=f)
        p.sort_stats("calls").print_stats()

    #Clean up
    os.remove("parserFindContentResults.dat")
    os.remove("parserFindFacetsResults.dat")
    
        
if __name__ == "__main__":
    evaluateParserPerformance(URLS[0])
    #n = 0
    #for URL in URLS:
    #    evaluateParserPerformance(URL, n)
    #    n += 1