from textblob import TextBlob #Textblob is used for creating bigrams and trigrams

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
                reference_counter = reference_counter + 1
            summary_counter = summary_counter + 1

        ngram_count = len(ngram_referencetuples)
        return match_counter, ngram_count

    #Rouge-N Recall is calculated based on the matches and the bigram count and returned
    def rouge_recall(match_amount, ngram_amount):
        recall = match_amount / ngram_amount
        return str(recall)

    #Rouge-N Precision is calculated and returned
    def rouge_precision(match_amount, text_word_amount):
        precision = match_amount / text_word_amount
        return str(precision)

    #Function responsible for the Rouge-N evaluations. Uses the other helper functions to achieve that.
    #Returns the values for Rouge-2 Recall, Rouge-2 Precision, Rouge-3 Recall and Rouge-3 Precision
    def rouge_evaluations(self,summary,reference):
        rouge2results = RougeEvaluation.ngram_creation_and_counting(reference,summary,2)
        rouge3results = RougeEvaluation.ngram_creation_and_counting(reference,summary,3)
        summary_wordcount = TextBlob(summary)
        rouge2recall = RougeEvaluation.rouge_recall(rouge2results[0],rouge2results[1])
        rouge2precision = RougeEvaluation.rouge_precision(rouge2results[0],len(summary_wordcount.words))
        rouge3recall = RougeEvaluation.rouge_recall(rouge3results[0],rouge3results[1])
        rouge3precision = RougeEvaluation.rouge_precision(rouge3results[0],len(summary_wordcount.words))

        return rouge2recall,rouge2precision,rouge3recall,rouge3precision
