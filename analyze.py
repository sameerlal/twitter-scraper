'''
    Simple example of extrating Katy Perry's Tweets and writing to a CSV file 
'''


from twitter_scraper import get_tweets
import pandas as pd 
import numpy as np 
import csv


with open('output.txt', 'w') as file:
    for tweet in get_tweets('katyperry'):
        file.write(tweet['text'] + '\n')