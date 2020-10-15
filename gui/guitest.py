import os
from tkinter import *
import summaries
root = Tk()

def summarize(sel):
    data = getData(entry.get())
    result = runSummarize(sel, data)
    someLabel2 = Label(root, text=filePath +" "+str(sel))
    someLabel2.pack()

def runSummarize(sel, data):
    if sel == 1:
        summary = summaries.TextRankSummarizer(sel, data)
    elif sel == 2:
        summary = summaries.summary_LSA(sel, data)
    elif sel == 3:
        summary = summaries.summary_relevance(sel, data)
    return summary

def getData(filepath):
    if os.path.exists(filepath):
        with open filepath as f:
            data = f.read()
        return data

someLabel1 = Label(root, text="Text Summarizer")
entry = Entry(root, width=50)
entry.insert(0, "./sampleDocs/")


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

#entry.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
entry.pack()
someButton.pack()
someLabel1.pack()


root.mainloop()