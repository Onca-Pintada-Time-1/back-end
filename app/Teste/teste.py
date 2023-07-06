from collections import Counter

import pandas as pd
from fastapi import APIRouter
from imblearn.over_sampling import BorderlineSMOTE
from sklearn.model_selection import train_test_split

url = "https://media.githubusercontent.com/media/Iagoakiosaito/dataset-pd/main/creditcard.csv"
router = APIRouter()
df = pd.read_csv(url, on_bad_lines='skip')


X = df.drop(['Class'], axis=1)
Y = df["Class"]
# getting just the values for the sake of processing
# (it's a numpy array with no columns)
xData = X.values
yData = Y.values

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)  # 80% Treino e 20% Teste
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2,
                                                  random_state=42)  # do Treino 20% é Validação

attributes = pd.DataFrame(X_train)
labels = pd.Series(y_train, name='class')
df_train = pd.concat([attributes, labels], axis=1)

smote = BorderlineSMOTE(k_neighbors=3, m_neighbors=2, sampling_strategy='minority')
X_smote, y_smote = smote.fit_resample(X, Y)

df_train_smt = pd.DataFrame(X_smote, columns=df_train.columns)
df_train_smt['class'] = y_smote


@router.get("/api")
async def readCSV():
    try:

        # Frequencia das classes com gráfico de barras
        freq_class = sorted(Counter(df_train['class']).items())
        return {"Normal": freq_class[0][1], "Fraude": freq_class[1][1]}

    except Exception as e:
        return {"error": str(e)}


@router.get("/scatterData")
async def scatterData():
    x = df_train_smt['V14']
    y = df_train_smt['V4']
    return {"V14": x, "V4": y}
