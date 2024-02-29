import pandas as pd
import os

dir_path = 'test'
df1 = pd.DataFrame(columns=['phrase', 'sentiment'])
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.txt'):
            with open(os.path.join(root, file), 'r') as f:
                phrase = f.read()
                
                sentiment = os.path.basename(root)
                df1 = df1._append({'phrase': phrase, 'sentiment': sentiment}, ignore_index=True)
                
df2 = pd.DataFrame(columns=['phrase', 'sentiment'])
dir_path = 'train'               
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.txt'):
            with open(os.path.join(root, file), 'r') as f:
                phrase = f.read()
                sentiment = os.path.basename(root)
                df2 = df2._append({'phrase': phrase, 'sentiment': sentiment}, ignore_index=True)

df1.to_csv('test_dataset.csv', index=False)
df2.to_csv('train_dataset.csv', index=False)
#aa