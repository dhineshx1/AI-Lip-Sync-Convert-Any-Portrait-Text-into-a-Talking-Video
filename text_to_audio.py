from elevenlabs.client import ElevenLabs

class TextToSpeech:
    def __init__(self, api_key, voice_id,output_format="mp3_44100_128",): 
        self.client = ElevenLabs(api_key=api_key,)
        self.voice_id = voice_id
        self.output_format = output_format

    def convert_text_to_audio(self, text, output_file="audio.mp3"):
        """
        Convert text to speech and save the audio file.
        :param text: The text to be converted to speech
        :param output_file: Name of the output audio file

        """
        try: 
            audio = self.client.text_to_speech.convert(
                text=text,
                voice_id=self.voice_id,
                model_id="eleven_multilingual_v2",
                output_format=self.output_format,
            )
            print(f"Audio saved as {output_file}")
            return True
        except:
            print("error in audio converter")
            return False
        