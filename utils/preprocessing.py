import string
import hazm
import nltk
import pandas as pd

from collections import Counter
from hazm import Lemmatizer, Normalizer, stopwords_list, word_tokenize


data = pd.read_csv('../data/taghche.csv')


def mean_rating(book_name):
    filtered_data = data[data['bookname'] == book_name]
    return filtered_data['rate'].mean()


def frequent_word(book_name):
    filtered_data = data[data['bookname'] == book_name]
    merged_comment_text = ' '.join(filtered_data['comment'])
    normalizer = Normalizer()
    normalize_comment = normalizer.normalize(merged_comment_text)
    punctuation_chars = string.punctuation + "۔،؛«؟»٬٫٪٭٪ـٰٕٖٓٗٔٛۖۗۘۙۚۛۜ۝۞ۣ۟۠ۡۢۤۥۦۯۦۧۨ۩۪ۭ۫۬ۮۯ۰۱۲۳۴۵۶۷۸۹"
    normalize_comment_without_punck = normalize_comment.translate(str.maketrans('', '', punctuation_chars))
    input_tokens = word_tokenize(normalize_comment_without_punck)
    stopwords_set = set(stopwords_list())
    clean_tokens = [token for token in input_tokens if token not in stopwords_set]
    lemmatizer = Lemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in clean_tokens]
    token_counts = Counter(lemmatized_tokens)
    frequent_token = sorted(token_counts.items(), key=lambda x: x[1], reverse=True)
    return frequent_token[0][0]
