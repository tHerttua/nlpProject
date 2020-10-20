# nlpProject
Project 18: Automatic Text Summarization

Extractive single document summarization and evaluation with in-built information retrieval and graphical user interface

# GUI features:
User input URL (Daily Mail article)
Summarizer selection
Output summary review


# TODO
GUI:
-Implement backend for rouge and spacy
-Add rouge metrics output
-Add system performance metrics

Performance metrics:
-Memory usage
-Processor usage
-Timing
-Comparing against another program

# Design choices
-Only DailyMail will be supported for this version
    *Daily Mail includes user written summaries, which are suitable for    evaluating the rouge metrics

-Only local User Interface will be developed for this version
    *Web application would need more work, and it would need to be hosted
     to be useful

-No language selection
    *This version doesn't have language selection as it would require more tuning to use between all the tools, and in the end is only a 'nice-to-have' feature as all the articles are in english 

# Future Development
-Language
    *In the future development, multi-linguality or even cross-linguality
    are great features, but left out of the scope for lack of resource,
    and the application will be langue-specific.

-Web application
    *Hosted web application...

# NOTE
Python must be configured for Tk

# Packages
Needed python packages: 
(Later on will be included in setup.py file)
-pytldr
-beautifulsoup4
-requests
