import argparse
import json
import logging
import time
import numpy as np
import pandas as pd
import yaml
from datetime import datetime

def setup_logging(log_file):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

def write_metrics(output_path, metrics):
    with open(output_path, 'w') as f:
        json.dump(metrics, f, indent=2)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--config', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--log-file', required=True)
    args = parser.parse_args()

    setup_logging(args.log_file)
    logger = logging.getLogger(__name__)

    start_time = time.time()
    logger.info(f"Job started at {datetime.now()}")

    version = "v1"

    try:
        # Load config
        with open(args.config, 'r') as f:
            config = yaml.safe_load(f)

        required_fields = ['seed', 'window', 'version']
        for field in required_fields:
            if field not in config:
                raise ValueError(f"Missing required config field: {field}")

        seed = config['seed']
        window = config['window']
        version = config['version']

        np.random.seed(seed)
        logger.info(f"Config loaded — seed={seed}, window={window}, version={version}")

        # Load dataset
        try:
            df = pd.read_csv(args.input)
        except FileNotFoundError:
            raise FileNotFoundError(f"Input file not found: {args.input}")
        except Exception as e:
            raise ValueError(f"Invalid CSV format: {e}")

        if df.empty:
            raise ValueError("Input file is empty")

        if 'close' not in df.columns:
            raise ValueError("Missing required column: close")

        logger.info(f"Rows loaded: {len(df)}")

        # Rolling mean
        df['rolling_mean'] = df['close'].rolling(window=window).mean()
        logger.info(f"Rolling mean computed with window={window}")

        # Signal generation
        df_valid = df.dropna(subset=['rolling_mean'])
        df_valid = df_valid.copy()
        df_valid['signal'] = (df_valid['close'] > df_valid['rolling_mean']).astype(int)
        logger.info("Signal generated")

        # Metrics
        rows_processed = len(df)
        signal_rate = round(float(df_valid['signal'].mean()), 4)
        latency_ms = int((time.time() - start_time) * 1000)

        metrics = {
            "version": version,
            "rows_processed": rows_processed,
            "metric": "signal_rate",
            "value": signal_rate,
            "latency_ms": latency_ms,
            "seed": seed,
            "status": "success"
        }

        write_metrics(args.output, metrics)
        logger.info(f"Metrics: {metrics}")
        logger.info(f"Job completed successfully at {datetime.now()}")
        print(json.dumps(metrics, indent=2))

    except Exception as e:
        latency_ms = int((time.time() - start_time) * 1000)
        error_metrics = {
            "version": version,
            "status": "error",
            "error_message": str(e)
        }
        write_metrics(args.output, error_metrics)
        logger.error(f"Job failed: {e}")
        print(json.dumps(error_metrics, indent=2))
        exit(1)

if __name__ == "__main__":
    main()