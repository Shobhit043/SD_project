# Multilingual Text to Image/Video Generator

## Overview

The **Multilingual Text to Image/Video Generator** is a Python-based application that generates images and videos from textual descriptions in multiple languages. Utilizing state-of-the-art machine learning models like Stable Diffusion, this project enables users to create media content from natural language inputs across various languages, making it accessible to a global audience.

## Features

- **Multilingual Support**: Generate images and videos from text descriptions in multiple languages using the Google Translate API.
- **Image and Video Generation**: Create high-quality images and short videos using advanced diffusion models.
- **User-Friendly Interface**: Interact with the application via a simple Streamlit-based web interface.
- **Customizable Parameters**: Adjust various parameters for image and video generation to suit specific needs.

## Technologies Used

- **Python**: The core programming language for the application.
- **Streamlit**: A web application framework to create interactive web interfaces.
- **Diffusers**: A library for diffusion models, such as Stable Diffusion.
- **Transformers**: A library for natural language processing.
- **Google Translate API**: Provides multilingual support for text input.
- **FFmpeg**: A tool for video processing.

## Installation

To install and run the project locally, follow these steps:

1. **Clone the repository:**

    ```bash
    https://github.com/Shobhit043/GAN-project.git
    cd GAN-project
    ```

2. **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Install `localtunnel` globally (for web access or running web app in colab):**

    ```bash
    npm install -g localtunnel
    ```

## Usage

To start the application, run the following command:

```bash
streamlit run app.py
```

To start the application in colab, run the following command:

```bash
!streamlit run app.py &  npx localtunnel --port 8501
```

**Follow run_app_in_colab.ipynb to get more clear instructions**

**Note : It is essential to enable gpu for fast performance in local or in colab**

## Some application images

### English Prompt

<figure>
  <img src="https://github.com/Shobhit043/GAN-project/blob/main/application%20images/ss-240802-20%3A45%3A34.png" alt="English prompt" />
</figure>

### Hindi Prompt

<figure>
  <img src="https://github.com/Shobhit043/GAN-project/blob/main/application%20images/ss-240802-20%3A46%3A25.png" alt="Hindi prompt" />
</figure>

### Japanese Prompt

<figure>
  <img src="https://github.com/Shobhit043/GAN-project/blob/main/application%20images/ss-240802-20%3A53%3A44.png" alt="Japanese prompt">
</figure>

## Sample Output of the model:
### Image
<figure>
  <img src="https://github.com/Shobhit043/GAN-project/blob/main/generated%20output%20images/ss-240802-21%3A25%3A39.png" alt="sample output image" />
</figure>

### Video
Sample video is present in the **Generated output folder** in the repository <br>

#### GIF form
![generated video converted to gif](https://github.com/Shobhit043/GAN-project/blob/main/generated%20output%20images/generated_video_in_gif_format.gif)<br>
(this video seems static but there is slight movement in the river in the actual video)
