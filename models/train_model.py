import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression


df = pd.read_csv("../data/predictive_maintenance.csv")


df = df.drop(columns=["UDI","Product ID", "Failure Type"])


x = df.drop(columns=["Target"])
y = df["Target"]

numeric_features = ["Air temperature [K]", "Process temperature [K]", "Rotational speed [rpm]", "Torque [Nm]", "Tool wear [min]"]
categorical_features = ["Type"]

numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown="ignore")


preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)


Pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced"))
])



X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
Pipeline.fit(X_train, y_train)



joblib.dump(Pipeline, "predictive_maintenance_model.pkl")



print("Model training complete and saved to models/predictive_maintenance_model.pkl")
print(Pipeline.score(X_train, y_train))
print(Pipeline.score(X_test, y_test))