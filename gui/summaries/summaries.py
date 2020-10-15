from pytldr.summarize import TextRankSummarizer
from pytldr.summarize import LsaSummarizer
from pytldr.summarize import RelevanceSummarizer

def textRank(filepath, text):
    TextRankSummarizer = TextRankSummarizer()
    summary_TextRank = TextRankSummarizer.summarize(text, length=5)
    return summary_TextRank

def LSA(filepath):
    LSASummarizer = LsaSummarizer()
    summary_LSA = LSASummarizer.summarize(text, topics=4, length=5, binary_matrix=True, topic_sigma_threshold=0.5)
    return summary_LSA

def relevance(filepath):
    RelevanceSummarizer = RelevanceSummarizer()
    summary_relevance = RelevanceSummarizer.summarize(text, length=5, binary_matrix=True)
    return summary_relevance
