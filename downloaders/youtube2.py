import yt_dlp
import os

def YoutubeDownloader(url, title, down_format):

    ydl_opts_video = {
            "format": "bv*[height<=1080]+ba/b[height<=720] ",
            "outtmpl": f"current_videos/{title}.mp4"
        }

    ydl_opts_only_video = {
            "format": "bestvideo[height<=1080]",
            "outtmpl": f"current_videos/{title}.mp4"

    }
    ydl_opts_only_audio = {
            "format": "ba",
            "outtmpl": f"current_videos/{title}.mp3"
        }

    options = [ydl_opts_video, ydl_opts_only_video, ydl_opts_only_audio]

    try:
        with yt_dlp.YoutubeDL(options[down_format]) as ydl:
            ydl.download([url])
            b = ydl.extract_info(url=url)

        filename = os.path.splitext(f"BotDownloader/current_videos/{title}.mp4.webm")
        print(filename)
        return True
    except:
        return False



YoutubeDownloader(url="https://www.youtube.com/watch?v=xhMgugw_qcE", title="Как протестировать соседский Wifi 2.0. Wi-Fi рыбалка (wifiphisher) на Kali", down_format=0)