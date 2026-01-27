#store the results in the csv format
#what columns will the csv contain? video_name, video_timestamp, dominant_emotion, confidence
import logging

class resultWriter:
    def __init__(self):
        pass
    def writeCSV(results:list[dict], output_path:str) -> None:
        '''
        Return the CSV file containing the columns: video_name, video_timestamp, dominant_emotion
        '''
        pass 