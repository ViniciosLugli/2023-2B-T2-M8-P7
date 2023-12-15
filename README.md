# OpenAI Audio Processor

## Description

This project provides a comprehensive solution for audio processing that includes speech-to-text translation, text translation into Brazilian Portuguese, and text-to-speech conversion. It leverages OpenAI's powerful models to perform these tasks.

## Features

-   **Speech to Text**: Converts audio files to text using OpenAI's Whisper model.
-   **Text Translation**: Translates the transcribed text into Brazilian Portuguese.
-   **Text to Speech**: Converts translated text back into speech using OpenAI's text-to-speech model.
-   **Audio Playback**: Plays the original and translated audio.

## Requirements

-   Python 3.6+
-   OpenAI API Key
-   Required Python libraries: `openai`, `python-dotenv`, `playsound`

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Place your OpenAI API key in a `.env` file with the variable `OPENAI_API_KEY`.

## Usage

Run the script using the command:

```
python main.py <path_to_audio_file>
```

## Configuration

-   The script expects an environment variable `OPENAI_API_KEY` for API authentication.
-   Audio files should be in MP3 format and placed in the `/data` directory.

## Output

-   The transcribed text is saved in `output/text_raw.txt`.
-   The translated text is saved in `output/text_translated.txt`.
-   The synthesized speech is saved in `output/audio_raw.mp3` and `output/audio_translated.mp3`.

## Demo
[demo](https://github.com/ViniciosLugli/2023-2B-T2-M8-P7/assets/40807526/0d324b86-829a-4f9f-b43e-cbce72b17fc2)

You can find the texts and listen to the audios on [output folder](output/)
