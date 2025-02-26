import subprocess
class InferenceRunner:
    def __init__(self, img="/data/img.jpeg", audio="/data/input_audio.mp3", result_dir="./output"):
        self.img = img
        self.audio = audio
        self.result_dir = result_dir

    def run_inference(self):
        """
        run the inference in inference file 
        enhance using gfpgan
        
        """
        
        command = [
            "python","inference/inference.py",
            "--driven_audio", self.audio,
            "--source_image", self.img,
            "--result_dir", self.result_dir,
            "--still",
            "--preprocess", "full",
            "--enhancer", "gfpgan"
        ]

        try:
            subprocess.run(command, check=True)
            print("Inference completed successfully!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error during execution: {e}")
            return False
        except FileNotFoundError as e:
            print(f"Error: inference.py or Python executable not found. {e}")
            return False
