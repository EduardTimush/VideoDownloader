import yt_dlp


def InstagramDownloader(url, title):
    url = url

    ydl_opts_video = {
            "format": "  b",
            "outtmpl": f"current_videos/{title}.mp4"
        }
    try:
        with yt_dlp.YoutubeDL(ydl_opts_video) as ydl:
             ydl.download([url])
             b = ydl.extract_info(url=url)
    except:
        return False
InstagramDownloader('https://youtu.be/-nnTDnpTIjU?si=0y0NynY3C4aJVxhd', 'hh')