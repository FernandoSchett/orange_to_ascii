import cv2
import time
from PIL import Image

class video_to_ascii_converter:
    
    def __init__(self, video_path, width):
        self.ascii_chars = '@%#*+=-:. '  # String containing ASCII characters from darkest to lightest
        self.video_path = video_path  # Path to the video file
        self.width = width  # Width of the ASCII art representation

    def map_to_ascii(self, gray_val):
        return self.ascii_chars[gray_val * len(self.ascii_chars) // 256]  # Map grayscale value to ASCII character

    def convert(self):
        cap = cv2.VideoCapture(self.video_path)  # Open the video file
        while cap.isOpened():
            ret, frame = cap.read()  # Read a frame from the video
            if not ret:
                break

            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))  # Convert frame to grayscale using OpenCV
            img = img.resize((self.width, int(self.width * img.height / img.width // 2)))  # Resize image while maintaining aspect ratio
            ascii_str = ''

            for y in range(img.height):
                for x in range(img.width):
                    ascii_str += self.map_to_ascii(img.getpixel((x, y)))  # Map each pixel to an ASCII character
                ascii_str += '\n'  # Add newline character at the end of each row

            print(ascii_str)  # Print the ASCII art representation of the frame

            time.sleep(0.03)  # Wait for a while before processing the next frame
            print('\033c')  # Clear the screen using escape sequence

        cap.release()  # Release the video capture
