import pandas as pd

data = pd.read_csv('../data/taghche.csv')


def mean_rating(book_name):
    filtered_data = data[data['bookname'] == book_name]
    return filtered_data['rate'].mean()


mean_rating('آشپزخانه')
