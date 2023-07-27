import pandas as pd

url = "https://media.githubusercontent.com/media/Iagoakiosaito/dataset-pd/main/creditcard.csv"


def readCSV():
    df = pd.read_csv(url, on_bad_lines='skip')

    df = df.astype(float)
    df['Class'] = df['Class'].astype(int)

    return df