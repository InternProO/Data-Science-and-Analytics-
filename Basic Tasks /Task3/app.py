import tweepy
import pandas as pd

# Twitter API credentials (replace with your own)
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# Authentication
auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Scrape tweets about a trending topic
def scrape_tweets(query, count=100):
    tweets = tweepy.Cursor(api.search, q=query, lang="en").items(count)
    tweet_list = []
    for tweet in tweets:
        tweet_list.append(tweet.text)
    return tweet_list

# Example usage
query = 'Python programming'
tweets = scrape_tweets(query)

from textblob import TextBlob

def analyze_sentiment(tweets):
    sentiments = []
    for tweet in tweets:
        analysis = TextBlob(tweet)
        sentiments.append(analysis.sentiment.polarity)
    return sentiments

# Analyze sentiment
sentiments = analyze_sentiment(tweets)

import matplotlib.pyplot as plt
import seaborn as sns

def generate_report(sentiments):
    df = pd.DataFrame(sentiments, columns=['Sentiment'])
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Sentiment'], kde=True)
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.show()

# Generate and display report
generate_report(sentiments)

import tweepy
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

# Twitter API credentials (replace with your own)
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# Authentication
auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Scrape tweets about a trending topic
def scrape_tweets(query, count=100):
    tweets = tweepy.Cursor(api.search, q=query, lang="en").items(count)
    tweet_list = []
    for tweet in tweets:
        tweet_list.append(tweet.text)
    return tweet_list

# Analyze sentiment
def analyze_sentiment(tweets):
    sentiments = []
    for tweet in tweets:
        analysis = TextBlob(tweet)
        sentiments.append(analysis.sentiment.polarity)
    return sentiments

# Generate and display report
def generate_report(sentiments):
    df = pd.DataFrame(sentiments, columns=['Sentiment'])
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Sentiment'], kde=True)
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.show()

# Example usage
query = 'Python programming'
tweets = scrape_tweets(query)
sentiments = analyze_sentiment(tweets)
generate_report(sentiments)
