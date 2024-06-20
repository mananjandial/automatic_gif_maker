import os
import tempfile
import moviepy.editor as mp
import whisper
import logging

def transcribe_audio(video_path):
    try:
        model = whisper.load_model("base")
        video_clip = mp.VideoFileClip(video_path)
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
            audio_path = temp_audio.name
            video_clip.audio.write_audiofile(audio_path)
        result = model.transcribe(audio_path)
        segments = result['segments']

        os.remove(audio_path)
        return segments
    except Exception as e:
        logging.error(f"Error during audio transcription: {e}")
        return []
