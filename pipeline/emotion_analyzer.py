#extract emotion from the image
import logging
from deepface import DeepFace

class EmotionAnalyzer:
    @staticmethod
    def analyze_emotion(frame: list) -> list:
        '''
        Analyze all the emotions in the video and return the scores for each emotion
        ("angry","happy","sad")
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