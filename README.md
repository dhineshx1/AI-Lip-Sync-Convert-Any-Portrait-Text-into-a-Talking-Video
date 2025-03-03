# AI Lip Sync: Convert Any Portrait & Text into a Talking Video! 

- Bring static images to life! Our AI-powered tool leverages SadTalker and gTTS to generate realistic talking videos from portraits and text. Just input an image and text—our model does the rest! 🤯🎥

## Features

- Converts **text** into speech using a TTS model.
- Generates a **talking head video** by syncing an image with the generated audio.
- Uses **pre-trained AI models** for realistic facial animation.

---

## DEMO APP

## 📌 Example  

| **Input (Text and Portrait Image)** | **Output (Lip-Synced Video)** |
|----------------------------|--------------------------------|
| ![Input Image](data\26pe45ko.png) | ![Output Video](results/2025_03_03_23.10.12.mp4) |


## Setup Instructions

### ** Clone the Repository**

```sh
git clone https://github.com/dhineshx1/Audio-and-Image-to-Video
cd Audio-and-Image-to-Video
```

### ** Install Dependencies**

```


conda create -n venv python=3.8

conda activate venv

pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113

conda install ffmpeg

pip install -r requirements.txt

### Coqui TTS is optional for gradio demo.
### pip install TTS

```

### ** Download Required Models**

Some pre-trained models were removed due to size constraints. Download them manually:

- **Checkpoints (Facial Animation Model)**

  - 🔗 [Download Here](https://drive.google.com/file/d/1gwWh45pF7aelNP_P78uDJL8Sycep-K7j/view)
  - Extract to `checkpoints/` inside the project folder.

- **GFPGAN (Face Enhancement Model)**
  - 🔗 [Download Here](https://drive.google.com/file/d/19AIBsmfcHW6BRJmeqSFlG5fL445Xmsyi/edit)
  - Extract to `gfpgan/` inside the project folder.

```sh
# Example structure after downloading models
your-repo/
│── checkpoints/   # Pre-trained models
│── gfpgan/        # Face enhancement models
│── src/           # Source code
│── output/        # Generated audio and video
│── requirements.txt
│── README.md
```

---



## How to Use

### \*\*Run the main.py

```sh
python main.py
```

This will:

1. Convert the **reminder text** into speech (`output_audio.mp3`).
2. Use a **static image** to generate a talking-head video.
3. Save the final video in the `results/` folder.

---

## Customization

- **Modify the Reminder Text**  
  Edit the `main.py` file and change the `text` variable to generate reminders for different users.
- **Change the Source Image**  
  Replace `data/img.jpeg` with a new image.

---

## Troubleshooting

### **Error: Missing Checkpoints or GFPGAN**

- Make sure you downloaded the required models and placed them in the correct directories.

### **Error: Python Not Found**

- Ensure Python 3.8+ is installed. Check with:
  ```sh
  python --version
  ```

### **Error: Module Not Found**

- Install missing dependencies:
  ```sh
  pip install -r requirements.txt
  ```

## **Acknowlegement**

- We used SadTalker open source audio to video converter for this project. we appreciate the work.
- SadTalker Link: https://sadtalker.github.io/

## 📜 License

This project is open-source under the **MIT License**.
