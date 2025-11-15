# opencv-subtitle-generator
A Python tool that adds customizable subtitles to videos using OpenCV. Supports text positioning, styling, and saving frames with a keypress.

# 🎬 OpenCV Subtitle Generator

A Python tool that adds **customizable subtitles** to videos using OpenCV.  
Supports text positioning, timed subtitles, and saving frames with a keypress.

Built as part of my Computer Vision practice (1st Year B.Tech IT, DTU).

---

## 🚀 Features

### ✔ Custom Subtitle Input
- Add any number of subtitles  
- Each subtitle contains:
  - Text  
  - Start frame  
  - End frame  

### ✔ Subtitle Customization
- Choose subtitle position (x, y)  
- White background with black text for clear visibility  
- Font, size, and thickness can be modified inside the code  

### ✔ Frame Saving
- Press **`s`** to save the current frame  
- Saved frames appear in the **`/saved_frames`** directory  

### ✔ Interactive Playback
- Subtitles appear in real-time during video playback  
- Press **`q`** to quit at any time  

### ✔ Automatic Output File
- Output video with subtitles is saved as **`output_video.mp4`**

---

## 🛠 Tech Stack
- Python  
- OpenCV  
- OS module  

---

## 📦 Dependencies

Install OpenCV:

pip install opencv-python

## ▶️ How to Run
# Run the Python script:
  python subtitle_overlay.py
  When prompted, enter:
    Video input path
    Subtitle position (x, y)
    Number of subtitles
    Subtitle text + start frame + end frame
  During video playback:
    Press s → save the current frame
    Press q → quit playback


Feel free to fork this project, suggest improvements, or build on top of it!
