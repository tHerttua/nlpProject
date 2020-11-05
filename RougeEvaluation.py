from textblob import TextBlob #Textblob is used for creating bigrams and trigrams
import re

class RougeEvaluation():
    #N-grams are created from the given (human created) reference text. Those N-grams are then searched from the summary.
    #The function returns the amount of N-grams and the amount of words in the summary text.
    def ngram_creation_and_counting(reference_text, summary_text, grams):
        #Create tuple lists of the reference text and the summary
        ngram_referencetuples = TextBlob(reference_text).ngrams(grams)
        ngram_summarytuples = TextBlob(summary_text).ngrams(grams);

        summary_counter = 0
        match_counter = 0

        #Loop through all the tuples in the reference wordlist and compare them to the tuples in the summary tuples wordlist
        for i in ngram_summarytuples:
            reference_counter = 0
            for j in ngram_referencetuples:
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
    def rouge_recall(match_amount, ngram_amount):
        recall = match_amount / ngram_amount
        return str(recall)

    #Rouge precision is calculated and returned
    def rouge_precision(match_amount, text_word_amount):
        precision = match_amount / text_word_amount
        return str(precision)

    def rouge_evaluations(self,summary,reference):
        rouge2results = RougeEvaluation.ngram_creation_and_counting(reference,summary,2)
        rouge3results = RougeEvaluation.ngram_creation_and_counting(reference,summary,3)
        summary_wordcount = TextBlob(summary)
        rouge2recall = RougeEvaluation.rouge_recall(rouge2results[0],rouge2results[1])
        rouge2precision = RougeEvaluation.rouge_precision(rouge2results[0],len(summary_wordcount.words))
        rouge3recall = RougeEvaluation.rouge_recall(rouge3results[0],rouge3results[1])
        rouge3precision = RougeEvaluation.rouge_precision(rouge3results[0],len(summary_wordcount.words))

        return rouge2recall,rouge2precision,rouge3recall,rouge3precision

#-----TESTING------

#This section is opening a text file with a document summary and a facet that's used as a reference text
#If other summaries or reference texts are used as a source, this needs to be modified
#datafile = open("testAbstraction.txt", "r")
#
#Goes through every line in the text file and finds the points where the document text or the facet text starts
#Results for each text and their respective bigrams and trigrams are printed as they are created, searched and calculated
#for x in datafile:
#    doc_text = re.search("Summary", x)
#    if (doc_text):
#        summary_text = next(datafile)
#        print("Summary text: " + summary_text)
#        summary_wordcount = TextBlob(summary_text)
#        print("Number of words in summary: " + str(len(summary_wordcount.words)))
#
#    facet_text = re.search("Reference", x)
#    if (facet_text):
#        reference_text = next(datafile)
#        print("Reference text: " + reference_text)
#
#        rouge2results = ngram_creation_and_counting(reference_text,summary_text,2)
#        rouge3results = ngram_creation_and_counting(reference_text,summary_text,3)
#
#        print("ROUGE-2 recall: " + rouge_recall(rouge2results[0],rouge2results[1]))
#        print("ROUGE-2 precision: " + rouge_precision(rouge2results[0],len(summary_wordcount.words)))
#        print("ROUGE-3 recall: " + rouge_recall(rouge3results[0],rouge3results[1]))
#        print("ROUGE-3 precision: " + rouge_precision(rouge3results[0],len(summary_wordcount.words)))
#
#datafile.close()