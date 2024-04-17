import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
Source_data=pd.read_csv("diabetes_prediction_dataset.csv")
Source_data["gender"]=OrdinalEncoder().fit_transform(Source_data[["gender"]])
Source_data["smoking_history"]=OrdinalEncoder().fit_transform(Source_data[["smoking_history"]])
Source_data.drop_duplicates(inplace=True)
Source_data.to_csv('Source_data.csv',index=False)
