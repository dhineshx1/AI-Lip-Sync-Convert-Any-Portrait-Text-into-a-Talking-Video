from text_to_audio import TextToSpeech
from audio_image_to_video import InferenceRunner

class Generater:
    def __init__(self, text, audio_output="output/audio.mp3", image="data/img.jpeg", result_dir="results"):
        
        self.text = text
        self.audio_output = audio_output
        self.image = image
        self.result_dir = result_dir
        self.tts = TextToSpeech(api_key="your_api_key", voice_id="MF4J4IDTRo0AxOO4dpFR")

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
            if self.generate_video():
                print("Conversion Successful!")
            else:
                print("Video generation failed.")
        else:
            print("Audio generation failed.")

# Example usage
if __name__ == "__main__":
    text = """
        Namaste Mathangi! My name is Anika, and I am here to guide you through managing your credit 
        card dues. Mathangi, as of today, your credit card bill shows an amount due of INR 5,053 which 
        needs to be paid by 31st December 2024. 
        Missing this payment could lead to two significant consequences: 
        First, a late fee will be added to your outstanding balance. 
        Second, your credit score will be negatively impacted, which may affect your future borrowing 
        ability. 
        Make your payment by clicking the link here... Pay through UPI or bank transfer. Thank you!
    """

    convert = Generater(text)
    convert.run()
