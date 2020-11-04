import os
from tkinter import *
import dailyParser.dailyMailparser as dp
#import summaries.summarizers as summaries
root = Tk()
parser = dp.DailyMailParser()

def summarize(sel):
    data = getArticle(entry.get())
    result = runSummarize(sel, data)
    someLabel2 = Label(root, text=result +" "+str(sel))
    someLabel2.pack()

def runSummarize(sel, data):
    if sel == 1:
        summary = "X"
        #summary = summaries.TextRankSummarizer(data)
    elif sel == 2:
        summary = "Y"
        #summary = summaries.LSA(data)
    elif sel == 3:
        summary = "Z"
        #summary = summaries.relevance(data)
    return summary

def getArticle(URL):
    parser.openURL(URL)
    article = parser.findContent()
    return article

def evaluateText():
    pass



someLabel1 = Label(root, text="Text Summarizer")
entry = Entry(root, width=50)
entry.insert(0, "Daily Mail URL here")


MODES = [
    ("Text Rank",1),
    ("LSA",2),
    ("Relevance",3),
    ]
selection = IntVar(root)
selection.set(1)
for text, mode, in MODES:
    Radiobutton(root, text=text, value=mode, variable=selection).pack()

someButton = Button(root, text="Submit", command=lambda: summarize(selection.get()))

entry.pack()
someButton.pack()
someLabel1.pack()


root.mainloop()