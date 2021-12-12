from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from flair.models import TextClassifier
from flair.data import Sentence
# import nltk
# import ssl
#
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
# nltk.download()


class SentimentAnalyzer:

    def __init__(self):
        # self.analyzer = SentimentIntensityAnalyzer()
        self.analyzer = TextClassifier.load('en-sentiment')

    def determine_sentiment(self, text):
        score = 0
        try:
            # return self.analyzer.polarity_scores(text)
            # return TextBlob(text).sentiment.polarity
            sentence = Sentence(text)
            self.analyzer.predict(sentence)
            score = round(sentence.labels[0].score, 2)
            sentiment_category = sentence.labels[0].value
            if sentiment_category == 'NEGATIVE':
                score = -score
            elif sentiment_category == 'POSITIVE':
                t = 0  # do nothing
            else:
                raise Exception("Unsupported sentiment category: " + str(sentiment_category))
        except Exception as err:
            print("Failed to determine sentiment: ", err)
        return score
