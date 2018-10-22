from gensim.models import Word2Vec as w2v
import multiprocessing
import nltk

# Tokenize the sentences
raw_sentences = []
tweets = open("tweet_file","r")
for tweet in tweets:
    raw_sentences.append(nltk.word_tokenize(tweet))


# Define parameters for the w2v model
num_features = 300
min_word_count = 3
num_workers = multiprocessing.cpu_count()
context_size = 7
downsampling = 1e-3
seed = 1

# Build the model
tweet2vec = w2v.Word2Vec(
    sg=1,
    seed=seed,
    workers=num_workers,
    size=num_features,
    min_count=min_word_count,
    window=context_size,
    sample=downsampling
)
# Build the vocabulary
tweet2vec.build_vocab(raw_sentences)
# Train the model
tweet2vec.train(raw_sentences,epochs=10, total_examples=len(raw_sentences))