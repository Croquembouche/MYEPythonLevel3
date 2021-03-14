from pytube import YouTube

url = "https://www.youtube.com/watch?v=9vJRopau0g0"

video = YouTube(url)
filters = video.streams.filter(progressive=True, file_extension="mp4")
filters.get_highest_resolution().download()
print("done")