import spacy 
from textblob import TextBlob 
import numpy
import re

# Load and install the trained model for English language
nlp = spacy.load("en_core_web_sm")

class NERSummarizer():

    def __init__(self):
        pass

    def list_named_entities(self, document_text):
        """
        Finds all the named entities for organizations and persons from the article text.
        Creates and populates a list for the named entities with ORG or PERSON label.
        """
        doc = nlp(document_text)
        entity_list = []
        for ent in doc.ents:
            if ent.label_ == "ORG" or ent.label_ == "PERSON":
                entity_list.append(ent.text)
        return entity_list

    def original_text_sentences(self, original_text):
        """
        Splits the article text into sentences
        """
        textblob = TextBlob(original_text)
        sentence_list = []
        for sentence in textblob.sentences:
            sentence_list.append(sentence)
        return sentence_list

    def sentence_named_entities(self, sentence_text, named_entity):
        """
        Finds the amount of times a named entity appears in a sentence
        """
        times_found = len(re.findall(named_entity, str(sentence_text)))
        return times_found

    def NER_scoring_for_sentence(self, sentence, NE_list):
        """
        Scores each sentence in a list
        """
        NER_score = 0
        for NE in NE_list:
            NER_score = NER_score + self.sentence_named_entities(sentence, NE)
        return NER_score

    def NER_scoring(self, sentence_list,NE_list):
        """
        Creates a list of all the named entity scores.
        The list correspondent to list of all sentences.
        """
        NER_scores = []
        for sentence in sentence_list:
            NER_scores.append(self.NER_scoring_for_sentence(sentence,NE_list))
        return NER_scores

    def highest_NER_scores(self, score_list, score_amount):
        """
        Sorts the score list by highest score in descending order and stores the index in a list.
        Produces the amount of scores that were requested.
        If there are more scores requested than there are sentences, the return value is maxed at the amount of sentences
        """
        s = numpy.array(score_list)
        sorted_index_list = numpy.argsort(s)[::-1]
        return_list = []
        if score_amount > len(sorted_index_list):
            score_amount = len(sorted_index_list)
        for i in range(0,score_amount):
            return_list.append(sorted_index_list[i])
        return return_list

    def NER_summary(self, sentence_list,score_list):
        """
        Sort the highest scored sentences to the original order as they appear in the article
        """
        sorted_score_list = numpy.sort(score_list)
        NER_summary = []
        for i in sorted_score_list:
            NER_summary.append(str(sentence_list[i]))
        return NER_summary

    def Named_Entity_Summary(self, article, length):
        """
        Handles the summarization using all the methods and procudes the named entity summary
        """
        sentences = self.original_text_sentences(article)
        sentence_score_list = self.NER_scoring(sentences, self.list_named_entities(article))
        summary = self.NER_summary(sentences, self.highest_NER_scores(sentence_score_list, length))
        return summary
