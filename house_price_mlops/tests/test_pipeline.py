import pandas as pd
from pipeline.train_model import train

def test_train_model_runs():
    try:
        train()
        assert True
    except Exception as e:
        assert False, f"Training failed: {e}"
