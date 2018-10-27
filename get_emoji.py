import json
import sys
import numpy as np
# A list of all emojis
from emojiList import emoji


class getEmojis:
	"""Class to get Emojis from tweets"""
	def __init__(self, tweet_file):
		self.file = tweet_file

	def read_data(self):
		"""Reads all the tweets from the json file"""
		with open(self.file, encoding='utf-8') as data_file:
			self.data = json.loads(data_file.read())

	@staticmethod
	def extract_emojis(s):
		"""Given a tweet, returns emjois in it"""
		return ' '.join(c for c in s if c in emoji)

	def find_emojis(self):
		"""Find all the emojis in the given data and unique emojis"""
		# Extract the emoji from each tweet and save the unique emoji
		# There is only one unique emoji per tweet
		self.emoji_labels = []
		for i, d in enumerate(self.data):
			if i > 20000:
				break
			emoji_label = self.extract_emojis(d)
			li = np.asarray(list(emoji_label.split(" ")))
			self.emoji_labels.append(np.unique(li))

		self.unique_emojis = np.unique(self.emoji_labels)
		self.unique_emojis = (np.array(self.unique_emojis.tolist())[1:]).tolist()

	def run(self):
		"""Helper function to run all required functions"""
		self.read_data()
		self.find_emojis()
