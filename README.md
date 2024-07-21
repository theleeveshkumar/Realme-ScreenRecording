# RealMe: Screen Recording and Audio Synchronization

**RealMe** is a Python-based project designed to capture screen video and audio simultaneously and combine them into a synchronized final video file. It leverages popular Python libraries like OpenCV, PyAutoGUI, PyAudio, and MoviePy.

## Features

- **Screen Recording**: Captures screen video at a specified frame rate.
- **Audio Recording**: Records audio from the microphone concurrently.
- **Synchronization**: Merges recorded audio with video into a final output file.
- **Multiple Formats Supported**: Outputs video in AVI, MP4, and MOV formats.

## Installation

To set up RealMe, follow these steps:

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/realme.git
    ```

2. **Navigate to the Project Directory**:

    ```bash
    cd realme
    ```

3. **Install Dependencies**:

    Ensure you have Python 3.12 or higher installed. Then, install the required Python packages:

    ```bash
    pip install opencv-python pyautogui numpy pyaudio moviepy
    ```

## Usage

1. **Run the Script**:

    ```bash
    python ScreenRecording.py
    ```

2. **Provide Video File Name**:

    When prompted, enter the desired name and path for the output video file (e.g., `output.avi`).

3. **Stop Recording**:

    Press `q` in the recording window to stop the recording process.

4. **Final Output**:

    The script will generate a video file with synchronized audio. The final video will be named `final_<your_filename>`.

## Configuration

- **Video Frame Rate (fps)**: Default is `10.0`. Adjust as needed.
- **Resolution**: Uses the current screen resolution.
- **Audio Settings**:
  - **Sample Format**: `pyaudio.paInt16`
  - **Channels**: `2` (stereo)
  - **Rate**: `44100` Hz

## Troubleshooting

- **Codec Issues**: Ensure the required codecs are installed on your system. For AVI files, `'XVID'` is used; for MP4 and MOV files, `'libx264'` is used.
- **Audio Errors**: Check microphone settings and ensure it is properly configured.

## Contributing

Contributions are welcome! To contribute:

1. **Fork the Repository**.
2. **Create a Feature Branch**:

    ```bash
    git checkout -b feature/YourFeature
    ```

3. **Commit Your Changes**:

    ```bash
    git commit -am 'Add new feature'
    ```

4. **Push to the Branch**:

    ```bash
    git push origin feature/YourFeature
    ```

5. **Create a Pull Request**.

## License

RealMe is licensed under the MIT License. 

## Contact

For questions or feedback, contact [Leevesh Kumar](mailto:leeveshkumar14@gmail.com).

## Acknowledgements

- **OpenCV**: For video processing.
- **PyAutoGUI**: For capturing screenshots.
- **PyAudio**: For audio recording.
- **MoviePy**: For video editing and synchronization.
