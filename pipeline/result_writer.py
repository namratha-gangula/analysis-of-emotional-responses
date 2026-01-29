#store the results in the csv format
#what columns will the csv contain? video_name, video_timestamp, dominant_emotion, confidence
import pandas as pd
from pathlib import Path

class ResultWriter:
    @staticmethod
    def output_path(video_path:Path):
        video_file_name = video_path.stem
        results_output = Path("results")
        results_output.mkdir(exist_ok=True)
        output = results_output/f"{video_file_name}_emotion.CSV"
        return output

    @staticmethod
    def writeCSV(results:list[dict], output_path:Path):
        '''
        Return the CSV file
        '''
        rows = []
        for frame in results:
            face = frame[0]
            rows.append(face['emotion'])
        df = pd.DataFrame(rows)
        mean_series = df.mean()
        dominant_emotion = mean_series.idxmax()
        mean_series_to_dict = mean_series.to_dict()
        mean_series_to_dict['dominant_emotion'] = dominant_emotion
        mean_data_frame = pd.DataFrame([mean_series_to_dict])
        mean_data_frame.to_csv(output_path, index=False)