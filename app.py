
import streamlit as st
import torch
from googletrans import Translator
from diffusers import StableDiffusionPipeline, DiffusionPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video
import subprocess
import os

# Cache the image model loading function
@st.cache_resource
def load_image_model():
    model_id = "stabilityai/stable-diffusion-2"
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    return model.to(device)

# Cache the video model loading function
@st.cache_resource
def load_video_model():
    model_id = "damo-vilab/text-to-video-ms-1.7b"
    model = DiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, variant="fp16")
    model.scheduler = DPMSolverMultistepScheduler.from_config(model.scheduler.config)
    model.enable_model_cpu_offload()
    return model

# Load models
image_model = load_image_model()
video_model = load_video_model()

# Translate other language input to English
def get_translation(text, dest_lang='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=dest_lang)
    return translated_text.text

# Returns generated image
def image_generator(prompt):
    with torch.no_grad():
        image = image_model(prompt).images[0]
    return image

# Returns path to generated video
def video_generator(prompt, length=5):
    video_frames = video_model(
        prompt=prompt,
        num_frames=length*5,
        num_inference_steps=10,
        guidance_scale=6.5
    ).frames
    frame_rate = 5  # Frames per second (FPS) for the video
    video_path = export_to_video(video_frames[0], fps=frame_rate)
    return video_path

# Main Page
def main_page():
    st.title("Media Generator")

    # Create two columns for layout
    col1, col2 = st.columns(2)

    with col1:
        st.header("Input")
        text_input = get_translation(st.text_input("Enter some text:", key="text_input"),'en')
        media_type = st.radio("Select media type:", ("Image", "Video"))
        if(media_type == 'Video'):
          video_length = st.number_input("Enter the length of the video (seconds):", min_value=1, step=1)

        if st.button("Generate"):
            st.session_state["current_prompt"] = text_input

            # Clear previous generation results
            if "generated_image" in st.session_state:
                del st.session_state["generated_image"]
            if "generated_video" in st.session_state:
                del st.session_state["generated_video"]

            # Generate new content based on the selected media type
            if media_type == "Image":
                st.session_state["generated_image"] = image_generator(text_input)
                st.session_state["generated_media_type"] = "Image"
            else:
                st.session_state["generated_video"] = video_generator(text_input, length=video_length)
                st.session_state["generated_media_type"] = "Video"

            st.session_state["last_prompt"] = text_input

    with col2:
        st.header("Output")
        if "generated_media_type" in st.session_state:
            if st.session_state["generated_media_type"] == "Image":
                image = st.session_state["generated_image"]
                st.image(image, caption="Generated Image")
                st.download_button(
                    label="Download Image",
                    data=image.tobytes(),  # Convert the image to bytes
                    file_name="generated_image.png",
                    mime="image/png"
                )
            else:
                video_path = st.session_state["generated_video"]

                # converting mp4 to h264
                input_file = video_path
                output_file = '/content/output.mp4'

                if(os.path.exists(output_file)):
                    os.remove(output_file)

                command = [
                    'ffmpeg',
                    '-i', input_file,
                    '-c:v', 'libx264',
                    '-crf', '23',
                    '-preset', 'medium',
                    output_file
                ]

                subprocess.run(command, check=True)

                st.video(open(output_file, "rb").read())
                st.download_button(
                    label="Download Video",
                    data=open(output_file, "rb").read(),  # Read the video file
                    file_name="generated_video.mp4",
                    mime="video/mp4"
                )

if __name__ == "__main__":
    main_page()
