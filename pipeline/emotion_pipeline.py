import logging
import cv2
from video_loader import VideoLoader
from frame_extractor import FrameExtractor
from pathlib import Path

class EmotionPipeline:
    def __init__(self):
        pass
    def run_pipeline(self, input_path:Path, output_path:Path):
        '''
        Connects all parts of code together
        '''
        logging.info("We are in emotion pipeline")
        video_exists = VideoLoader.user_input(input_path)
        if video_exists:
            FrameExtractor.extract_frame(input_path)
            

