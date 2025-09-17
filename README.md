🧏‍♂️ Speech-to-Sign-Language Translator
📌 Project Overview

The Speech-to-Sign-Language Translator is an assistive communication tool designed to bridge the gap between hearing individuals and the Deaf/Hard of Hearing community.
It takes live speech or recorded audio as input, converts it into text, and then displays relevant Indian Sign Language (ISL) images/GIFs for better communication.

✨ Features

🎤 Speech Recognition: Captures live speech through a microphone.

🔊 Audio File Support: Works with pre-recorded audio files.

📝 Text Preprocessing: Cleans and prepares text using NLP techniques.

🖼 Sign Language Translation: Converts text into Indian Sign Language (images/GIFs).

💻 User-Friendly GUI: Built with EasyGUI for simple interactions.

🌐 Offline & Online Support:

Online: Google Speech API

Offline: CMU Sphinx

🛠️ Tech Stack

Programming Language: Python 🐍

Libraries/Modules:

speech_recognition (Google Speech API, Sphinx)

pyaudio (microphone input)

numpy, matplotlib (processing & visualization)

easygui (GUI)

nltk or spacy (text preprocessing)

Dataset: Indian Sign Language (ISL) image/GIF dataset

🚀 How It Works

Input Speech → via microphone or audio file.

Speech-to-Text → processed using Google API or Sphinx.

Text Preprocessing → remove noise, stopwords, normalize words.

Sign Mapping → words matched with ISL dictionary.

Output → corresponding ISL signs displayed as images/GIFs.

📂 Project Structure
SEM_project/
│── Main1.py                # Main program file
│── main.py                 # Alternate main script
│── /Sign_Language_Dataset  # ISL images/GIFs
│── /modules                # NLP + Translator modules
│── requirements.txt        # Dependencies
│── README.md               # Project documentation

⚙️ Installation & Setup
1️⃣ Clone Repository
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

🤖 Add machine learning models for better translation.

🌐 Expand support to multiple sign languages.

🎥 Add real-time animated avatars for smoother communication.

📱 Build a mobile-friendly app version.

🤝 Contributing

Contributions are welcome!

Fork the repo

Create a new branch (feature-xyz)

Commit changes

Push to your branch

Open a Pull Request

📜 License

This project is licensed under the MIT License – free to use and modify.

👨‍💻 Author

Amey Sunil Kalsapnavar
🚀 Passionate about AI, ML, and Assistive Technology.