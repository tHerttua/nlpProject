from pytldr.summarize import TextRankSummarizer
from pytldr.summarize import LsaSummarizer
from pytldr.summarize import RelevanceSummarizer

def textRank(text):
    TextRankSum = TextRankSummarizer()
    summary_TextRank = TextRankSum.summarize(text, length=5)
    return summary_TextRank

def LSA(text):
    LSASum = LsaSummarizer()
    summary_LSA = LSASum.summarize(text, topics=4, length=5, binary_matrix=True, topic_sigma_threshold=0.5)
    return summary_LSA

def relevance(text):
    RelevanceSum = RelevanceSummarizer()
    summary_relevance = RelevanceSum.summarize(text, length=5, binary_matrix=True)
    return summary_relevance

