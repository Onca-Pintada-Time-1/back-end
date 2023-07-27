from app.utils.CSVReader import readCSV

df = readCSV()
async def most_important_features():

    pairs = {
        "v14": df['V14'].to_list(),
        "v17": df['V17'].to_list(),
        "v4": df['V4'].to_list(),
        "class": df['Class'].to_list()
    }

    return pairs


def least_important_features():

    pairs = {
        "v13": df['V13'].to_list(),
        "v22": df['V22'].to_list(),
        "class": df['Class'].to_list()
    }
    
    return pairs