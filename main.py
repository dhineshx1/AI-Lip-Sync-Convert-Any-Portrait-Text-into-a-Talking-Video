from text_to_audio import TextToSpeech as TTS
from audio_image_to_video import InferenceRunner

class Generater:
    def __init__(self, text, audio_output="output/audio.mp3", image="data/img.jpeg", result_dir="results"):
        
        self.text = text
        self.audio_output = audio_output
        self.image = image
        self.result_dir = result_dir
        self.tts = TTS()

    def generate_audio(self):
        """
        Converts text to speech and saves the audio file.
        Returns True if successful, False otherwise.

        """
        try:
            success = self.tts.convert_text_to_audio(self.text, self.audio_output)
            return success
        except Exception as e:
            print(f"Error generating audio: {e}")
            return False

    def generate_video(self):
        """
        Generates a video using the image and generated audio.
        Returns True if successful, False otherwise.
        """
        try:
            inference = InferenceRunner(img=self.image, audio=self.audio_output, result_dir=self.result_dir)
            success = inference.run_inference()
            
            return success
        except Exception as e:
            print(f"Error generating video: {e}")
            return False

    def run(self):
        """
        Runs the full process: Text-to-Speech and then Video Generation.
        """
        if self.generate_audio():
            success = self.generate_video()

            if success:
                print("Conversion Successful!")
                return  True
            else:
                print("Video generation failed.")
                return False
        else:
            print("Audio generation failed.")
            return False
