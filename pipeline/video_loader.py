from pathlib import Path
import logging

class VideoLoader:
    @staticmethod    
    def user_input(path: Path) -> bool:
        '''
        Takes the path from the user to find the video that needs to be processed
        Args:
            path: This is the path given by the user. This is the path where the video is present.
        Returns:
            bool: user_input() takes the input from the user to check if the video with .mp4 extension
            is present at the path given by the user or not. If it is present, user_input() returns true.
            Else it returns false.
        '''
        video_name = path.name
        logging.info(f"This is the name of the video: {video_name} ")
        if not video_name.lower().endswith(".mp4"):
            logging.warning(f"Unsupported file type: {video_name.endswith}")
            return False
        return True
        