# extract-presentation
A script made to extract presentation's slides from a video.

Requirements:
- Only on Windows: Windows Subsystem for Linux 
- Python 3
- `opencv-python`, `rename`, `imagemagick`, `ffmpeg`, `ocrmypdf` (all installed by `install.sh` script)

How to run it:
1. Only on Linux: remove word `wsl` from `extract_presentation.py`.
1. Run `./install.sh` on Linux or `wsl ./install.sh` on Windows before the first run to install dependencies.
2. `python extract_presentation.py input.mp4 output.pdf`

How it works:
1. FFMPEG extracts all frames from the video.
2. OpenCV removes all duplicated frames.
3. Convert from ImageMagick joins extracted slides to PDF file.
4. Ocrmypdf adds text layer. 

