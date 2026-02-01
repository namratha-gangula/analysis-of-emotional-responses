import argparse
import logging
from pipeline.emotion_pipeline import EmotionPipeline
from pathlib import Path

def main():
    """
    Starting point of the code.
    Takes the input path from the user and sends it to the emotion_pipeline.py for processing.
    """
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting main")
    parser = argparse.ArgumentParser(description="Arguments to provide the path")
    parser.add_argument("--input", required=True, help="Provide the path to the video.")
    args = parser.parse_args()
    pipeline_object = EmotionPipeline()
    pipeline_object.run_pipeline(Path(args.input))




if __name__ == "__main__":
    main()