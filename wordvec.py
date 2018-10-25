from gensim.models import Word2Vec as w2v
import multiprocessing
import nltk


class word2vec:
	def __init__(self, tweet_file):
		self.file = tweet_file

	def preprocess_tweets(self):
		""" Tokenises all tweets to get words"""

		# Tokenize the sentences
		raw_sentences = []
		tweets = open(self.file, "r")
		for tweet in tweets:
		    raw_sentences.append(nltk.word_tokenize(tweet))
		self.sentences = raw_sentences


	def make_model(self):
		""" Model and train the word2vec model on words from tweets"""

		# Define parameters for the w2v model
		num_features = 300
		min_word_count = 3
		num_workers = multiprocessing.cpu_count()
		context_size = 7
		downsampling = 1e-3
		seed = 1

		# Build the model
		self.tweet2vec = w2v(
		    sg = 1,
		    seed = seed,
		    workers = num_workers,
		    size = num_features,
		    min_count = min_word_count,
		    window = context_size,
		    sample = downsampling
		)

		# Build the vocabulary
		self.tweet2vec.build_vocab(self.sentences)
		# Train the model
		self.tweet2vec.train(self.sentences, epochs = 10, total_examples = len(self.sentences))

	def run(self):
		self.preprocess_tweets()
		self.make_model()