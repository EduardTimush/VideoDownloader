import yt_dlp


def VkontakteDownloader(url, title):

    ydl_opts_video = {
            "format": "  b",
            "outtmpl": f"current_videos/{title}.mp4"
        }


    try:
        with yt_dlp.YoutubeDL(ydl_opts_video) as ydl:
            ydl.download([url])
            b = ydl.extract_info(url=url)
            return True

    except:
        return False

