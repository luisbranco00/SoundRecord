# SoundRecord

This is a simple Python script that uses the `pyaudio` library to record sound. It continuously captures audio input from the default audio device and stores it in a WAV file named "record.wav". It is part of an academic project where an alarm constantly reads the recorded sound and alerts the user when the decibel (dB) level exceeds the specified dangerous limit.

## Prerequisites

Before running the script, please ensure you have the following installed:

- Python 3.x: You can download it from the official Python website (https://www.python.org/downloads/).
- `pyaudio` library: You can install it using pip, by running the following command:

```shell
pip install pyaudio
```

## Usage

1. Ensure that you have a microphone or another audio input device connected to your computer.
2. Clone or download the repository to your local machine.
3. Open the script file (`soundrecord.py`) in a text editor or Python IDE.
4. Optionally, modify the following parameters based on your requirements:

   - `RATE`: The sample rate for audio recording (44100 Hz by default).
   - `CHANNELS`: The number of audio channels (1 for mono, 2 for stereo).
   - `FORMAT`: The format of the audio samples (16-bit integer, in this case).
   - `CHUNK_SIZE`: The number of audio frames per buffer.

5. Save the changes to the script file.
6. Open a terminal or command prompt and navigate to the directory where the script is located.
7. Run the following command to start recording:

```shell
python3 soundrecord.py
```

8. The script will continuously capture audio input until you interrupt it by pressing `Ctrl+C` in the terminal.
9. After stopping the script, you will find the recorded audio saved as "record.wav" in the same directory.

Please note that the recorded audio will be saved in mono format by default. If you wish to record in stereo format, change the value of `CHANNELS` to 2 in the script.


I hope this script helps you record sound and save it as a WAV file. If you have any questions or encounter any issues, please feel free to reach out for assistance.

Happy recording!
