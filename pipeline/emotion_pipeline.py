import logging
import cv2
from pipeline.video_loader import VideoLoader
from pipeline.frame_extractor import FrameExtractor
from pipeline.emotion_analyzer import EmotionAnalyzer
from pipeline.result_writer import ResultWriter
from pathlib import Path

class EmotionPipeline:
    def __init__(self):
        self.analyzed_emotion = []
    def run_pipeline(self, input_path:Path):
        '''
        Emotion pipeline binds all parts of the code together.
        1) Sends the video to the video loader
        2) If the video exists, the video is converted to frames in frame_extractor.py
        3) Emotion in each frame is analyzed by emotion_analyzer.py
        4) Mean of the emotions is found and the result along with the dominant emotion in the video
        is stored in a CSV format inside the results folder by result_writer.py
        Args:
            Takes the path provided by the user.
        '''
        logging.info("We are in emotion pipeline")
        video_exists = VideoLoader.user_input(input_path)
        if video_exists:
            frames = FrameExtractor.extract_frame(input_path)
            for frame in frames:
                if frame is None:
                    continue
                try:
                    self.analyzed_emotion.append(EmotionAnalyzer.analyze_emotion(frame))
                except Exception as e:
                    logging.warning(f"Skipping frame: {e}")
        
        path_to_store_results = ResultWriter.output_path(input_path)
        ResultWriter.writeCSV(self.analyzed_emotion, path_to_store_results)
        

            

