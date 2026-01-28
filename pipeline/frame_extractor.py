#convert video to images
import logging
from pathlib import Path
import cv2

class FrameExtractor:
    def __init__(self):
        pass
    def extract_frame(video_path: Path) -> list: # return list of frames
        '''
        Extract the frame from the video and return the result.
        '''
        open_video_file = cv2.VideoCapture(video_path)
        logging.info("Path given by the user to the location of the video", Path(video_path).resolve())
        logging.info("Does the path exist?:", Path(video_path).exists())
        #check if video file was opened successfully
        if not open_video_file.isOpened():
            logging.warning("Error:Could not open video file.")
        else:
            logging.info("Video file opened successfully!")
        is_frame_captured, frame = open_video_file.read()
        if is_frame_captured:
            cv2.imshow("First frame", frame)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Error could not read the frame.")