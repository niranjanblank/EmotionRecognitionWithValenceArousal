"""
Script to download youtube videos from the specified csv file
"""
import argparse
import pandas as pd
from pathlib import Path
import logging
import pytube

logging.basicConfig(level=logging.INFO)
def download_video(youtube_link, type, file_id):
    """
    Download a video from YouTube.

    Parameters:
    youtube_link (str): The link to the YouTube video.
    type (str): The type of dataset (e.g., "test", "train", "validation").
    file_id (str): The file ID to use for the downloaded video.
    """
    try:
        # getting the current directory
        current_directory = Path.cwd()
        # setting the path
        path = current_directory / 'data' / type
        yt = pytube.YouTube(youtube_link)

        if not path.exists():
            path.mkdir(parents=True)
        video_file_path = path / f'{file_id}.mp4'
        if video_file_path.exists():
            logging.info(f"Video {file_id} already downloaded. Skipping download.")
            return
        yt.streams.filter().get_highest_resolution().download(filename=video_file_path)
        logging.info(f'{file_id} downloaded')
    except Exception as e:
        logging.error(f"Error occurred while downloading {youtube_link}: {e}")


if __name__ == '__main__':
    # parser to run the script from terminal using args
    parser = argparse.ArgumentParser(description="Python script to download youtube videos")
    parser.add_argument('-i','--input',type=str,help="path of csv file")
    parser.add_argument('-t','--type', type=str, help="type of dataset e.g. test, train or validation")

    # parse the args
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    # dropping the duplicates to only download one instance of video
    df = df.drop_duplicates(subset=['id'])

    for i in range(len(df)):
        row = df.iloc[i]
        file_id = row['id']
        link = row['link']
        download_video(link,args.type,file_id)