import json
import sys
import numpy as np
import re
# A list of all emojis
from emojiList import emoji

resultfile = open('resultdata.json', 'wt')
data = []
with open('tweet_by_ID_21_10_2018__02_45_52.txt') as json_data:
	for line in json_data:
		obj = json.loads(line)
		# print(obj['text'])
		data.append(obj['text'])
resultfile.write(json.dumps(data))
resultfile.close()

HASHTAGS_REGEX = re.compile('#')
MENTIONS_REGEX = re.compile('@[^\s]+')
EMOJI_NAME_REGEX = re.compile(':[a-z_-]+:')
LINK_REGEX = re.compile('https?://[^\s]+')
EXTRA_SPACES_REGEX = re.compile('\s{2,}')
HAYSTACK_REGEX = re.compile('(RT)')
ASCII_REGEX = re.compile('[[:ascii:]]')

def preprocess_tweet(tweet, pipeline):
    for pipe in pipeline:
        tweet = pipe(tweet)
    return tweet

def preprocess_hashtags(tweet):
    return HASHTAGS_REGEX.sub('', tweet)

def preprocess_mentions(tweet):
    return MENTIONS_REGEX.sub('', tweet)

def remove_extra_spaces(tweet):
    return EXTRA_SPACES_REGEX.sub(' ', tweet).strip()

def remove_hyperlinks(tweet):
    return LINK_REGEX.sub('', tweet)

def remove_haystack(tweet):
    return HAYSTACK_REGEX.sub('', tweet)

def remove_unicode(tweet):
    return ASCII_REGEX.sub('', tweet)

def extract_tweet(tweet):
    tweet = EMOJI_NAME_REGEX.sub('', tweet)
    return tweet

preprocessing_pipeline = [
    preprocess_hashtags,
    preprocess_mentions,
    remove_hyperlinks,
    remove_unicode,
    remove_haystack,
]

f = open("tweet_file","w+")
for d in data:
    f.write("{}\n".format(extract_tweet(preprocess_tweet(d, preprocessing_pipeline))))
f.close()