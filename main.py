from pytube import YouTube #Library for downloading YouTube videos

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution() #To get the highest resolution of the video
    try: #If an error ocurres 
        youtubeObject.download()
    except:
        print("Ha ocurrido un error")
    print("Download is completed succesfully")
    
link = input("Enter the YouTube video URL: ")
Download(link)

