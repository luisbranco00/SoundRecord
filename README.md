# Audio Streaming and Adafruit Integration

This script captures real-time audio data using PyAudio, processes it for amplitude calculation, and sends the processed data to the Adafruit platform for further analysis or visualization.

## Prerequisites

Ensure you have the following dependencies installed:

- [PyAudio](https://pypi.org/project/PyAudio/)
- [NumPy](https://numpy.org/)
- [Adafruit_IO](https://pypi.org/project/Adafruit-IO/)

## Setup

1. Obtain Adafruit credentials: Replace `X` and `Key` with your Adafruit Client name and key in the `aio = Client(X, Key)` line.

2. Customize Adafruit feed: Modify the feed name from `"semana2"` to your desired Adafruit feed in the `aio.send_data("semana2", valores[j])` lines.

## Usage

1. **Run the script:** Execute the script to start streaming and processing audio data.

2. **Interrupt the script:** Use keyboard interrupt (`Ctrl+C`) to stop the script.

## Notes

- The script converts audio data into JSON format before sending it to Adafruit.
- Ensure you have a reliable internet connection for successful communication with Adafruit.

Feel free to adapt the script based on your specific requirements.

## Acknowledgments

- [PyAudio Demos](https://github.com/cclaan/PyAudioNotebook/blob/master/PyAudio%20Demos.ipynb)
- [Adafruit IO API Cookbook](https://io.adafruit.com/api/docs/cookbook.html)



