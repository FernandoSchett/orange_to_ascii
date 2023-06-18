import sys
import os

# Importing libraries
from classes.video_to_ascii_converter import video_to_ascii_converter

if __name__ == "__main__":
    if len(sys.argv) != 2:
        error_msg = "Arguments invalid, try: python3 " + os.path.basename(os.path.abspath(__file__)) + " <path_to_file>"
        raise ValueError(error_msg)
    converter = video_to_ascii_converter(sys.argv[1], 80)
    converter.convert()
