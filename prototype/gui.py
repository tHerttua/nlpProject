import os
from tkinter import *
from tkinter import scrolledtext
import dailyParser.dailyMailparser as dp
#import summaries.summarizers as summaries
root = Tk()
root.title("Text Summarizer")
root.geometry('500x400')
frame = Frame(root)
rowIndex = 1

parser = dp.DailyMailParser()

def summarize(sel):
    data = getArticle(entry.get())
    result = runSummarize(sel, data)
    summaryText.delete("1.0", "end")
    summaryText.insert(END, result)
    evaluateText()
    evaluateNER()

def runSummarize(sel, data):
    if sel == 1:
        summary = "Mark Halsey has slammed the FA for overlooking Mark Clattenburg Former Premier League referee Halsey has called the decision 'a joke'"
        #summary = summaries.TextRankSummarizer(data)
    elif sel == 2:
        summary = "Y"
        #summary = summaries.LSA(data)
    elif sel == 3:
        summary = "After beating Tommy Burns in 1908, Jack Johnson became the first ever black world heavyweight champion He held the belt for six years and Sunday will mark the 100 year anniversary of his last title defence During a particularly racist period of American history, Johnson's title reign was met with many protests Johnson was eventually defeated by Jess Willard in 1915, following 26 brutal rounds in the sweltering heat of Cuba "
        #summary = summaries.relevance(data)
    return summary

def getArticle(URL):
    parser.openURL(URL)
    article = parser.findContent()
    return article

def evaluateText():
    evalList = [1,2,3,4]
    rougeLabel = Label(frame, text="Rouge Results")
    rougeResults = ("Rouge-2 recall: "+ str(evalList[0])+"\n"
                   +"Rouge-2 precision: "+ str(evalList[0]) +"\n"
                   +"Rouge-3 recall: "+ str(evalList[0]) +"\n"
                   +"Rouge-3 precision: "+ str(evalList[0])+"\n")
    rougeLabel['text'] = rougeResults
    rougeLabel.grid(row=rowIndex+5, column=0)

def evaluateNER():
    pass



#https://www.dailymail.co.uk/news/article-8911739/Georgia-QAnon-supporter-Marjorie-Taylor-Greene-elected-Congress.html

MODES = [
    ("Text Rank",1),
    ("LSA",2),
    ("Relevance",3),
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
root.mainloop()