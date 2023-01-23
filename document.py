import twint
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os
from dotenv import load_dotenv
load_dotenv()
company_name = os.environ.get("COMPANY_NAME")

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Get tweets
c = twint.Config()
c.Search = company_name
c.Utc = True
c.Full_text = True
c.Limit = 100
c.Lang = "en"
c.Pandas = True

twint.run.Search(c)

# Save to a dataframe
tweets_df = pd.DataFrame(twint.storage.panda.Tweets_df)

# Run sentiment analysis on tweets
tweets_df['sentiment_score'] = tweets_df['tweet'].apply(
    lambda x: analyzer.polarity_scores(x))

# Filter out all tweets sent by @primark
tweets_df = tweets_df[tweets_df['username'] != company_name]
# Filter out all tweets that are not in English
tweets_df = tweets_df[tweets_df['language'] == 'en']

# Output to csv
tweets_df.to_csv('results.csv')
