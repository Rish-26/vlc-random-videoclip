This fork of the original repo adds a few features:
1) The clips now start in fullscreen mode
2) You have the option to play random length of clips.
3) You have the option to skip a few seconds off the start and the end of the original video so that when using movies as source clips, the intro and the end credits don't end up in the clips. Default value 0.

# System Requirements
This script has been tested with Python 3 and Windows 7 and above. It also needs FFmpeg.

# Installation
* `git clone` this repo.
* Execute `python setup.py install`.
* Download [FFMpeg](https://www.ffmpeg.org/download.html#build-windows/), extract the folder and put the `ffprobe.exe` in your local repo.

# Usage
* Create a subfolder `videos` in your local version of the repo and put all the videos you want the script to choose from into that folder.
* Run with `python party.py`.

# Configuration
* Change the variable `videos` in the script to use a different folder.
* Change the variable `interval` to play longer or shorter clips.
* Change intStart and intEnd to set start and end values for random length clips. Make both the values equal for a single length clip each time.
* Change skipStart and skipEnd to set offsets at the start and the end of the video files.
