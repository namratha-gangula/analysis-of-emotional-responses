from pathlib import Path
import logging

class VideoLoader:
    @staticmethod    
    def user_input(path: Path) -> bool:
        '''
        Takes the path from the user to find the video that needs to be processed
        '''
        video_name = path.name
        logging.info(f"This is the name of the video: {video_name} ")
        if not video_name.lower().endswith(".mp4"):
            logging.warning(f"Unsupported file type: {video_name.endswith}")
            return False
        return True
        