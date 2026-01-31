"""
Pytests to check the frame extraction functionality.
"""
import pytest
import numpy as np
from unittest.mock import MagicMock, patch
from pipeline.frame_extractor import FrameExtractor

def test_frame_extractor():
    """
    Detects if the frames are getting exxtracted from a video file.
    Args:
    Returns:
    Example:
    """
    fake_frame = np.zeros((480, 640, 3), dtype=np.uint8)
    fake_capture = MagicMock()
    fake_capture.read.side_effect = [
        (True, fake_frame),
        (True, fake_frame),
        (False, None),
    ]
    with patch("pipeline.frame_extractor.cv2.VideoCapture", return_value = fake_capture):
        frames = FrameExtractor.extract_frame("fake/path/video.mp4")
    assert isinstance(frames, list)
    assert len(frames) == 2
    assert all(frame is not None for frame in frames)

def test_frame_extractor_empty_video():
    with patch("cv2.VideoCapture") as mock_capture:
        mock_cap = MagicMock()
        mock_cap.read.return_value = (False, None) #empty video
        mock_capture.return_value = mock_cap

        frames = FrameExtractor.extract_frame("fake/path/video.mp4")
    
    assert frames == []
