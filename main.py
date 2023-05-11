from pytube import YouTube
link = input('>> ')
y = YouTube(link)
s = y.streams.get_highest_resolution()
print(s.default_filename)
s.download()
