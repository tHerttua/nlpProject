import os
from tkinter import *
from tkinter import scrolledtext
import dailyParser.dailyMailparser as dp
#import summarizers.summarizer as summ
from rougeEvaluator.RougeEvaluation import RougeEvaluation
from namedEntitySummarizer.NamedEntitySumm import NERSummarizer

window = Tk()
window.title("Text Summarizer")
window.geometry('500x400')
frame = Frame(window)
rowIndex = 1

parser = dp.DailyMailParser()
rouge = RougeEvaluation()
ner = NERSummarizer()

def summarize(sel):
    data = getArticle(entry.get())
    facets = parser.findFacets()
    result = runSummarize(sel, data.replace("\xa0"," "), len(facets))
    summaryText.delete("1.0", "end")
    summaryText.insert(END, result)
    evaluateText(result, facets)
    

def runSummarize(sel, data, refSentences):
    if sel == 1:
        summary = "text rank summary"#summ.textRank(data, refSentences)
    elif sel == 2:
        summary = "lsa_o summary"#summ.LSA_O(data, refSentences)
    elif sel == 3:
        summary = "lsa_s summary"#summ.LSA_S(data, refSentences)
    elif sel == 4:
        summary = "relevance summary"#summ.relevance(data, refSentences)
    elif sel == 5:
        summary = ner.Named_Entity_Summary(data, refSentences)
    return summary

def getArticle(URL):
    parser.openURL(URL)
    article = parser.findContent()
    return article

def evaluateText(summary, facets):
    refText = str(facets)
    evalScore = rouge.rouge_evaluations(summary, refText.replace("\xa0"," "))
    rougeLabel = Label(frame, text="Rouge Results")
    rougeResults = ("Rouge-2 recall: "+ str(evalScore[0])+"\n"
                   +"Rouge-2 precision: "+ str(evalScore[0]) +"\n"
                   +"Rouge-3 recall: "+ str(evalScore[0]) +"\n"
                   +"Rouge-3 precision: "+ str(evalScore[0])+"\n")
    rougeLabel['text'] = rougeResults
    rougeLabel.grid(row=rowIndex+5, column=0)



#https://www.dailymail.co.uk/news/article-8911739/Georgia-QAnon-supporter-Marjorie-Taylor-Greene-elected-Congress.html

MODES = [
    ("Text Rank",1),
    ("LSA Ozsoy",2),
    ("LSA Steinberg",3),
    ("Relevance", 4),
    ("Named Entity Summarizer",5)
    ]
selection = IntVar(frame)
selection.set(1)
for text, mode, in MODES:
    Radiobutton(frame, text=text, value=mode, variable=selection).grid(row=rowIndex, column=0)
    rowIndex += 1

Label(frame, text="Select a summarizer").grid(row=0, column=0)

entry = Entry(frame, width=50)
entry.grid(row=rowIndex+1, column=0)
entry.insert(0, "Write your Daily Mail article URL here")

launchButton = Button(frame, text="Submit", command=lambda: summarize(selection.get()))
launchButton.grid(row=rowIndex+2, column=0)

summaryLabel = Label(frame, text="Summary")
summaryLabel.grid(row=rowIndex+6, column=0)
summaryText = scrolledtext.ScrolledText(frame, width=50, height=10)
summaryText.grid(column=0)


frame.pack()
window.mainloop()