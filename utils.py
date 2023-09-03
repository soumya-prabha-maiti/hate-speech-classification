import re
import string
from collections.abc import Iterable

import nltk
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from nltk.corpus import stopwords

nltk.download('stopwords')


# Apply regex and do cleaning.
def clean_text(words: str) -> str:
    words = str(words).lower()
    words = re.sub('\[.*?\]', '', words)
    words = re.sub('https?://\S+|www\.\S+', '', words)
    words = re.sub('<.*?>+', '', words)
    words = re.sub(r'@\w+', '', words)
    words = re.sub('[%s]' % re.escape(string.punctuation), '', words)
    words = re.sub('\n', '', words)
    words = re.sub('\w*\d\w*', '', words)

    stopword = set(stopwords.words('english'))
    words = ' '.join(
        [word for word in words.split(' ') if word not in stopword])

    stemmer = nltk.SnowballStemmer("english")
    words = ' '.join([stemmer.stem(word) for word in words.split(' ')])

    return words


def tokenize_and_pad(text_list: Iterable[str], tokenizer: Tokenizer, max_len: int) -> np.ndarray[np.str_]:
    sequences = tokenizer.texts_to_sequences(text_list)
    sequences_matrix = pad_sequences(sequences, maxlen=max_len)
    return sequences_matrix
