# 🧏‍♂️ Speech-to-Sign-Language Translator

## 📌 Project Overview
The **Speech-to-Sign-Language Translator** is an assistive communication tool designed to bridge the gap between hearing individuals and the Deaf/Hard of Hearing community.  
It takes **live speech or recorded audio** as input, converts it into **text**, and then displays relevant **Indian Sign Language (ISL) images/GIFs** for effective communication.

---

## ✨ Features
- 🎤 **Speech Recognition**: Captures live speech through a microphone.  
- 🔊 **Audio File Support**: Works with pre-recorded audio files.  
- 📝 **Text Preprocessing**: Cleans and prepares text using NLP techniques.  
- 🖼 **Sign Language Translation**: Converts text into **Indian Sign Language** (images/GIFs).  
- 💻 **User-Friendly GUI**: Built with **EasyGUI** for simple interactions.  
- 🌐 **Offline & Online Support**:  
  - Online → Google Speech API  
  - Offline → CMU Sphinx  

---

## 🛠️ Tech Stack
- **Programming Language**: Python 🐍  
- **Libraries/Modules**:  
  - `speech_recognition` (Google Speech API, Sphinx)  
  - `pyaudio` (microphone input)  
  - `numpy`, `matplotlib` (processing & visualization)  
  - `easygui` (GUI)  
  - `PIL` (image handling)  
  - `tkinter` (GIF display)  
- **Dataset**: Indian Sign Language (ISL) image/GIF dataset  

---

## 🚀 How It Works
1. **Input Speech** → via microphone or audio file.  
2. **Speech-to-Text** → processed using Google API or Sphinx.  
3. **Text Preprocessing** → removes noise, punctuation, and normalizes words.  
4. **Sign Mapping** → words matched with ISL dictionary.  
5. **Output** → corresponding ISL signs displayed as images/GIFs.  

---

## 📂 Project Structure
SEM_project/
│── Main1.py # Main program file
│── signlang.png # GUI image
│── /ISL_Gifs # GIF dataset for words/phrases
│── /letters # ISL alphabet images
│── requirements.txt # Dependencies
│── README.md # Project documentation

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On Linux/Mac

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Project
python Main1.py

📊 Future Enhancements

🤖 Add machine learning models for more accurate translation.

🌐 Expand support to multiple sign languages.

🎥 Add real-time 3D animated avatars for smoother communication.

📱 Develop a mobile-friendly version of the app.