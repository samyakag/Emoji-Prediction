import json
import sys
import numpy as np
# A list of all emojis
from emojiList import emoji

with open('resultdata.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

def extract_emojis(s):
    return ' '.join(c for c in s if c in emoji)

emoji_labels = []
unique_emojis = []

# Extract the emoji from each tweet and save the unique emoji
# There is only one emoji per tweet
for i, d in enumerate(data):
	emoji_label = extract_emojis(d)
	li = np.asarray(list(emoji_label.split(" ")))
	emoji_labels.append(np.unique(li))

unique_emojis = np.unique(emoji_labels)
unique_emojis = (np.array(unique_emojis.tolist())[1:]).tolist()
print (unique_emojis)