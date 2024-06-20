import os
from PIL import Image, ImageDraw, ImageFont
import moviepy.editor as mp
import logging
from settings import FONT_PATH, FONT_SIZE, OUTPUT_DIR

def create_gifs(video_path, segments):
    try:
        video_clip = mp.VideoFileClip(video_path)
        gif_paths = []
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
        text_color = "white"
        caption_height = 50
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        for i, segment in enumerate(segments):
            start_time, end_time, text = segment['start'], segment['end'], segment['text']
            if end_time - start_time > 5:
                continue
            subclip = video_clip.subclip(start_time, end_time)
            frames = []
            for frame in subclip.iter_frames(fps=10, dtype='uint8'):
                img = Image.fromarray(frame)
                draw = ImageDraw.Draw(img)
                text_bbox = draw.textbbox((0, 0), text, font=font)
                text_width = text_bbox[2] - text_bbox[0]
                text_height = text_bbox[3] - text_bbox[1]
                text_x = (img.width - text_width) // 2
                text_y = img.height - caption_height - text_height
                outline_color = "black"
                draw.text((text_x, text_y), text, font=font, fill=text_color, stroke_width=2, stroke_fill=outline_color)
                frames.append(img)
            output_gif_path = os.path.join(OUTPUT_DIR, f"output_{i}.gif")
            frames[0].save(output_gif_path, save_all=True, append_images=frames[1:], duration=100, loop=0)
            gif_paths.append(output_gif_path)
        return gif_paths
    except Exception as e:
        logging.error(f"Error during GIF creation: {e}")
        return []
