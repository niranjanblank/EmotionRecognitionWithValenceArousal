import argparse
import pandas as pd


def add_id_to_videos(filepath,dataset_type,output_filename):
    '''

    :param filepath: path of the initial data_link.csv
    :param dataset_type: train, valid or test
    :param output_filename: filename of the output path e.g. output.csv
    :return: message showing if complete or not
    '''
    df = pd.read_csv(filepath)
    df['id'] = dataset_type+'_id_' + df.groupby('link').ngroup().astype(str)
    try:
        df.to_csv(output_filename,index=False)
        return f'data saved to: {output_filename}'
    except:
        return f'Couldn\'nt save the data'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Python script to add unique ids to the links")
    parser.add_argument('-i','--input', type=str, help="path of input file")
    parser.add_argument('-t','--type', type=str, help="type of data file e.g. train,test")
    parser.add_argument('-o','--output', type=str, help="path of output")

    # parse the args
    args = parser.parse_args()

    # use the args
    print(add_id_to_videos(args.input,args.type,args.output))