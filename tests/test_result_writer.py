from pathlib import Path
from unittest.mock import patch
import pandas as pd

from pipeline.result_writer import ResultWriter

def test_result_writer(tmp_path):
    fake_results = [
        [{
            "emotion": {
                "angry": 0.0,
                "happy": 80.0,
                "sad": 10.0,
                "neutral": 10.0
            }
        }],
        [{
            "emotion": {
                "angry": 0.0,
                "happy": 90.0,
                "sad": 5.0,
                "neutral": 5.0
            }
        }]
    ]
    output_path = tmp_path/ "results.csv"
    df = ResultWriter.writeCSV(fake_results, output_path)

    assert df is not None
    assert "happy" in df.columns
    assert "sad" in df.columns
    assert "neutral" in df.columns
    assert "dominant_emotion" in df.columns

    assert df.loc[0, "dominant_emotion"] == "happy"


def test_result_writer_empty_results(tmp_path):
    output_path = tmp_path/"results.csv"
    with patch("pandas.DataFrame.to_csv") as mock_to_csv:
        ResultWriter.writeCSV([], output_path)
        mock_to_csv.assert_not_called()
