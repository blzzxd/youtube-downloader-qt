# youtube-downloader-qt
Easy download videos from YouTube with youtube-downloader-qt

## About
I created this program for me to fastly download videos from youtube without searching weird downloader sites.

### Platform
Works on Windows. About GNU/Linux - I tested it on Linux. It runs with admin permissions, because by default downloaded videos saving in root folder. You can change this in `main.py` file. Other thing, I don't tested `Open Folder` feature, maybe it will work or not. Anyways, you can delete `os.system(f'start {os.path.realpath(video_path)}')` lines. Maybe it will work.

### Downloaded video directory
By default downloaded videos stores in `C:/downloaded-videos/`. Of course you can change it in `main.py` file. `video_path = '<your path>'`

## Clone
```bash
git clone https://github.com/blzzxd/youtube-downloader-qt
```

## Used libraries
This program using only 2 libraries. `pyqt6` and `pytube` and some built-in libraries

## Build
You can convert main.py file to an exe file with `auto-py-to-exe` library. Don't forget to copy `youtubedownloader.ui` file to your exe file location.
