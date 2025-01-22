import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

class ModelHandler:
    def __init__(self):
        self.data = None
        self.model = None
        self.data_loaded = False

    def load_data(self, data):
        # Preprocessing: Impute missing values
        self.data = data.copy()
        imputer = SimpleImputer(strategy="mean")
        numeric_cols = self.data.select_dtypes(include=["float64"]).columns
        self.data[numeric_cols] = imputer.fit_transform(self.data[numeric_cols])
        
        # Encode the target variable
        label_encoder = LabelEncoder()
        self.data["Downtime"] = label_encoder.fit_transform(self.data["Downtime"])
        
        self.data_loaded = True

    def train_model(self):
        if not self.data_loaded:
            return None

        # Define features and target
        X = self.data[["Coolant_Temperature", "Torque"]]
        y = self.data["Downtime"]

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train the model
        self.model = LogisticRegression()
        self.model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = self.model.predict(X_test)
        metrics = {
            "accuracy": accuracy_score(y_test, y_pred),
            "f1_score": f1_score(y_test, y_pred)
        }
        return metrics

    def predict(self, input_data):
        if not self.model:
            return None
        
        # Convert input data to a DataFrame
        input_df = pd.DataFrame([input_data])
        prediction = self.model.predict(input_df)
        confidence = self.model.predict_proba(input_df).max()
        return {
            "Downtime": "Machine_Failure" if prediction[0] == 1 else "No_Machine_Failure",
            "Confidence": round(confidence, 2)
        }
