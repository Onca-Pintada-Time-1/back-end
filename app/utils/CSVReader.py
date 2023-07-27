import pandas as pd

url = "https://media.githubusercontent.com/media/Iagoakiosaito/dataset-pd/main/creditcard.csv"


def readCSV():
    df = pd.read_csv(url, on_bad_lines='skip')
    return df
