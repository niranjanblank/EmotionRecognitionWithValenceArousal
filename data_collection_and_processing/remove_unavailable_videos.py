import argparse
import pandas as pd
from pathlib import Path

# function to add id each row in the csv file
def remove_unavailable_videos(csv_path, dataset_type,output_filename):
    '''
    :param csv_path: path of csv file containing info about video relative of current folder
    :param dataset_type: train, valid or test
    :param output_filename: filename of the output path e.g. output.csv
    :return: message showing if complete or not
    '''

    try:
        # get the file path
        current_directory = Path.cwd()
        # setting the path
        data_path = current_directory / 'data' / dataset_type
        # getting the name of downloaded files
        file_names = [file.stem for file in data_path.iterdir() if file.is_file()]

        # read the csv file
        df = pd.read_csv(csv_path)
        df = df[df['id'].isin(file_names)]

        # save the data frame
        df.to_csv(output_filename)
    except:
        return f'Couldn\'nt save the data'


if __name__ == '__main__':
    # parser to run the script from terminal using args
    parser = argparse.ArgumentParser(description="Python script to add unique ids to the links")
    parser.add_argument('-i','--input', type=str, help="path of csv file")
    parser.add_argument('-t','--type', type=str, help="type of data file e.g. train,test")
    parser.add_argument('-o','--output', type=str, help="path of output")

    # parse the args
    args = parser.parse_args()

    # use the args
    remove_unavailable_videos(args.input,args.type,args.output)