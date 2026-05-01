# MLOps Task - Signal Generator

## Local Run
pip install -r requirements.txt
python run.py --input data.csv --config config.yaml --output metrics.json --log-file run.log

## Docker Run
docker build -t mlops-task .
docker run --rm mlops-task

## Example metrics.json
{
  "version": "v1",
  "rows_processed": 10000,
  "metric": "signal_rate",
  "value": 0.4991,
  "latency_ms": 174,
  "seed": 42,
  "status": "success"
}