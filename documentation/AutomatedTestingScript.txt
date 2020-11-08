from pytldr.summarize.lsa import LsaOzsoy, LsaSteinberger
from pytldr.summarize.relevance import RelevanceSummarizer
from pytldr.summarize.textrank import TextRankSummarizer
from NamedEntitySummarizer import NERSummarizer
from RougeEvaluation import RougeEvaluation
import dailyMailparser as dp
from textblob import TextBlob
from datetime import datetime
import time

parser = dp.DailyMailParser()
lsa_o = LsaOzsoy()
lsa_s = LsaSteinberger()
relevance = RelevanceSummarizer()
textrank = TextRankSummarizer()
ner = NERSummarizer()
rougeval = RougeEvaluation()

#Open the file containing the links to the articles
linkfile = open("linkList.txt", "r")

#Create a file that's used for gathering the test data used for statistics
#Add a first row with the headers for the data points
#The file is a csv-file with semicolon used as a delimiter
statsfile = open("Stats-" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv", "w")
statsfile.write("article_retrieved;article_word_amount;reference_word_amount;LSA_O_word_amount;LSA_O_execution_time;LSA_S_word_amount;LSA_S_execution_time;Relevance_word_amount;Relevance_execution_time;TextRank_word_amount;TextRank_execution_time;NER-summary_word_amount;NER_execution_time;LSA_O_ROUGE2-recall;LSA_O_ROUGE2-precision;LSA_O_ROUGE3-recall;LSA_O_ROUGE3-precision;LSA_S_ROUGE2-recall;LSA_S_ROUGE2-precision;LSA_S_ROUGE3-recall;LSA_S_ROUGE3-precision;Relevance_ROUGE2-recall;Relevance_ROUGE2-precision;Relevance_ROUGE3-recall;Relevance_ROUGE3-precision;TextRank_ROUGE2-recall;TextRank_ROUGE2-precision;TextRank_ROUGE3-recall;TextRank_ROUGE3-precision;NER-summary_ROUGE2-recall;NER-summary_ROUGE2-precision;NER-summary_ROUGE3-recall;NER-summary_ROUGE3-precision\n")

#Start processing all the links in the link file
#The links are all on their own rows in the file
url_link = linkfile.readline()
while url_link:
    #Print the URL and the time, so that the log can be referred to later if there is an issue with the processing
    #Time and date are also printed into the data file
    print(url_link)
    parser.openURL(url_link)
    print(datetime.now())
    statsfile.write(str(datetime.now()))
    statsfile.write(";")

    #Use the parser to get the content from the article
    #The document is split into the content (document text) and the reference text (bullet points in the article)
    #The text count of the article and the reference text are stored in the data file
    article = parser.findContent()
    textCount = TextBlob(str(article)).ngrams(n=1)
    statsfile.write(str(len(textCount)))
    statsfile.write(";")

    facets = parser.findFacets()
    reference_text = []
    for facet in facets:
        reference_text.append(facet.replace("\xa0",""))

    textCount = TextBlob(str(reference_text)).ngrams(n=1)
    statsfile.write(str(len(textCount)))
    statsfile.write(";")

    #Use all five different summarizers and calculate the time it took for them to process the article
    #The word count and the processing time are stored on the data file
    start_time = time.perf_counter()
    lsa_o_summary = lsa_o.summarize(article.replace("\xa0"," "), length=len(reference_text))
    end_time = time.perf_counter()
    time_diff = (end_time - start_time)
    textCount = TextBlob(str(lsa_o_summary)).ngrams(n=1)
    statsfile.write(str(len(textCount)))
    statsfile.write(";")
    statsfile.write(str(time_diff))
    statsfile.write(";")

    start_time = time.perf_counter()
    lsa_s_summary = lsa_s.summarize(article.replace("\xa0"," "), length=len(reference_text))
    end_time = time.perf_counter()
    time_diff = (end_time - start_time)
    textCount = TextBlob(str(lsa_s_summary)).ngrams(n=1)
    statsfile.write(str(len(textCount)))
    statsfile.write(";")
    statsfile.write(str(time_diff))
    statsfile.write(";")

    start_time = time.perf_counter()
    relevance_summary = relevance.summarize(article.replace("\xa0"," "), length=len(reference_text))
    end_time = time.perf_counter()
    time_diff = (end_time - start_time)
    textCount = TextBlob(str(relevance_summary)).ngrams(n=1)
    statsfile.write(str(len(textCount)))
    statsfile.write(";")
    statsfile.write(str(time_diff))
    statsfile.write(";")

    start_time = time.perf_counter()
    textrank_summary = textrank.summarize(article.replace("\xa0"," "), length=len(reference_text))
    end_time = time.perf_counter()
    time_diff = (end_time - start_time)
    textCount = TextBlob(str(textrank_summary)).ngrams(n=1)
    statsfile.write(str(len(textCount)))
    statsfile.write(";")
    statsfile.write(str(time_diff))
    statsfile.write(";")

    start_time = time.perf_counter()
    ner_summary = ner.Named_Entity_Summary(article.replace("\xa0"," "), len(reference_text))
    end_time = time.perf_counter()
    time_diff = (end_time - start_time)
    textCount = TextBlob(str(ner_summary)).ngrams(n=1)
    statsfile.write(str(len(textCount)))
    statsfile.write(";")
    statsfile.write(str(time_diff))
    statsfile.write(";")

    #Summaries are then run through the Rouge-N evaluation
    #The results for Rouge-2 Recall, Rouge-2 Precision, Rouge-3 Recall and Rouge-3 Precision are stored in the data file
    lsa_o_rouge = rougeval.rouge_evaluations(str(lsa_o_summary), str(reference_text))
    statsfile.write(lsa_o_rouge[0])
    statsfile.write(";")
    statsfile.write(lsa_o_rouge[1])
    statsfile.write(";")
    statsfile.write(lsa_o_rouge[2])
    statsfile.write(";")
    statsfile.write(lsa_o_rouge[3])
    statsfile.write(";")

    lsa_s_rouge = rougeval.rouge_evaluations(str(lsa_s_summary), str(reference_text))
    statsfile.write(lsa_s_rouge[0])
    statsfile.write(";")
    statsfile.write(lsa_s_rouge[1])
    statsfile.write(";")
    statsfile.write(lsa_s_rouge[2])
    statsfile.write(";")
    statsfile.write(lsa_s_rouge[3])
    statsfile.write(";")

    relevance_rouge = rougeval.rouge_evaluations(str(relevance_summary), str(reference_text))
    statsfile.write(relevance_rouge[0])
    statsfile.write(";")
    statsfile.write(relevance_rouge[1])
    statsfile.write(";")
    statsfile.write(relevance_rouge[2])
    statsfile.write(";")
    statsfile.write(relevance_rouge[3])
    statsfile.write(";")

    textrank_rouge = rougeval.rouge_evaluations(str(textrank_summary), str(reference_text))
    statsfile.write(textrank_rouge[0])
    statsfile.write(";")
    statsfile.write(textrank_rouge[1])
    statsfile.write(";")
    statsfile.write(textrank_rouge[2])
    statsfile.write(";")
    statsfile.write(textrank_rouge[3])
    statsfile.write(";")

    ner_rouge = rougeval.rouge_evaluations(str(ner_summary), str(reference_text))
    statsfile.write(ner_rouge[0])
    statsfile.write(";")
    statsfile.write(ner_rouge[1])
    statsfile.write(";")
    statsfile.write(ner_rouge[2])
    statsfile.write(";")
    statsfile.write(ner_rouge[3])

    #Start a new row in the data file and read the next link from the link list
    statsfile.write("\n")

    url_link = linkfile.readline()

#Close the used files
linkfile.close()
statsfile.close()