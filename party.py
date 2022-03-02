import random
import time
import subprocess
import vlc
import os

# create list of all videos in folder 'videos'
subfolder = "videos"
videos = os.listdir(subfolder)

# setup vlc instance
player = vlc.MediaPlayer()

# interval for the clips. It will randomly choose a clip length between intStart and intEnd
# Enter same value for both intStart and intEnd to make the interval a single value.
intStart = 8
intEnd = 20

# define time to skip (in seconds) at the start and the end of the video to skip intros and end credits
skipStart = 0
skipEnd = 0

try:
    print("Script running... press Ctrl+C to quit.")

    # Open player in fullscreen mode
    player.toggle_fullscreen()
    while True:
        intervall = random.randint(intStart,intEnd)
        # choose random file number
        n = random.randint(0, len(videos) - 1)

        # create path to current video file
        video = os.path.join(subfolder, videos[n])

        # get length of video n using ffprobe
        ffprobe = subprocess.check_output(['ffprobe', video],
                                          shell=True,
                                          stderr=subprocess.STDOUT)

        # calculate length of current video in seconds
        i = ffprobe.find(bytes("Duration:", 'UTF-8'))
        duration = ffprobe[i + 9:i + 9 + 12].decode('UTF-8').strip().split(":")
        length = int(int(duration[0]) * 3600 +
                     int(duration[1]) * 60 +
                     float(duration[2])
                     )

        # create random position in video n
        position = random.randint(skipStart, (length - intervall)-skipEnd)


        # feed player with video and position
        player.set_mrl(video)
        player.play()
        player.set_time(position * 1000)

        # wait till next video
        time.sleep(intervall)
except KeyboardInterrupt:
    pass
