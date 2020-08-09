# Sentiment Analysis

For this project, we conducted sentiment analysis on homework review data. By running different sentiment analysis processes on our input data, we were able to analyze subjective characteristics of our input data and extrapolate further information that can be used to draw conclusions and improve the course.

## Motivation for Sentiment Analysis

Sentiment analysis is a way to analyze the mood or emotion in a large collection of text documents. Sentiment analysis is a particularly powerful tool to use because it combines natural language processing and data analysis. By using sentiment analysis on our input data, we are able to extract qualities of our input data and then display those qualities in visual formats like graphs and charts. For our homework reviews data, we are able to break down our results even further by things like homework, topic, or semester.  This allows us to easily filter our output based on different audiences we may have or specific problems we are trying to solve. 

## Sentiment Score Calculations

In order to determine the sentiment score of a given review, the following calculation was used: 

*Sentiment Score = (positive words-negative words) / Total Words*

The sentiment score was different between the sum of the positive words and the sum of the  negative words in the review divided by the total words in the review. In order to determine if a word was positive or negative, we used the list of positive and negative words that was supplied. In Appendix 8.2 there is a sample walkthrough of this calculation. The other calculation that was considered was the following:

*Sentiment Score = positive words - negative words*

As will be discussed in the evaluation of the model, the sentiment score that divides by total words proved to be more effective in identifying if a review was positive or negative. Due to the way it is calculated, the range of values were [-1,1], where 1 is perfectly positive and -1 is perfectly negative. 
    The last part of the sentiment calculations involved negation handling. In order to account for phrases like “not good” in which the negation word “not” changes the sentiment meaning of the word “good.” In order to handle this, we stored if a word had a negation word (“not”, “no”, “neither”, etc.) before it, and if it did, the value of the word was multiplied by negative to flip the sentiment of the original score.

`To view the complete report, see SentimentAnalysisFindings.pdf `
