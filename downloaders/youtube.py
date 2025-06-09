import yt_dlp
import os

def YoutubeDownloader(url, title, down_format):

    url = "https://youtu.be/-nnTDnpTIjU?si=0y0NynY3C4aJVxhd"
    ydl_opts_video = {
            "format": "bv*[height<=720]+ba/b[height<=480] ",
            "outtmpl": f"current_videos/{title}"
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
        if down_format <= 1:
            for filename in os.scandir("current_videos/"):
                if filename.name == f"{title}.mkv":
                    print("mkv")
                    os.path.splitext(f"current_videos/{title}.mkv")
                    os.rename(f"current_videos/{title}.mkv", f"current_videos/{title}.mp4" )
                elif filename.name == f"{title}.webm":
                    print("wwebm")
                    os.path.splitext(f"current_videos/{title}.webm")
                    os.rename(f"current_videos/{title}.webm", f"current_videos/{title}.mp4")
                else:
                    print("nothing")
        return True
    except Exception as e:
        print(e)
        return False


