# Video to GIF with Captions

This project demonstrates how to convert video segments into GIFs with transcribed captions using MoviePy, Whisper, and PIL.

## Features
- Transcribes audio from video using Whisper
- Generates GIFs with captions for short speech segments

## Requirements
- Python 3.7 or higher
- moviepy
- Pillow
- openai-whisper

## Setup
1. Clone the repository
    ```bash
    git clone <repository_url>
    cd project
    ```

2. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

3. Download the Whisper model (if not already available)

## Usage
1. Place your video files in the `video_samples` directory.
2. Run the script
    ```bash
    python transcribe_and_gif.py
    ```

## Example
A sample video `videotogif.mp4` is included in the `video_samples` directory for testing purposes.

## Output
Generated GIFs will be saved in the `output_gifs` directory.

## Notes
- Ensure that the `Roboto-Black.ttf` font file is available in the `assets` directory.
- Adjust the font size and other parameters in the script as needed.

## Contact
For any issues or questions, please contact [Your Name] at [your.email@example.com].
