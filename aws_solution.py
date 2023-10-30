# -*- coding: utf-8 -*-
"""AWS_Solution.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12rP_Ru1NPLiEqjCb9psOesPlZFR9_H_C
"""

import pandas as pd
import time
#we store the start time of the script.
start_time= time.time()
#we initialise an empty list
tags_list = []
# we take a chunk size
chunk_size = 15000
# we initialize an empty list to store chunks
lists = pd.DataFrame()
# We Loop through each chunk and append it to the result dataframe
with open('list.json', 'r') as lists_set:
  for chunk in pd.read_json(lists_set, lines=True, chunksize=chunk_size,encoding='utf-8'):
        # We have to Flatten the lists of tags and extend the tags_list
        for tags in chunk['tags']:
            if isinstance(tags, list):
                tags_list.extend(tags)
tags_df = pd.DataFrame({'tags': tags_list})
tags_df.dropna(inplace=True)
# We now will count the usage of each tag
tag_counts = tags_df['tags'].value_counts().reset_index()
tag_counts.columns = ['tag', '#usage']
# We will Sort the DataFrame by usage count in descending order
sorted_tags = tag_counts.sort_values(by='#usage', ascending=False)

end_time= time.time()
# then we print the top tags and time taken
print(sorted_tags.head(5))
print(f"Time taken: {end_time - start_time:.2f} seconds")
