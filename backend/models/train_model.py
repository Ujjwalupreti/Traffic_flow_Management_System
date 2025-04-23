import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib
import os

class Train_Model:   
     
    def preprocess_data(self,csv_path="backend/data/traffic_data_1.csv")->int:
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"{csv_path} not found")

        df = pd.read_csv(csv_path)
        df['date'] = pd.to_datetime(df['date'],dayfirst=True)
        df['day'] = df['date'].dt.day
        df['month'] = df['date'].dt.month
        df['year'] = df['date'].dt.year

        features = ['day','month','year','hour']
        target = ['vehicles']

        X = df[features]
        Y = df[target]

        return X, Y

    @staticmethod
    def train_model(self)->None:
        X, Y = self.preprocess_data()

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=40)

        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, Y_train.values.ravel())

        score = model.score(X_test, Y_test)
        print("Model Score:", score)
        joblib.dump(model,'trained_set.pkl')

    def predict_traffic(self,day=1, month=1, year=2025,hour=0):
        model = joblib.load('trained_set.pkl')
        features = pd.DataFrame([[day, month, year,hour]], columns=['day','month','year','hour'])
        prediction = model.predict(features)
        return prediction

if __name__ == '__main__':
    List = Train_Model()