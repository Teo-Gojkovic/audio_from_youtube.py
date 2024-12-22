from pytubefix import YouTube 
import os 
destination = "audio/"

def audio_from_youtube() :
    try:
        if not os.path.exists(destination):
            os.makedirs(destination)
    except Exception as e:
        print(f"Erreur lors de la création du dossier : {e}")
    
    yt = YouTube( 
        str(input("Enter the URL of the video you want to download: \n>> "))) 
    video = yt.streams.filter(only_audio=True).first() 
    out_file = video.download(output_path=destination) 
    base, ext = os.path.splitext(out_file) 
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    
    print(yt.title + " has been successfully downloaded.")

if __name__ == "__main__":
   audio_from_youtube()