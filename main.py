import PySimpleGUI as sg 
from pytubefix import YouTube
from moviepy.editor import AudioFileClip
import pymsgbox
import os

def conversor(mp4, mp3):
    arquivo = AudioFileClip(mp4)
    arquivo.write_audiofile(mp3)
    arquivo.close()

sg.theme("Dark Blue 16")

interface = [
    [sg.Titlebar('Youtube Downloader', None, 'red', 'white')],
    [sg.Text('Insert a video url')],
    [sg.InputText(size=(50, 1), key='url')],
    [sg.Checkbox('Need to convert a MP3 Audio?', key='mp3')],
    [sg.Button('download')],
]

window = sg.Window('window', interface)

while True:
    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'download':
        link = value['url']
        video = YouTube(link)
        stream = video.streams.get_highest_resolution()
        download_path = stream.download()
        
        if value['mp3']:
                path_video = download_path
                path_sound = os.path.splitext(download_path)[0] + '.mp3'
                conversor(path_video, path_sound)
                pymsgbox.alert('Conversão Concluída','Conversor')

window.close()
exit()
