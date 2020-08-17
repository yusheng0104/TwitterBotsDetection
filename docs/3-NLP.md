# Natural Language Processing (NLP)

We developed two different approaches for adding NLP features to our data.  Each is explained below:

**(I) NLP Using Microsoft Azure**

Our first approach to incorporate natural language processing (NLP) features into our classification modeling was with an API from Microsoft’s AI Text Analytics service on Azure’s cloud computing platform (https://azure.microsoft.com/en-us/services/cognitive-services/text-analytics/).  The API allowed us to evaluate the text component of each tweet to create two, new NLP features: 
- Sentiment Score: a real number between 0 and 1 that corresponds to the negative to positive sentiment of the tweet.
- Topic Count:  an integer between 0 and infinity (where 10 appears to be close to an actual upper bound) of the number of topics mentioned in the tweet.

These features are prominent in our analysis--especially since a) Tweepy does not deliver every user attribute via its free, standard service level and b) we lack time to analyze fully deeper aspects of each tweet such as embedded URLs.


**(II) NLP Using NLTK Library**

A second NLP analysis was conducted by hand using the NLTK library. The tweets were aggregated by users and EDA was conducted on the two sets of data to identify key elements of the tweets: the average word-lengths of the tweets per users and the utterance of the top 10 words used by bots. Once these features were engineered, a battery of analytical/classification techniques were employeed on the dataset: data scaling and PCA using sklearn-kit. A modeling suite with grid_search_cv to find optimal parameters on the following models: KNN, Logistic Regression, Linear and Quadradic Discriminant Analysis, Decision Tree Classifiers, Random Forest Classifier, and AdaBoost Clasifier.

[Go to next page](4-EDA)
