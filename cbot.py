import nltk
nltk.download('punkt')
import random
import string
import warnings
warnings.filterwarnings('ignore')

f=open('./data.txt', 'r', errors='ignore')

raw = f.read()
raw = raw.lower()

sent_tokens = nltk.sent_tokenize(raw)       #converts to list of sentences
word_tokens = nltk.word_tokenize(raw)       #converts to list of words

sentTokens = sent_tokens[:4]
print(sentTokens)

wordTokens = word_tokens[:4]
print(wordTokens)