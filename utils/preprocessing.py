import pandas as pd

data = pd.read_csv('/media/zahra/06D8A5DBD8A5C8EF/Projects/taaghcheh/data/taghche.csv')


def mean_rating(book_name):
    filtered_data = data[data['bookname'] == book_name]
    return filtered_data['rate'].mean()
