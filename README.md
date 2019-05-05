# Internship Assignment

## Code arrangement
Data directory contains the code files and raw dataset. Output.csv is the final dataset which is present in the main directory.
To run the code in data directory, run the following files in order by changing the channel links and the output files names:

 1. getVideosDesc.py (YouTube API KEY required)
 2. scrapeDesc.py
 3. CombineScrapings.py

Data generated from the first two code files is already in the folder. Directly run the combinescrapings.py to genereate output csv. 
## Running the algorithms
Use pre_processed_data.csv in running the svm_nb.py as it takes a bit of time to pre process the dataset. Comment out the preprocessing steps in the file to speed up the algorithm.
rnn can be run directly either by training again or using the generated model file. Both are fast enough.



