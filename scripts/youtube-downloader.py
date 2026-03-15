from pytube import YouTube
link = input('Enter link to download: ')
video = YouTube(
    link,
    client="ANDROID",            
    use_oauth=False,
    allow_oauth_cache=False
)
stream = video.streams.get_highest_resolution()
stream.download()