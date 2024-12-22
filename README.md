# YouTube MP3 Downloader

This project allows you to download MP3 files from YouTube videos.

## Requirements

- Python 3.x
- `pytubefix` library

## Installation

1. Clone the repository:

```sh
git clone https://github.com/yourusername/youtube_mp3_downloader.git
cd youtube_mp3_downloader
```

2. Install the required libraries:

```sh
pip install pytubefix
```

## Usage

1. Run the `main.py` script:

```sh
python main.py
```

2. Enter the YouTube video URL when prompted :

```sh
Enter the URL of the video you want to download:
>> 
```

3. The script will download the video in mp3 format, and save it in the `audio` directory.

## How `main.py` Works

1. **Import Libraries**: The script imports necessary libraries such as `pytube` for downloading videos and `pydub` for converting video to audio.

2. **Get YouTube URL**: The script prompts the user to enter a YouTube video URL.

3. **Download Video**: Using `pytube`, the script downloads the video from the provided URL.

4. **Convert to MP3**: The downloaded video is then converted to MP3 format using `pydub`.

5. **Save MP3**: The converted MP3 file is saved in the `downloads` directory.

## Example

```sh
python main.py
```
```sh
Enter the URL of the video you want to download:
>> https://www.youtube.com/watch?v=example
```

The MP3 file will be saved in the `audio` directory.

## License

This project is licensed under the MIT License.

## Autor
[![Teo GOJKOVIC](https://img.shields.io/badge/Teo_GOJKOVIC-222e45?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Teo-Gojkovic)