
# /////////////////////////
# //youtube-downloader-qt//
# /////////////////////////
# https://github.com/blzzxd

import os
from PyQt6 import uic
from pytube import YouTube
from PyQt6.QtWidgets import QApplication, QMessageBox
from threading import Thread

file_size = 0
video_path = '/downloaded-videos/'

Form, Window = uic.loadUiType("youtubedownloader.ui")
app = QApplication([])
app.setStyle('Fusion')
window = Window()
form = Form()
form.setupUi(window)
window.show()


def aboutwin():
    msg = QMessageBox()
    msg.setText("youtube downloader qt v1.0")
    msg.setInformativeText("by blzzxd")
    msg.setWindowTitle("About")
    msg.exec()


def close():
    app.exit()


def open_folder():
    if os.path.isdir(video_path):
        os.system(f'start {os.path.realpath(video_path)}')
    else:
        os.mkdir(video_path)
        os.system(f'start {os.path.realpath(video_path)}')


# clear video name, state and reset progress bar
def clear_state():
    form.ytname.setText('( waiting... )')
    form.videostate.setText('( waiting...)')
    form.progressBar.setValue(0)


# getting progressbar work!
def progress(stream=None, chunk=None, remaining=0):
    form.videostate.setText('downloading...')
    file_downloaded = (file_size - remaining)
    per = (file_downloaded / file_size) * 100
    form.progressBar.setValue(int(per))

    if per == 100:  # if download completed
        form.videostate.setText('completed!')
        open_folder()
        form.convertButton.setEnabled(True)
        form.pasteBox.clear()


def download():
    try:
        form.convertButton.setEnabled(False)
        global file_size
        clear_state()
        yt = YouTube(form.pasteBox.text(), on_progress_callback=progress)
        form.ytname.setText(yt.title)
        video = yt.streams.get_highest_resolution()
        file_size = video.filesize
        video.download(video_path)
    except:
        form.videostate.setText('error :(')
        form.convertButton.setEnabled(True)


def on_convert_button_click():
    download()


# connections
form.actionExit.triggered.connect(close)
form.actionOpen_Folder.triggered.connect(open_folder)
form.convertButton.clicked.connect(on_convert_button_click)
form.actionAbout.triggered.connect(aboutwin)

app.exec()
