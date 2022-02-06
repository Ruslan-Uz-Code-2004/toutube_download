from pytube import YouTube



link = str(input('Введите URL :'))
s = YouTube(link)
stream = s.streams.get_highest_resolution()

stream.download()



