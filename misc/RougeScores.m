%Load the data of the 73 text summarizations
data = readtable('Stats-20201107-120521.csv')

rouge2_recall = [data.LSA_O_ROUGE2_recall, data.LSA_S_ROUGE2_recall, data.Relevance_ROUGE2_recall, data.TextRank_ROUGE2_recall, data.NER_summary_ROUGE2_recall]
rouge2_precision = [data.LSA_O_ROUGE2_precision, data.LSA_S_ROUGE2_precision, data.Relevance_ROUGE2_precision, data.TextRank_ROUGE2_precision, data.NER_summary_ROUGE2_precision]
rouge3_recall = [data.LSA_O_ROUGE3_recall, data.LSA_S_ROUGE3_recall, data.Relevance_ROUGE3_recall, data.TextRank_ROUGE3_recall, data.NER_summary_ROUGE3_recall]
rouge3_precision = [data.LSA_O_ROUGE3_precision, data.LSA_S_ROUGE3_precision, data.Relevance_ROUGE3_precision, data.TextRank_ROUGE3_precision, data.NER_summary_ROUGE3_precision]

%Calculate the means
for i = 1:5
    rouge2_recall_mean(:,i) = nanmean(rouge2_recall(:,i))
    rouge2_precision_mean(:,i) = nanmean(rouge2_precision(:,i))
    rouge3_recall_mean(:,i) = nanmean(rouge3_recall(:,i))
    rouge3_precision_mean(:,i) = nanmean(rouge3_precision(:,i))
    f_scores_rouge2(:,i) = ((2*(rouge2_recall(:,i) .* rouge2_precision(:,i))) ./ (rouge2_recall(:,i) + rouge2_precision(:,i)))
    f_scores_rouge3(:,i) = ((2*(rouge2_recall(:,i) .* rouge2_precision(:,i))) ./ (rouge2_recall(:,i) + rouge2_precision(:,i)))
    f_scores_mean_rouge2(:,i) = nanmean(f_scores_rouge2(:,i))
    f_scores_mean_rouge3(:,i) = nanmean(f_scores_rouge3(:,i))
end

%Create plots
y = [f_scores_mean_rouge2 ; f_scores_mean_rouge3]
figure(1)
bar(y)
title('F-Measures of Rouge-2 and Rouge-3 Scores')
set(gca, 'xticklabel',{'Rouge-2', 'Rouge-3'})
set(gca, 'YLim', [0,0.25])
ylabel('F-Measure')
legend({'LSA_O', 'LSA_S', 'Relevance', 'TextRank', 'Named Entity'}, 'Location', 'northeast')

y = [rouge2_recall_mean;rouge2_precision_mean]
figure(2)
bar(y)
title('Rouge-2 Scores')
set(gca, 'xticklabel',{'Rouge-2 Recall', 'Rouge-2 Precision'})
ylabel('Rouge-2 scores')
legend({'LSA_O', 'LSA_S', 'Relevance', 'TextRank', 'Named Entity'}, 'Location', 'northeast')

y = [rouge2_recall_mean;rouge2_precision_mean;rouge3_recall_mean;rouge3_precision_mean]
figure(3)
h = heatmap(y)
title('Rouge-2 and Rouge-3 Scores')
set(gca, 'XData',{'LSA_O', 'LSA_S', 'Relevance', 'TextRank', 'Named Entity'})
set(gca, 'YData',{'Rouge-2 Recall', 'Rouge-2 Precision', 'Rouge-3 Recall', 'Rouge-3 Precision'})

y = [rouge3_recall_mean;rouge3_precision_mean]
figure(4)
bar(y)
title('Rouge-3 Scores')
set(gca, 'xticklabel',{'Rouge-3 Recall', 'Rouge-3 Precision'})
ylabel('Rouge-3 scores')
legend({'LSA_O', 'LSA_S', 'Relevance', 'TextRank', 'Named Entity'}, 'Location', 'northeast')


