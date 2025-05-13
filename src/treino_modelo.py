
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import mlflow
import mlflow.sklearn
from pipeline import criar_pipeline

# Dados
df = pd.read_csv('inputs/dados_vendas.csv')
X = df[['temperatura']]
y = df['vendas']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pipeline e treinamento
pipeline = criar_pipeline()
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

# Log com MLflow
with mlflow.start_run():
    mlflow.log_param("pipeline", "StandardScaler + LinearRegression")
    mlflow.log_metric("r2_score", r2_score(y_test, y_pred))
    mlflow.log_metric("rmse", mean_squared_error(y_test, y_pred, squared=False))
    mlflow.sklearn.log_model(pipeline, "modelo_sorvete")
