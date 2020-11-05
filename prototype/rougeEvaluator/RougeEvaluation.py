from textblob import TextBlob #Textblob is used for creating bigrams and trigrams
import re
from memory_profiler import profile

class RougeEvaluation():

    def __init__(self):
        pass

    #N-grams are created from the given (human created) reference text. Those N-grams are then searched from the summary.
    #The function returns the amount of N-grams and the amount of words in the summary text.
    @profile
    def ngram_creation_and_counting(self, reference_text, summary_text, grams):
        #Create tuple lists of the reference text and the summary
        ngram_referencetuples = TextBlob(reference_text).ngrams(grams)
        ngram_summarytuples = TextBlob(summary_text).ngrams(grams)

        summary_counter = 0
        match_counter = 0

        #Loop through all the tuples in the reference wordlist and compare them to the tuples in the summary tuples wordlist
        for _ in ngram_summarytuples:
            reference_counter = 0
            for __ in ngram_referencetuples:
                if ngram_referencetuples[reference_counter].lower() == ngram_summarytuples[summary_counter].lower():
                    match_counter = match_counter + 1
                    #print(match_counter)
                reference_counter = reference_counter + 1
                #print("reference counter: " + str(reference_counter))
            summary_counter = summary_counter + 1
            #print("summary counter: " + str(summary_counter))


        ngram_count = len(ngram_referencetuples)
        #print("Number of matches: " + str(match_counter))
        #print("Number of N-grams: " + str(ngram_count))

        return match_counter, ngram_count

    #Rouge recall is calculated based on the matches and the bigram count and returned
    @profile
    def rouge_recall(self, match_amount, ngram_amount):
        recall = match_amount / ngram_amount
        return str(recall)

    #Rouge precision is calculated and returned
    @profile
    def rouge_precision(self, match_amount, text_word_amount):
        precision = match_amount / text_word_amount
        return str(precision)

    @profile
    def rouge_evaluations(self, summary,reference):
        rouge2results = self.ngram_creation_and_counting(reference,summary,2)
        rouge3results = self.ngram_creation_and_counting(reference,summary,3)
        summary_wordcount = TextBlob(summary)
        rouge2recall = self.rouge_recall(rouge2results[0],rouge2results[1])
        rouge2precision = self.rouge_precision(rouge2results[0],len(summary_wordcount.words))
        rouge3recall = self.rouge_recall(rouge3results[0],rouge3results[1])
        rouge3precision = self.rouge_precision(rouge3results[0],len(summary_wordcount.words))

        return rouge2recall,rouge2precision,rouge3recall,rouge3precision