from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
import numpy as np

class Classifier():

	def __init__(self, tweet_file, labels, clf, w2v):
		self.file = tweet_file
		self.labels = labels
		self.tweet2vec = w2v
		self.features = []
		if clf == 'KNN':
			self.clf = KNeighborsClassifier()
		elif clf == 'NB':
			self.clf = GaussianNB()
		elif clf == 'MLP':
			self.clf = MLPClassifier()

	def make_features(self):
		"""Creates features for out model from training tweets"""
		tweets = open(self.file, "r")
		for i, tweet in enumerate(tweets):
			if i > 20000:
				break
			avg_vec = np.zeros(self.tweet2vec.wv.vector_size)
			for word in tweet:
				if word not in self.tweet2vec.wv.vocab:
					continue
				avg_vec = np.add(avg_vec, self.tweet2vec.wv[word])
			self.features.append(np.true_divide(avg_vec, len(tweet)))
		tweets.close()

	def train(self):
		"""Trains the classifier"""
		self.clf.train(self.features, self.labels)

	def predict(self, tweet):
		"""Predicts the emoji given a tweet"""
		avg_vec = np.zeros(self.tweet2vec.wv.vector_size)
		for word in tweet:
			if word not in self.tweet2vec.wv.vocab:
				continue
			avg_vec = np.add(avg.vec, self.tweet2vec.wv[word])
		vector = np.true_divide(avg_vec, len(tweet))
		pred = self.clf.prdict(vector)
		return pred
