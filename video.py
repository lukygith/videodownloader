import yt_dlp
import sys

def get_arg(flag):
    if flag in sys.argv:
        i = sys.argv.index(flag)
        if i + 1 < len(sys.argv):
            return sys.argv[i + 1]
    return None

url = get_arg("-u")
fmt = get_arg("-f")

if not url or not fmt:
    print("Použití: python main.py -u <odkaz> -f <mp3/mp4>")
    sys.exit(1)

fmt = fmt.lower()

if fmt == "mp3":
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "%(title)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }

elif fmt == "mp4":
    ydl_opts = {
        "format": "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]",
        "outtmpl": "%(title)s.%(ext)s",
        "merge_output_format": "mp4",
    }

else:
    print("Neplatný formát (použij mp3 nebo mp4)")
    sys.exit(1)

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Hotovo ✔")
