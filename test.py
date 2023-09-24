import AudioConverter as ac

Converter = ac.AudioConverter("files/encodedFile.txt", "temp.mp3")

print(Converter.Convert())
