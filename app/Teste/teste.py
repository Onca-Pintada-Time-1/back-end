from collections import Counter

import pandas as pd
from fastapi import APIRouter
from imblearn.over_sampling import BorderlineSMOTE
from sklearn.model_selection import train_test_split
import requests
from io import StringIO

url = "https://drive.google.com/file/d/1ZSYC8leY7MyMqS3dCehkkZLZej_7ON4E/view?usp=sharing"

file_id = url.split('/')[-2]
dwn_url = 'https://drive.google.com/uc?export=download&id=' + file_id
url2 = requests.get(dwn_url).text
csv_raw = StringIO(url2)
df = pd.read_csv(csv_raw)
print(df.head())

router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}
