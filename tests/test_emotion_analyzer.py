import numpy as np
from unittest.mock import patch
from pipeline.emotion_analyzer import EmotionAnalyzer

def test_emotion_analyzer_sucess():
    fake_frame = np.zeros((480, 640, 0), dtype=np.uint8)

    fake_output = [
        {
            "dominant_emotion":"happy",
            "emotion": {
                "angry": 1.0,
                "happy": 90.0,
                "sad": 2.0,
                "neutral": 7.0
            }
        }
    ]
    with patch("pipeline.emotion_analyzer.DeepFace.analyze") as mock_analyze:
        mock_analyze.return_value = fake_output
        result = EmotionAnalyzer.analyze_emotion(fake_frame)
    assert result is not None
    assert isinstance(result, list)
    assert result[0]["dominant_emotion"] == "happy"

def test_emotion_analyzer_deepface_error():
    fake_frame = np.zeros((480, 640, 3), dtype=np.uint8)

    with patch("pipeline.emotion_analyzer.DeepFace.analyze") as mock_analyze:
        mock_analyze.side_effect = RuntimeError("DeepFace crashed")
        result = EmotionAnalyzer.analyze_emotion(fake_frame)
        assert result is None

def test_emotion_analyzer_no_frame():
    result = EmotionAnalyzer.analyze_emotion(None)
    assert result is None