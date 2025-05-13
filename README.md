
# 🧊 Previsão de Vendas de Sorvete com Machine Learning

Este projeto utiliza aprendizado de máquina para prever as vendas de sorvete com base na temperatura diária. Ideal para sorveterias otimizarem sua produção, reduzindo desperdício e aumentando lucro. 🏖️🍦

## 🎯 Objetivos do Projeto

✅ Construir um modelo de regressão para prever vendas com base na temperatura  
✅ Utilizar MLflow para rastreamento de experimentos  
✅ Implementar um pipeline de ML estruturado  
✅ Expor uma API para previsões em tempo real  
✅ Implantar o modelo na nuvem (opcional)

## 📁 Estrutura do Projeto

```
├── data/                  # Base de dados com temperatura e vendas
├── notebooks/             # Análises exploratórias e desenvolvimento inicial
├── pipeline/              # Scripts com pipeline de treinamento e validação
├── mlruns/                # Registro automático dos experimentos (MLflow)
├── api/                   # API com FastAPI para servir o modelo
├── models/                # Modelos treinados (.pkl)
├── README.md              # Documentação do projeto
```

## 🧪 Modelagem

- **Regressão Linear Simples** usando `scikit-learn`
- Rastreio de experimentos com `MLflow`
- Pipeline treinado com `train_test_split`, `StandardScaler` e `LinearRegression`

## 📊 Dataset

Pequeno dataset fictício para simular a relação entre temperatura e vendas de sorvete.

| Temperatura (°C) | Vendas (unid.) |
|------------------|----------------|
| 30               | 200            |
| 35               | 250            |
| 40               | 300            |

## 📦 Como Rodar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/sorvete-previsao-ml.git
cd sorvete-previsao-ml
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Treine o modelo:
```bash
python pipeline/train.py
```

4. Inicie a API:
```bash
uvicorn api.main:app --reload
```

5. Faça uma requisição:
```json
POST /predict
{
  "temperatura": 35
}
```

## 📌 Prints do Projeto

*Adicione aqui capturas de tela do notebook, MLflow, e API em funcionamento.*

## 🤖 Tecnologias Utilizadas

- Python, Pandas, Numpy
- scikit-learn, MLflow
- FastAPI
- matplotlib, seaborn

## 🚀 Possibilidades Futuras

- Melhorar o modelo com dados reais/históricos
- Adicionar validação cruzada e outros algoritmos
- Deploy completo com Docker e Cloud

---

Projeto desenvolvido como parte do desafio da [DIO](https://www.dio.me).
