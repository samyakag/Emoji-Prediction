import json
import sys
import numpy as np
import re
# A list of all emojis
from emojiList import emoji


class preprocessingTweets:

    HASHTAGS_REGEX = re.compile('#')
    MENTIONS_REGEX = re.compile('@[^\s]+')
    EMOJI_NAME_REGEX = re.compile(':[a-z_-]+:')
    LINK_REGEX = re.compile('https?://[^\s]+')
    EXTRA_SPACES_REGEX = re.compile('\s{2,}')
    HAYSTACK_REGEX = re.compile('(RT)')
    ASCII_REGEX = re.compile('[[:ascii:]]')

    preprocessing_pipeline = [
        preprocess_hashtags,
        preprocess_mentions,
        remove_hyperlinks,
        remove_unicode,
        remove_haystack,
    ]

    def __init__(self, json_file):
        self.file = json_file

    def read_data(self):
        resultfile = open('resultdata.json', 'wt')
        data = []
        with open(self.file) as json_data:
        	for line in json_data:
        		obj = json.loads(line)
        		# print(obj['text'])
        		data.append(obj['text'])
        self.data = data
        resultfile.write(json.dumps(data))
        resultfile.close()

    @staticmethod
    def preprocess_hashtags(tweet):
        return HASHTAGS_REGEX.sub('', tweet)

    @staticmethod
    def preprocess_mentions(tweet):
        return MENTIONS_REGEX.sub('', tweet)

    @staticmethod
    def remove_extra_spaces(tweet):
        return EXTRA_SPACES_REGEX.sub(' ', tweet).strip()

    @staticmethod
    def remove_hyperlinks(tweet):
        return LINK_REGEX.sub('', tweet)

    @staticmethod
    def remove_haystack(tweet):
        return HAYSTACK_REGEX.sub('', tweet)

    @staticmethod
    def remove_unicode(tweet):
        return ASCII_REGEX.sub('', tweet)

    @staticmethod
    def preprocess_tweet(tweet, pipeline):
        for pipe in pipeline:
            tweet = pipe(tweet)
        return tweet

    @staticmethod
    def extract_tweet(tweet):
        tweet = EMOJI_NAME_REGEX.sub('', tweet)
        return tweet

    def write_file(self):
        f = open("tweet_file","w+")
        for d in self.data:
            f.write("{}\n".format(extract_tweet(preprocess_tweet(d, preprocessing_pipeline))))
        f.close()