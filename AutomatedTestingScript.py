from pytldr.summarize.lsa import LsaOzsoy, LsaSteinberger
from pytldr.summarize.relevance import RelevanceSummarizer
from pytldr.summarize.textrank import TextRankSummarizer
from NamedEntitySummarizer import NERSummarizer
from RougeEvaluation import RougeEvaluation
import dailyMailparser as dp
from textblob import TextBlob
from datetime import datetime

parser = dp.DailyMailParser()

lsa_o = LsaOzsoy()
lsa_s = LsaSteinberger()
relevance = RelevanceSummarizer()
textrank = TextRankSummarizer()

ner = NERSummarizer()

rougeval = RougeEvaluation()

#Avataan tiedosto, missä listä URLeja
linkfile = open("linkList.txt", "r")
statsfile = open("statistics.txt", "w")

statsfile.write("article_retrieved;article_word_amount;reference_word_amount;LSA_O_word_amount;LSA_S_word_amount;Relevance_word_amount;TextRank_word_amount;NER-summary_word_amount;LSA_O_ROUGE2-recall;LSA_O_ROUGE2-precision;LSA_O_ROUGE3-recall;LSA_O_ROUGE3-precision;LSA_S_ROUGE2-recall;LSA_S_ROUGE2-precision;LSA_S_ROUGE3-recall;LSA_S_ROUGE3-precision;Relevance_ROUGE2-recall;Relevance_ROUGE2-precision;Relevance_ROUGE3-recall;Relevance_ROUGE3-precision;TextRank_ROUGE2-recall;TextRank_ROUGE2-precision;TextRank_ROUGE3-recall;TextRank_ROUGE3-precision;NER-summary_ROUGE2-recall;NER-summary_ROUGE2-precision;NER-summary_ROUGE3-recall;NER-summary_ROUGE3-precision\n")

#Käydään listä rivi riviltä läpi ja tehdään seuraavat tehtävät:
url_link = linkfile.readline()
while url_link:
    print(url_link)
    #Avataan linkki
    parser.openURL(url_link)
    print(datetime.now())
    statsfile.write(str(datetime.now()))
    statsfile.write(";")

    #Eritellään alkuperäinen teksti, mitä käytetään summarien luomiseen
    article = parser.findContent()

    textCount = TextBlob(str(article)).ngrams(n=1)
    statsfile.write(str(len(textCount)))
    statsfile.write(";")

    #Eritellään bullet pointit erikseen ja luodaan niistä reference text array (näin saadaan tietoon myös lauseiden määrä)
    facets = parser.findFacets()
    reference_text = []
    for facet in facets:
        reference_text.append(facet)

    textCount = TextBlob(str(reference_text)).ngrams(n=1)
    statsfile.write(str(len(textCount)))
    statsfile.write(";")


    #Lähetetään alkuperäinen teksti PyTLDR ja NamedEntitySummarizer scripteille ja tallennetaan palautetut summaryt muistiin.
    lsa_o_summary = lsa_o.summarize(article.replace("\xa0"," "), length=len(reference_text))
    #print("LSA_O: " + str(lsa_o_summary))
    textCount = TextBlob(str(lsa_o_summary)).ngrams(n=1)
    statsfile.write(str(len(textCount)))
    statsfile.write(";")

    lsa_s_summary = lsa_s.summarize(article.replace("\xa0"," "), length=len(reference_text))
    #print("LSA_S: " + str(lsa_s_summary))
    textCount = TextBlob(str(lsa_s_summary)).ngrams(n=1)
    statsfile.write(str(len(textCount)))
    statsfile.write(";")

    relevance_summary = relevance.summarize(article.replace("\xa0"," "), length=len(reference_text))
    #print("Relevance: " + str(relevance_summary))
    textCount = TextBlob(str(relevance_summary)).ngrams(n=1)
    statsfile.write(str(len(textCount)))
    statsfile.write(";")

    textrank_summary = textrank.summarize(article.replace("\xa0"," "), length=len(reference_text))
    #print("Textrank: " + str(textrank_summary))
    textCount = TextBlob(str(textrank_summary)).ngrams(n=1)
    statsfile.write(str(len(textCount)))
    statsfile.write(";")

    ner_summary = ner.Named_Entity_Summary(article.replace("\xa0"," "), len(reference_text))
    #print("Named Entity: " + str(ner_summary))
    textCount = TextBlob(str(ner_summary)).ngrams(n=1)
    statsfile.write(str(len(textCount)))
    statsfile.write(";")

    #Lähetetään summaryt ja bullet point reference teksti ROUGE-evaluointi -scriptille ja tallennetaan saatu tieto tekstitiedostoon
    lsa_o_rouge = rougeval.rouge_evaluations(str(lsa_o_summary), str(reference_text))
    #print(lsa_o_rouge)
    statsfile.write(lsa_o_rouge[0])
    statsfile.write(";")
    statsfile.write(lsa_o_rouge[1])
    statsfile.write(";")
    statsfile.write(lsa_o_rouge[2])
    statsfile.write(";")
    statsfile.write(lsa_o_rouge[3])
    statsfile.write(";")

    lsa_s_rouge = rougeval.rouge_evaluations(str(lsa_s_summary), str(reference_text))
    #print(lsa_s_rouge)
    statsfile.write(lsa_s_rouge[0])
    statsfile.write(";")
    statsfile.write(lsa_s_rouge[1])
    statsfile.write(";")
    statsfile.write(lsa_s_rouge[2])
    statsfile.write(";")
    statsfile.write(lsa_s_rouge[3])
    statsfile.write(";")

    relevance_rouge = rougeval.rouge_evaluations(str(relevance_summary), str(reference_text))
    #print(relevance_rouge)
    statsfile.write(relevance_rouge[0])
    statsfile.write(";")
    statsfile.write(relevance_rouge[1])
    statsfile.write(";")
    statsfile.write(relevance_rouge[2])
    statsfile.write(";")
    statsfile.write(relevance_rouge[3])
    statsfile.write(";")

    textrank_rouge = rougeval.rouge_evaluations(str(textrank_summary), str(reference_text))
    #print(textrank_rouge)
    statsfile.write(textrank_rouge[0])
    statsfile.write(";")
    statsfile.write(textrank_rouge[1])
    statsfile.write(";")
    statsfile.write(textrank_rouge[2])
    statsfile.write(";")
    statsfile.write(textrank_rouge[3])
    statsfile.write(";")

    ner_rouge = rougeval.rouge_evaluations(str(ner_summary), str(reference_text))
    #print(ner_rouge)
    statsfile.write(ner_rouge[0])
    statsfile.write(";")
    statsfile.write(ner_rouge[1])
    statsfile.write(";")
    statsfile.write(ner_rouge[2])
    statsfile.write(";")
    statsfile.write(ner_rouge[3])


    statsfile.write("\n")

    #Luetaan seuraava rivi
    url_link = linkfile.readline()

#Suljetaan linkkilista-tiedosto
linkfile.close()
statsfile.close()