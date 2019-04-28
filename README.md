# SubShift

## Quickly and easily align a subtitle track with the audio.

Sometimes it can be hard to find subtitles online that are properly aligned due to starting times of various videos. However, unless playback speed has been altered, video files are *usually* consistent (not accounting for commercials, etc), so problems with subtitle files can be fixed by just shifting all the timestamps by some amount. This is a command-line utility for doing just that. 

## Requirements:
* Python3
* Numpy

## Use: 

First, find the time difference between your subtitle track and the video. Then ensure the subtitle track is in the right directory. By default this can be the directory of the `SubShiftRunner.py` file. Run with `python SubShiftRunner.py`. Program needs to be called with 4 arguments: input file name, the time shift value, output file name, and the direction in which to shift by. So for example, if I have a file `in.srt`, which I want to shift backwards by 4.5 seconds, and retrieve a new file `out.srt`, I would run the following: `python SubShiftRunner.py -f in.srt, -t 00:00:04,500 -o out.srt -d B`. `-f` specifies the input file, `-o` specifies the output file, `-t` specifies the time shift value in the format of `hh:mm:ss:lll`, and `-d` specifies forward/backward shift with `F/B`, respectively. Take the output file, make sure it's both in the same directory and has the same name as the video you're watching, and enjoy the show. 

## To-Do:
Building a GUI version of the app.
Adding finer grained controls. 