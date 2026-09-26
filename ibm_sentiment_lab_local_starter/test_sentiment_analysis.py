import unittest 
from SentimentAnalysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):

    def test_sentiment_analyzer(self):
     actual = sentiment_analyzer("I love working with Python")
     expected = "SENT_POSITIVE"
     actual_label = actual["label"]
     self.assertEqual(actual_label, expected)

     actual = sentiment_analyzer("I hate working with Python")
     expected = "SENT_NEGATIVE"
     actual_label = actual["label"]
     self.assertEqual(actual_label, expected)

     actual = sentiment_analyzer("I am neutral on Python")
     expected = "SENT_NEUTRAL"
     actual_label = actual["label"]
     self.assertEqual(actual_label, expected)

if __name__ == "__main__":
 unittest.main()
     
