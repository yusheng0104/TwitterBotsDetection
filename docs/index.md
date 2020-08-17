# Introduction 

**Project Background and Purpose**

Most people who use twitter are aware of the possibility that tweets received are tweets generated by computer algorithms or ‘bots’.  There are concerns broadly that bots can cause societal damage by propagating ‘fake news’ that can influence people in a number of ways. The most prominent potential impact of ‘fake news’ is on how recipients of fake news vote in elections, both in the US and abroad.

To mitigate risks associated with bot activity, Twitter takes many steps that include the use of machine learning algorithms to detect the bots (and then terminate the accounts).

This project fits in this context and has its goal the development of machine learning algorithms to detect bots based on tweet activity.  We used techniques taught in CSCI S-109A as demonstrated throughout this report.

**Project Overview**

The following is an outline of how we approached this project:

- We collected user and tweet data from Twitter using its **Tweepy API**.  In the end, this data was for accounts verified by Twitter.
- Two analysis were conducted in parallel: Microsoft’s AI Text Analytics was employeed to provide intricate parameters: sentiment scores and topic counts, and a hand-made analysis suite was created using the free NLTK library..
- We collected user and tweet data from a public source (NBC News) for **'known bots'**.
- We cleaned and integrated the data and performed initial **Exploratory Data Analysis**.
- We added **NLP Features** to each tweet using two methods.  
  - We accessed an Microsoft Azure API that analyzed sentiment and topics.
  - We used the NLTK API to engineer complex features based off the contents of each user's tweets.
- We did additional enrichment, including **user level enrichment** in which we grouped and aggregated tweets by user to create user level features against which we did modeling.
- We modeled the data using many techniques learned in class including **KNN, Logit, LDA, QDA, DecisionTrees, RandomForests, AdaBoost, Stacking, Neural Networks and MLP Classifiers**. 
- In the end we summarize the various models to determine which performed best.
Additional details on the above activity is provided in this rest of this report.


[Go to next page](2-datacollection)