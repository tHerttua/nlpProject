from textblob import TextBlob
import re

class RougeEvaluation():
    def __init__(self):
        pass

    def ngram_creation_and_counting(self, reference_text, summary_text, grams):
        """
        N-grams are created from the given (human written) reference text. Those N-grams are then searched from the summary.
        The method returns the amount of N-grams and the amount of words in the summary text.
        Creates tuple lists of the reference text and the summary.
        Then compares the reference wordlist tuples and compares them to the summary tuples
        """
        ngram_referencetuples = TextBlob(reference_text).ngrams(grams)
        ngram_summarytuples = TextBlob(summary_text).ngrams(grams)

        summary_counter = 0
        match_counter = 0

        for _ in ngram_summarytuples:
            reference_counter = 0
            for __ in ngram_referencetuples:
                if ngram_referencetuples[reference_counter].lower() == ngram_summarytuples[summary_counter].lower():
                    match_counter = match_counter + 1
                reference_counter = reference_counter + 1
            summary_counter = summary_counter + 1

        ngram_count = len(ngram_referencetuples)

        return match_counter, ngram_count

    def rouge_recall(self, match_amount, ngram_amount):
        """
        Calculates the Rouge-N precision based on the matches and the bigram count
        """
        recall = match_amount / ngram_amount
        return str(recall)

    def rouge_precision(self, match_amount, text_word_amount):
        """
        Calculates the Rouge-N precision
        """
        precision = match_amount / text_word_amount
        return str(precision)

    def rouge_evaluations(self, summary,reference):
        """
        Uses the methods to calculate recall and precision values for both Rouge-2 and Rouge-3
        """
        rouge2results = self.ngram_creation_and_counting(reference,summary,2)
        rouge3results = self.ngram_creation_and_counting(reference,summary,3)
        summary_wordcount = TextBlob(summary)
        rouge2recall = self.rouge_recall(rouge2results[0],rouge2results[1])
        rouge2precision = self.rouge_precision(rouge2results[0],len(summary_wordcount.words))
        rouge3recall = self.rouge_recall(rouge3results[0],rouge3results[1])
        rouge3precision = self.rouge_precision(rouge3results[0],len(summary_wordcount.words))

        return rouge2recall,rouge2precision,rouge3recall,rouge3precision