import os
from tkinter import *
from tkinter import scrolledtext
import dailyParser.dailyMailparser as dp
#import summarizers.summarizer as summ
from rougeEvaluator.RougeEvaluation import RougeEvaluation
from namedEntitySummarizer.NamedEntitySumm import NERSummarizer

window = Tk()
window.title("Text Summarizer")
window.geometry('600x700')
frame = Frame(window)
rowIndex = 1

parser = dp.DailyMailParser()
rouge = RougeEvaluation()
ner = NERSummarizer()

def summarize(sel):
    #data = getArticle(entry.get())
    #facets = parser.findFacets()
    facets = []
    result = str(["Donald Trump declared election victory on Wednesday morning despite the fact that millions of votes remain uncounted, calling the process a 'fraud on the American people' and claiming he would go to the Supreme Court to challenge the result.", "In Michigan, which holds 16 electoral college votes, Trump is ahead with 49.4% of the vote to Biden's 48.9% with around 87% of the vote counted.", "In Wisconsin, which holds 10 electoral college votes, Biden is ahead with 49.4% of the vote to Trump's 48.85 with an estimated 97% of the vote in.", "Pennsylvania - Reporting 75% Wisconsin - Reporting 97%  Michigan - Reporting 87% Georgia -  Reporting 94%  Nevada - Reporting 67% North Carolina  - Reporting 94%   But at the White House, Trump demanded all counting to stop, boasting about the margins he had rung up already - prompting Biden's team to issue a scathing rebuttal.", 'If Trump wins the Badger state, he’ll need to pick up at least two of the three remaining states, as long as Arizona, Nevada and Nebraska’s 2nd Congressional district stay in Biden’s corner, and Trump earns Maine’s one rogue electoral vote.', "Trump provided little clarity about what he has in mind for his legal team after claiming falsely early Wednesday that he already 'won' the election, calling Tuesday's election a 'fraud on the American people', and demanding that 'all voting stop'.", "Trump said he was 'going' to the Supreme Court to stop the counting of votes, when in fact the course of action would be for Republican lawyers to sue in individual state and county jurisdictions that seek to stop or modify the count in some way.", 'Adding to the confusion and drama of the evening, each state counted its votes differently – with some running through early votes quickly, and others starting with Election Day votes, and mail-in ballots continuing to be the wild card.', 'Concerns are mounting that Trump will declare victory in the state long before votes are counted or that he will attempt to stop mail-in votes being counted after election day.', 'But Pennsylvania, Michigan and Wisconsin will not begin counting the vast majority of mail ballots until Election Day, raising the possibility of a prolonged vote count that could stretch for several days.'])
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
    evalScore = [0.23976608187134502, 0.1105121293800539, 0.08235294117647059, 0.03773584905660377]#rouge.rouge_evaluations(summary, refText.replace("\xa0"," "))
    rougeLabel = Label(frame, text="Rouge Results")
    rougeResults = ("Rouge-2 recall: "+ str(round(float(evalScore[0])*100, 2))+"%\n"
                   +"Rouge-2 precision: "+ str(round(float(evalScore[1])*100, 2))+"%\n"
                   +"Rouge-3 recall: "+ str(round(float(evalScore[2])*100, 2))+"%\n"
                   +"Rouge-3 precision: "+ str(round(float(evalScore[3])*100, 2))+"%\n")
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

entry = Entry(frame, width=70)
entry.grid(row=rowIndex+1, column=0)
entry.insert(0, "Write your Daily Mail article URL here")

launchButton = Button(frame, text="Submit", command=lambda: summarize(selection.get()))
launchButton.grid(row=rowIndex+2, column=0)

summaryLabel = Label(frame, text="Summary")
summaryLabel.grid(row=rowIndex+6, column=0)
summaryText = scrolledtext.ScrolledText(frame, width=70, height=30)
summaryText.grid(column=0)


frame.pack()
window.mainloop()