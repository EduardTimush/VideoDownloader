import yt_dlp
import shutil


def VideoDownloader(url, title):
    try:
        shutil.rmtree("current_videos")
    except:
        pass
    ydl_opts_video = {
        "format": "b",
        "outtmpl": f"current_videos/{title}.mp4",
        "proxy": "http://X7gAtt:WztArb@45.83.8.149:8000"
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts_video) as ydl:
            ydl.download([url])
            b = ydl.extract_info(url=url)
        return True

    except:
        return False



