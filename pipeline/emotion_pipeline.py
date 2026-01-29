import logging
import cv2
from video_loader import VideoLoader
from frame_extractor import FrameExtractor
from emotion_analyzer import EmotionAnalyzer
from result_writer import ResultWriter
from pathlib import Path

class EmotionPipeline:
    def __init__(self):
        self.analyzed_emotion = []
    def run_pipeline(self, input_path:Path):
        '''
        Connects all parts of code together
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
        

            

