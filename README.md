README for Audio Streaming and Adafruit Integration
This script captures audio data in real-time using PyAudio and processes it for amplitude calculation. The processed data is then sent to the Adafruit platform for further analysis or visualization.

Prerequisites
Ensure you have the necessary dependencies installed:

PyAudio
NumPy
Adafruit_IO
Setup
Obtain Adafruit credentials: Replace X and Key with your Adafruit Client name and key in the aio = Client(X, Key) line.

Customize Adafruit feed: Modify the feed name from "semana2" to your desired Adafruit feed in the aio.send_data("semana2", valores[j]) lines.

Usage
Run the script: Execute the script to start streaming and processing audio data.

Interrupt the script: Use keyboard interrupt (Ctrl+C) to stop the script.

Notes
The script converts audio data into JSON format before sending it to Adafruit.
Ensure you have a reliable internet connection for successful communication with Adafruit.
Feel free to adapt the script based on your specific requirements.
