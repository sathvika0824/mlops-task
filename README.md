# 🤖 ML Signal Generation Pipeline

A production-ready Machine Learning pipeline that processes real Bitcoin OHLCV financial data and generates buy/sell trading signals — fully containerized with Docker! 🐳

## ✨ What This Project Does
- 📈 Processes **10,000 rows** of real Bitcoin OHLCV price data
- 🔢 Calculates **rolling mean** with configurable window size
- 💹 Generates **buy/sell signals** — 49.91% signal rate achieved
- 📊 Outputs structured **JSON metrics** with full logging
- 🐳 Fully containerized with **Docker**
- ⚙️ CLI-driven execution with **YAML configuration**
- 🔁 Full **reproducibility** with seed control

## 🛠️ Tech Stack
- Python 🐍
- Pandas 🐼
- NumPy 🔢
- PyYAML ⚙️
- Docker 🐳
- Git & GitHub 🌿

## 📊 Output Example
```json
{
  "version": "v1",
  "rows_processed": 10000,
  "metric": "signal_rate",
  "value": 0.4991,
  "latency_ms": 174,
  "seed": 42,
  "status": "success"
}
```

![Pipeline Output](Screenshot%20(251).png)

## 🚀 How to Run Locally
```bash
git clone https://github.com/sathvika0824/mlops-task
cd mlops-task
pip install -r requirements.txt
python run.py --input data.csv --config config.yaml --output metrics.json --log-file run.log
```

## 🐳 Docker Run
```bash
docker build -t mlops-task .
docker run --rm mlops-task
```

## ⚙️ Configuration (config.yaml)
```yaml
seed: 42
window: 5
version: "v1"
```

## 📁 Project Structure
```
mlops-task/
├── run.py           # Main pipeline script
├── config.yaml      # Configuration file
├── data.csv         # Bitcoin OHLCV dataset
├── requirements.txt # Dependencies
├── Dockerfile       # Docker configuration
├── metrics.json     # Output metrics
├── run.log          # Execution logs
└── README.md        # Project documentation
```

## 👩‍💻 Developer
**Kameswari Sathvika Bhallamudi**
- 🔗 LinkedIn: linkedin.com/in/sathvika-aiml
- 💻 GitHub: github.com/sathvika0824
