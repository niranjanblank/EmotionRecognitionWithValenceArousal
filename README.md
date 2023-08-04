## EmotionRecognitionWithValenceArousal
Developing emotion recognition model using valence arousal score.(In Progress)

### Scripts done upto now
* add_id_to_videos.py
  * Located at `data_collection_and_processing/`
  * This script inputs the csv file containing youtube links of train,test and valid, and adds id to those csv files based on unique youtube links and dataset type. e.g.
  test_id_34 would be added to the rows with common youtube links in the test set, similarly valid_id_23, train_id_23 would be added to respective csv of dataset, and new file would be created which would be named as per required.
  * It can be run using below command after going to the directory where the script is located
  * `python add_id_to_videos.py -i omg_TrainVideos.csv -t train -o test.csv `<br>
  The new csv will be saved in the relative path given by the user
  

* download_videos.py
    * Located at `data_collection_and_processing/`
    * This script is used to download the available youtube videos of highest from links in the csv using pytube.
    * It can be run using below command after going to the directory where the script is located
    * `python download_videos.py -i train.csv -t train`<br>All the downloaded video would be saved in data/train directory for this command.


* download_videos.py
    * Located at `data_collection_and_processing/`
    * This script is used to remove rows containing videos from test, train or valid csv files which couldn't be downloaded from youtube.
    * It can be run using below command after going to the directory where the script is located
    * `python remove_unavailable_videos.py -i data_links/train.csv -t train -o data_links/train_available.csv
      `<br>
      The new csv will be saved in the relative path given by the user