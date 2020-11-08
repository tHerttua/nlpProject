# Three generated summaries of the intro to my master's thesis, can be found in the text file "intro.txt".
# Three types of summarizers are used: TextRank, latent semantic analysis (LSA), and relevance scoring based.

# The input 'text' can be a .txt file, url or a string.
# For some reason using the text file as input did not work, so we will first read it to a string.
name = "intro.txt"
file = open(name,'r')
text = file.read()
file.close()

# Import summarizers
from pytldr.summarize import TextRankSummarizer
from pytldr.summarize import LsaSummarizer
from pytldr.summarize import RelevanceSummarizer

# Initialize the summarizers
TextRankSummarizer = TextRankSummarizer()
LSASummarizer = LsaSummarizer()
RelevanceSummarizer = RelevanceSummarizer()

# Generate the summaries, each is five sentences long
summary_TextRank = TextRankSummarizer.summarize(text, length=5)
summary_LSA = LSASummarizer.summarize(text, topics=4, length=5, binary_matrix=True, topic_sigma_threshold=0.5)
summary_relevance = RelevanceSummarizer.summarize(text, length=5, binary_matrix=True)

# Print summaries
#print("TextRank: ", ' '.join(summary_TextRank))
#print("LSA: ", ' '.join(summary_LSA))
#print("Relevance scoring: ", ' '.join(summary_relevance))

# Save summaries to a text file for easier reading
file = open("summaries.txt",'w')
file.write("TextRank: " + ' '.join(summary_TextRank) + "\n\n")
file.write("LSA: " + ' '.join(summary_LSA) + "\n\n")
file.write("Relevance scoring: " + ' '.join(summary_relevance))
file.close()

# Overall comment: Not very coherent, but to be fair, five sentences is rather short anyway.
# We can of course use some different text. The instruction was "original document", but I don't know if it really needs to be.