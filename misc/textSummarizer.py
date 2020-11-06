import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument('URL list', type=str, help="The path to the list containing all the ULRs")
argParser.add_argument('-e', '--evaluate', help="Evaluate and produce csv containing the evaluation data from the URL list")
argParser.add_argument('-s', '--summarize', help="Summarize and produce output from the URL list")
argParser.add_argument('-p', '--performance', help="Produce performance metrics, and save them under perfMetrics directory")

args = argParser.parse_args()

