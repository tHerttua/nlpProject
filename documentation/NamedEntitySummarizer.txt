import spacy #Spacy is used for named entity recognition
from textblob import TextBlob #Textblob is used for creating bigrams and trigrams
import numpy
import re

#Load the spaCy model for the English language
#The model is already trained, but needs to be downloaded and installed before it can be used
nlp = spacy.load("en_core_web_sm")

class NERSummarizer():
    #Find all the named entities for organizations and persons from the article text
    #Create an array for named entities with ORG or PERSON label, populate it and return it as a list
    def list_named_entities(document_text):
        doc = nlp(document_text)
        entity_list = []
        for ent in doc.ents:
            if ent.label_ == "ORG" or ent.label_ == "PERSON":
                entity_list.append(ent.text)
        return entity_list

    #Split the article text into sentences and return the list
    def original_text_sentences(original_text):
        textblob = TextBlob(original_text)
        sentence_list = []
        for sentence in textblob.sentences:
            sentence_list.append(sentence)
        return sentence_list

    #Find how many times a named entity appears in a sentence and return the value
    def sentence_named_entities(sentence_text, named_entity):
        times_found = len(re.findall(named_entity, str(sentence_text)))
        return times_found

    #Give a score for each sentence and return the value
    def NER_scoring_for_sentence(sentence, NE_list):
        NER_score = 0
        for NE in NE_list:
            NER_score = NER_score + NERSummarizer.sentence_named_entities(sentence, NE)
        return NER_score

    #Create a list of all the named entity scores
    #The list corresponds with the previously created list of all the sentences
    def NER_scoring(sentence_list,NE_list):
        NER_scores = []
        for sentence in sentence_list:
            NER_scores.append(NERSummarizer.NER_scoring_for_sentence(sentence,NE_list))
        return NER_scores

    #Sort the score list by highest score in descending order and store the index in a list
    #Return the amount of scores that was requested.
    #If there are more scores requested than there are sentences, then the return value is maxed at the amount of sentences
    def highest_NER_scores(score_list, score_amount):
        s = numpy.array(score_list)
        sorted_index_list = numpy.argsort(s)[::-1]
        return_list = []
        if score_amount > len(sorted_index_list):
            score_amount = len(sorted_index_list)
        for i in range(0,score_amount):
            return_list.append(sorted_index_list[i])
        return return_list

    #Sort the highest scored sentences to the original order as they appear in the article
    def NER_summary(sentence_list,score_list):
        sorted_score_list = numpy.sort(score_list)
        NER_summary = []
        for i in sorted_score_list:
            NER_summary.append(str(sentence_list[i]))
        return NER_summary

    #The function which handles the summarization by calling all the helper functions and returns the named entity summary
    def Named_Entity_Summary(self, article, length):
        sentences = NERSummarizer.original_text_sentences(article)
        sentence_score_list = NERSummarizer.NER_scoring(sentences, NERSummarizer.list_named_entities(article))
        summary = NERSummarizer.NER_summary(sentences, NERSummarizer.highest_NER_scores(sentence_score_list, length))
        return summary
