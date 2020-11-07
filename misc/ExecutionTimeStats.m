%Load the data
data = readtable('Stats-20201107-120521.csv')
data = sortrows(data,'article_word_amount','ascend')

%Extract execution times
execution_times = [data.LSA_O_execution_time, data.LSA_S_execution_time, data.Relevance_execution_time, data.TextRank_execution_time, data.NER_execution_time]

%Plot the data
plot(data.article_word_amount, execution_times)
title('Execution times compared to article text length')
xlabel('Article length in words')
ylabel('Execution times in seconds')
legend({'LSA_O', 'LSA_S', 'Relevance', 'TextRank', 'Named Entity'}, 'Location', 'northwest')
