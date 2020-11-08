import re #Regular expressions for finding matches in the document text
from textblob import TextBlob #Textblob is used for creating bigrams and trigrams
import spacy #Spacy is used for named entity recognition

#Spacy needs a model for finding named entities
nlp = spacy.load("en_core_web_sm")

#Printing named entities from the given document
def print_named_entities(document_text):
    doc = nlp(document_text)
    for ent in doc.ents:
        #This only prints the entities. Can also include whether the entity is a person's name or an organization
        print(ent.text)

#Bigrams are created from the given (human created) reference text. Those bigrams are then searched from the summary.
#The function returns the amount of bigrams and the amount of words in the summary text.
def bigram_creation_and_counting(reference_text, summary_text):
    bigram_wordlist = TextBlob(reference_text).ngrams(2)
    bigram_count = len(bigram_wordlist)
    counter = 0
    match_counter = 0
    #The bigram words in the list are turned into a string of the two words, which are then searched from the summary text.
    for i in bigram_wordlist:
        words = bigram_wordlist[counter][0] + " " + bigram_wordlist[counter][1]
        amount_of_matches = re.findall(words, summary_text)
        match_counter = match_counter + len(amount_of_matches)
        counter = counter + 1
    return match_counter, bigram_count

#Works the same as the bigram creation, except there are three words (trigram) instead of two (bigram)
def trigram_creation_and_counting(reference_text, summary_text):
    trigram_wordlist = TextBlob(reference_text).ngrams(3)
    trigram_count = len(trigram_wordlist)
    counter = 0
    match_counter = 0
    for i in trigram_wordlist:
        words = trigram_wordlist[counter][0] + " " + trigram_wordlist[counter][1] + " " + trigram_wordlist[counter][2]
        amount_of_matches = re.findall(words, summary_text)
        match_counter = match_counter + len(amount_of_matches)
        counter = counter + 1
    return match_counter, trigram_count

#Rouge recall is calculated based on the matches and the bigram count and returned
def rouge_recall(match_amount, bigram_amount):
    recall = match_amount / bigram_amount
    return str(recall)

#Rouge precision is calculated and returned
def rouge_precision(match_amount, text_word_amount):
    precision = match_amount / text_word_amount
    return str(precision)


#This section is opening a text file with a document summary and a facet that's used as a reference text
#If other summaries or reference texts are used as a source, this needs to be modified
datafile = open("high_abstraction.txt", "r")

#Goes through every line in the text file and finds the points where the document text or the facet text starts
#Results for each text and their respective bigrams and trigrams are printed as they are created, searched and calculated
for x in datafile:
    doc_text = re.search("Document", x)
    if (doc_text):
        summary_text = next(datafile)
        print(summary_text)

    facet_text = re.search("Facet-0:", x)
    if (facet_text):
        reference_text = x
        print(reference_text)

        rouge2results = bigram_creation_and_counting(reference_text,summary_text)
        rouge3results = trigram_creation_and_counting(reference_text,summary_text)

        print("ROUGE-2 recall: " + rouge_recall(rouge2results[0],rouge2results[1]))
        print("ROUGE-2 precision: " + rouge_precision(rouge2results[0],len(summary_text.split())))
        print("ROUGE-3 recall: " + rouge_recall(rouge3results[0],rouge3results[1]))
        print("ROUGE-3 precision: " + rouge_precision(rouge3results[0],len(summary_text.split())))

        print_named_entities(summary_text)

datafile.close()