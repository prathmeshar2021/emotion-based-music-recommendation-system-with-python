# emotion-based-music-recommendation-system-with-python
Music recommendation system based on facial emotion detection
Emotion-Based Music Recommendation System

📌 Project Overview

The Emotion-Based Music Recommendation System is an AI-driven application that detects users' facial emotions and suggests personalized music playlists accordingly. This project leverages computer vision for emotion detection and integrates with Spotify's API to curate suitable playlists.

🚀 Features

🎭 Emotion Detection: Uses computer vision to analyze facial expressions.

🎵 Music Recommendation: Recommends personalized Spotify playlists based on detected emotions.

🔄 Real-time Analysis: Provides instant recommendations as emotions change.

🌐 Spotify Integration: Utilizes Spotify's Spotipy API for seamless playlist fetching.

🛠️ Tech Stack

Python

OpenCV (for facial emotion detection)

Deep Learning Models (e.g., CNN for emotion recognition)

Spotipy (Spotify API integration)

Tkinter (for GUI development)

📂 Project Structure

📁 Emotion-Based-Music-Recommendation
 ┣ 📂 dataset
 ┣ 📂 models
 ┣ 📂 gui
 ┣ 📜 app.py
 ┣ 📜 requirements.txt
 ┣ 📜 README.md
 ┗ 📜 .env (For Spotify credentials)

🔧 Installation

Clone the Repository

git clone https://github.com/prathmeshar2021/emotion-based-music-recommendation-system-with-python
cd Emotion-Based-Music-Recommendation

Create a Virtual Environment

python -m venv env
source env/bin/activate    # For Linux/Mac
.\env\Scripts\activate     # For Windows

Install Dependencies

pip install -r requirements.txt

Add Spotify Credentials
Create a .env file in the root directory with the following content:

SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback

Run the Application

python app.py

📋 Usage

Launch the application.

Allow access to the webcam for emotion detection.

The system will detect your facial expression (e.g., happy, sad, angry) and recommend a matching Spotify playlist.

🎯 Emotion-to-Genre Mapping

Emotion


Happy

Sad

Angry

Neutral


🧠 Future Enhancements

Add support for multiple faces.

Improve emotion detection accuracy using advanced models.

Enhance GUI with additional controls and playlist previews.

🤝 Contributing

Contributions are welcome! Feel free to fork the repo, create a new branch, and submit a pull request.
