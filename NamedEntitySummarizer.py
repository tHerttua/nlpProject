import spacy #Spacy is used for named entity recognition
from textblob import TextBlob #Textblob is used for creating bigrams and trigrams
import numpy
import re

# Spacy needs a model for finding named entities
nlp = spacy.load("en_core_web_sm")

class NERSummarizer():


    #Printing named entities from the given document
    def list_named_entities(document_text):
        doc = nlp(document_text)
        #Create an array for named entities with ORG or PERSON label and populate it
        entity_list = []
        for ent in doc.ents:
            if ent.label_ == "ORG" or ent.label_ == "PERSON":
                entity_list.append(ent.text)
        return entity_list

    def original_text_sentences(original_text):
        textblob = TextBlob(original_text)
        sentence_list = []
        for sentence in textblob.sentences:
            sentence_list.append(sentence)
        #print(len(sentence_list))
        return sentence_list

    def sentence_named_entities(sentence_text, named_entity):
        times_found = len(re.findall(named_entity, str(sentence_text)))
        return times_found

    def NER_scoring_for_sentence(sentence, NE_list):
        NER_score = 0
        for NE in NE_list:
            NER_score = NER_score + NERSummarizer.sentence_named_entities(sentence, NE)
        return NER_score

    def NER_scoring(sentence_list,NE_list):
        NER_scores = []
        for sentence in sentence_list:
            NER_scores.append(NERSummarizer.NER_scoring_for_sentence(sentence,NE_list))
        return NER_scores

    def highest_NER_scores(score_list, score_amount):
        s = numpy.array(score_list)
        #Sort the score list by highest score in descending order and store the index in a list
        sorted_index_list = numpy.argsort(s)[::-1]
        return_list = []
        #Return the amount that's asked in the score_amount
        if score_amount > len(sorted_index_list):
            score_amount = len(sorted_index_list)
        for i in range(0,score_amount):
            return_list.append(sorted_index_list[i])
        return return_list

    def NER_summary(sentence_list,score_list):
        #Sort the highest scored sentences to the original order as they appear in the article
        sorted_score_list = numpy.sort(score_list)
        NER_summary = []
        for i in sorted_score_list:
            NER_summary.append(str(sentence_list[i]))
        return NER_summary

    def Named_Entity_Summary(self, article, length):
        sentences = NERSummarizer.original_text_sentences(article)
        sentence_score_list = NERSummarizer.NER_scoring(sentences, NERSummarizer.list_named_entities(article))
        summary = NERSummarizer.NER_summary(sentences, NERSummarizer.highest_NER_scores(sentence_score_list, length))
        return summary

#------TESTING-----
#This section is opening a text file with a document summary and a facet that's used as a reference text
#If other summaries or reference texts are used as a source, this needs to be modified
#datafile = open("testAbstraction.txt", "r")
#
#Goes through every line in the text file and finds the points where the document text or the facet text starts
#Results for each text and their respective bigrams and trigrams are printed as they are created, searched and calculated
#for x in datafile:
#    orig_text = re.search("Original", x)
#    if (orig_text):
#        original_text = next(datafile)
#        original_text_sentences(original_text)
#
#sentence_score_list = NER_scoring(original_text_sentences(original_text), list_named_entities(original_text))
#print(sentence_score_list)
#print(highest_NER_scores(sentence_score_list, 12))
#print(NER_summary(original_text_sentences(original_text), highest_NER_scores(sentence_score_list, 5)))
#
#datafile.close()