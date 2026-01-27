import logging
from video_loader import VideoLoader
from pathlib import Path

class EmotionPipeline:
    def __init__(self):
        pass
    def run_pipeline(self, input_path:Path, output_path:Path):
        '''
        Connects all parts of code together
        '''
        logging.info("We are in emotion pipeline")
        VideoLoader.user_input(input_path)
