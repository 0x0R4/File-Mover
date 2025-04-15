# File Mover

## Description

File Mover is a simple Tkinter-based GUI tool that allows you to move files with specified extensions from a source directory to a destination directory and automatically deletes any empty folders after the operation. It also supports extracting archives (ZIP, RAR, 7z) to the destination folder.

## Note
Messy code & ugly UI but it works. Let me know if you need any changes!

False positives on VirusTotal: https://www.virustotal.com/gui/file/e6b4e6451fb11e801d568d348ad2e001329282302e2dfdf59931732a7acbc3bf

## Features

- Select source and destination directories.
- Enter file extensions (comma-separated).
- Move files with the specified extensions from the source directory and its subdirectories to the destination directory.
- Automatically delete empty folders after the files are moved.

## Requirements

Before running the script, make sure you have installed the following Python packages:

- rarfile
- py7zr

Note: `tkinter` is included in the Python standard library on Windows, so no separate installation is required.

## Setup
1. Clone or download the repository.
2. Install dependencies by running the provided `requirements.bat` file or by typing `pip install rarfile py7zr` in your Terminal.
3. Run the `main.py` script or the `File-Mover.exe` file to start the application.
