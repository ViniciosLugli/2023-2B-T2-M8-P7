import argparse
import os
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
from playsound import playsound

load_dotenv()


class AudioProcessor:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        self.speech_file_path = "output/audio"
        self.text_file_path = "output/text"

    def convert_to_text(self, file_path):
        with open(file_path, 'rb') as file:
            transcript = self.client.audio.translations.create(
                model='whisper-1',
                file=file
            )
        return transcript.text

    def write_to_file(self, transcript, file_description=""):
        with open(f'{self.text_file_path}_{file_description}.txt', "w") as file:
            file.write(transcript)
        return file

    def text_translation(self, transcript, target_language):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system",
                       "content":
                       f"You will be provided with a sentence in any language, and your task is to translate it into {target_language}."},
                      {"role": "user", "content": f"{transcript}"}],
            temperature=0.7)
        return response.choices[0].message.content

    def text_to_speech(self, file_path, output_file_description=""):
        with open(file_path, "r") as f:
            content = f.read()

        response = self.client.audio.speech.create(
            model="tts-1",
            voice="shimmer",
            input=f"{content}",
            response_format="mp3"
        )
        output_path = f"{self.speech_file_path}_{output_file_description}.mp3"
        response.stream_to_file(output_path)
        return output_path

    @staticmethod
    def play_audio(file_path):
        playsound(file_path)


def main(file_path):
    api_key = os.getenv('OPENAI_API_KEY')
    audio_processor = AudioProcessor(api_key)

    try:
        audio_transcript = audio_processor.convert_to_text(file_path)
        text_file_raw = audio_processor.write_to_file(audio_transcript, "raw")

        translation = audio_processor.text_translation(audio_transcript, "pt-br")
        text_file_translated = audio_processor.write_to_file(translation, "translated")

        speech_file_raw = audio_processor.text_to_speech(text_file_raw.name, "raw")
        speech_file_translated = audio_processor.text_to_speech(text_file_translated.name, "translated")
        audio_processor.play_audio(speech_file_raw)
        audio_processor.play_audio(speech_file_translated)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TTS and STT using OpenAI")
    parser.add_argument("file", help="Path to base audio file")
    args = parser.parse_args()
    main(args.file)
