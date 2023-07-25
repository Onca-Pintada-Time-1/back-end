import joblib

model = joblib.load('app/utils/XGBModel.pkl')

importances = model.feature_importances_
importances_list = importances.tolist()


async def retrieveData():
    data = {f"Feature_{i}": importance for i, importance in enumerate(importances_list)}
    sorted_data = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
    return sorted_data
