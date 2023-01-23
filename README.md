# README

This script uses the Twint library to search for tweets containing a specific keyword (in this case, the keyword is the name of a company, specified in an environment variable), and then uses the VaderSentiment library to perform sentiment analysis on the tweets. The script filters out tweets sent by the company itself and tweets that are not in English, and then saves the results to a CSV file.

## Requirements

- Twint
- VaderSentiment
- Pandas
- os
- dotenv

## Setup

- Install the required libraries by running `pip install -r requirements.txt`
- Create a .env file in the same directory as the script with the following contents: COMPANY_NAME=<name of company>

## Running the script

- Run the script by running `python script.py`
- The script will create a file named "results.csv" in the same directory, containing the tweets and their sentiment scores.

## Customizing the script

- To change the keyword for the tweets search, change the value of the `COMPANY_NAME` environment variable in the .env file
- To change the number of tweets to be retrieved, change the value of `c.Limit`
- To change the language of tweets, change the value of `c.Lang`
- To change the name of the output file, change the value of `tweets_df.to_csv('results.csv')`
