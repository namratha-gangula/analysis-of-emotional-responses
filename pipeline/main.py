import argparse
import logging
from emotion_pipeline import EmotionPipeline
from pathlib import Path

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting main")
    parser = argparse.ArgumentParser(description="Arguments to provide the path")
    parser.add_argument("--input", required=True, help="Provide the path to the video.")
    parser.add_argument("--output", required=False, help="Provide the output folder path where the results need be stored.")
    args = parser.parse_args()
    pipeline_object = EmotionPipeline()
    pipeline_object.run_pipeline(Path(args.input), args.output)




if __name__ == "__main__":
    main()