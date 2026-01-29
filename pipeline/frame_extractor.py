#convert video to images
import logging
from pathlib import Path
import cv2

class FrameExtractor:
    @staticmethod
    def extract_frame(video_path: Path) -> list: # return list of frames
        '''
        Extract the frame from the video and return the result.
        Frame is a numpy array.
        Frames is a list of numpy arrays.
        '''
        frames = []
        open_video_file = cv2.VideoCapture(video_path)
        logging.info("Path given by the user to the location of the video:%s", Path(video_path).resolve())
        logging.info("Does the path exist?:%s", Path(video_path).exists())
        #check if video file was opened successfully
        if not open_video_file.isOpened():
            raise RuntimeError(f"Error:Could not open video file: {video_path}")
        else:
            logging.info("Video file opened successfully!")
        #Get video properties (eg: frame count)
        frame_count = int(open_video_file.get(cv2.CAP_PROP_FRAME_COUNT))
        #getting frames per second
        frame_per_second = open_video_file.get(cv2.CAP_PROP_FPS)
        logging.info(f"Total frames: {frame_count}, frames per second: {frame_per_second}")
        #read and display each frame of the video
        while True:
            is_frame_captured, frame = open_video_file.read()
            frames.append(frame)
            if not is_frame_captured:
                break
                #maybe add an exception here
            cv2.imshow("Video frame", frame)
            #wait for 1 min for key press to continue or exit if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
        return frames
