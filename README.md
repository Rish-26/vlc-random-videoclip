# vlc-random-videoclip
A Python script that plays a videoclip in VLC chosen randomly from a subfolder. Great when having a party.

# System Requirements
This script has been tested with Python 3 and Windows 7. It also needs FFmpeg.

# Installation
* `git clone` this repo.
* Execute `python setup.py install`.
* Download [FFMpeg](http://ffmpeg.zeranoe.com/builds/), extract the folder and put the `ffprobe.exe` in your local repo.

# Usage
* Create a subfolder `videos` in your local version of the repo and put all the videos you want the script to choose from into that folder.
* Run with `python party.py`.

# Configuration
* Change the variable `videos` in the script to use a different folder.
* Change the variable `interval` to play longer or shorter clips.
