# AsciiPy

AsciiPy is a Python tool that is focused on ASCII art. The tool allows you to convert a video file into a sequence of ASCII frames, which can be either colored, grayscale, or true-color (for terminals that support it). Future updates will support image conversion into terminal ASCII art as well as ASCII art generation into image files.

## Features

- Convert video files to ASCII art in the terminal.
- Supports different color modes: 
  - Default colored output
  - Grayscale mode
  - True-color mode (if the terminal supports it)
- Frame rate, and aspect ratio retention for better control over the output.
- Automatically scales when terminal size changes.

## Future Features

- Convert images to ASCII art.
- Additional customization for ASCII characters and color mappings.

## Requirements

- Python 3.6 or higher
- Requires the following Python libraries:
  - OpenCV (`cv2`)
  - PIL (Pillow)
  - argparse

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/mazarskov/AsciiPy.git
    cd AsciiPy
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Convert a Video to ASCII

To convert a video into ASCII art and display it in the terminal, use the following command:

```bash
python3 main.py <video_path>
```

### Additional arguments 

Use the follwong arguments to change the behaviour of conversion.

`--grayscale` Outputs the ASCII video in grayscale.

`--true_color` Outputs the ASCII video in true RGB color insted of just 256-bit. **Note:** Default Windows 11 supports true color, default MacOS terminal doesn't.

`--retain_aspect` Preserves the original aspect ratio of the video instead of strecthing to fit the entire terminal.