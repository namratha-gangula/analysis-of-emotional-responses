#extract emotion from the image
import logging
from deepface import DeepFace

class EmotionAnalyzer:
    @staticmethod
    def analyze_emotion(frame: list) -> list:
        '''
        Analyze the scores for all the emotions in the video
        Args:
            frame: A list of numpy arrays
        Returns:
            A list of dict containing the scores for each emotion. The emotion with the highest probability
            is likely the dominant emotion in a frame.
        '''
        try:
            emotion = DeepFace.analyze(
                img_path=frame,
                actions=["emotion"],
                enforce_detection=False
            )
            return emotion
        except Exception as e:
            print("Deep face error:", e)
            return None