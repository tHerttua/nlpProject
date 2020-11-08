from pytldr.summarize import TextRankSummarizer
from pytldr.summarize.lsa import LsaOzsoy, LsaSteinberger
from pytldr.summarize import RelevanceSummarizer

def textRank(text, refSentences=5):
    """
    Loads the Text rank summarizer class and procudes a summary using it
    """
    TextRankSum = TextRankSummarizer()
    summary_TextRank = TextRankSum.summarize(text, length=refSentences)
    return summary_TextRank

def LSA_O(text, refSentences=5):
    """
    Loads the LSA Ozsoy summarizer class and procudes a summary using it
    """
    LSAOSum = LsaOzsoy()
    o_summary = LSAOSum.summarize(text, topics=4, length=refSentences, binary_matrix=True, topic_sigma_threshold=0.5)
    return o_summary

def LSA_S(text, refSentences=5):
    """
    Loads the LSA Steinberg summarizer class and procudes a summary using it
    """
    LSASSum = LsaSteinberger()
    s_summary = LSASSum.summarize(text, topics=4, length=refSentences, binary_matrix=True, topic_sigma_threshold=0.5)
    return s_summary

def relevance(text, refSentences=5):
    """
    Loads the Relevance based summarizer class and procudes a summary using it
    """
    RelevanceSum = RelevanceSummarizer()
    summary_relevance = RelevanceSum.summarize(text, length=refSentences, binary_matrix=True)
    return summary_relevance

