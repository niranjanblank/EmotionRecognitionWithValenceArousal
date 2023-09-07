import subprocess
import argparse
import pandas as pd
from pathlib import Path
import logging

# path of ffmpeg
ffmpeg= 'C:\\ffmpeg\\bin\\ffmpeg.exe'


logging.basicConfig(level=logging.INFO)
def split_video(input_file_name, utterance_file_name, utterance_start_time, utterance_end_time, type):
    input_file_path =  f'data/{type}/{input_file_name}.mp4'
    output_folder = f'data/split_videos/{type}'

    try:
        path = Path(output_folder)
        if not path.exists():
            path.mkdir(parents=True)
        output_file_path = f'{output_folder}/{input_file_name}_{utterance_file_name}'
        command = [ffmpeg,
                   "-y",
                   "-ss", str(start_time),  # Start time in seconds
                   "-to", str(end_time),  # End time in seconds
                   "-i", input_file_path,  # Input file
                   output_file_path]
        subprocess.run(command)
        logging.info(f'{input_file_name} split to {output_file_path}')
    except:
        logging.error(f'Couldnt split {input_file_name}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Python script to add unique ids to the links")
    parser.add_argument('-i','--input', type=str, help="path of csv file")
    parser.add_argument('-t','--type', type=str, help="type of data file e.g. train,test")

    # parse the args
    args = parser.parse_args()

    df = pd.read_csv(args.input)

    for i in range(len(df)):
        row = df.iloc[i]
        input_file_name = row['id']
        utterance = row['utterance']

        start_time = row['start']
        end_time = row['end']
        split_video(input_file_name,utterance, start_time, end_time, args.type)


