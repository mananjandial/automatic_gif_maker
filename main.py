import logging
from transcriber import transcribe_audio
from gif_creator import create_gifs
from settings import VIDEO_PATH

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    segments = transcribe_audio(VIDEO_PATH)
    if segments:
        logging.info("Transcription Segments: %s", segments)
        gif_paths = create_gifs(VIDEO_PATH, segments)
        if gif_paths:
            logging.info("Generated GIFs: %s", gif_paths)
        else:
            logging.error("No GIFs were generated.")
    else:
        logging.error("Transcription failed, no segments available.")

if __name__ == "__main__":
    main()
