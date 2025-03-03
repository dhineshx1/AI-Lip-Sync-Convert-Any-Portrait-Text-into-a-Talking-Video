import streamlit as st
import os
from main import Generater  
import glob

def save_uploaded_file(uploaded_file, folder="data"):
    """Save uploaded file to the specified folder and return the file path."""
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getvalue())
    return file_path

def main():
    st.set_page_config(page_title="Image & Text to Video", layout="centered")
    st.title("📽️ Image & Text to Video App")
    st.write("Upload an image and enter text to generate a video.")
    
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], help="Accepted formats: PNG, JPG, JPEG")
    user_text = st.text_area("Enter text for the video", help="This text will be used in the generated video.")
    
    if uploaded_file and user_text:
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
        
        if st.button("Generate Video 🎬"):
            with st.spinner("Generating video... This may take a moment."):
                image_path = save_uploaded_file(uploaded_file)
                
                try:
                    convertor = Generater(image=image_path, text=user_text)
                    success = convertor.run()
                    
                    
                    if success:
                        st.success("✅ Video generated successfully!")

                    else:
                        st.error("❌ Failed to generate video. Please try again.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
    else:
        st.warning("⚠️ Please upload an image and enter text before proceeding.")

if __name__ == "__main__":
    main()


