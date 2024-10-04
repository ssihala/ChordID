#!/usr/bin/env python
# coding: utf-8

import os
import shutil
from sklearn.model_selection import train_test_split
import pandas as pd


# # Load Kaggle Dataset

kaggle_token_path = os.path.join(os.getcwd(),"token")
data_path = os.path.join(os.getcwd(),"data")
os.environ["KAGGLE_CONFIG_DIR"] = kaggle_token_path
os.chmod(kaggle_token_path+"/kaggle.json", 0o600)
import kaggle

current_dir = os.getcwd()
os.chdir(data_path)
if "Training" not in os.listdir(data_path):
    os.system('kaggle datasets download -d fabianavinci/guitar-chords-v3 --unzip')


#Merge the Test and Training folders for now, we'll do a split later on
test_dir = os.path.join(data_path, "Test")
train_dir = os.path.join(data_path, "Training")
shutil.copytree(test_dir, train_dir, dirs_exist_ok=True)
shutil.rmtree(test_dir)

os.rename(train_dir, os.path.join(data_path, "Kaggle_data"))


# Split into Train and Test


file_list = []

kaggle_path = os.path.join(data_path, "Kaggle_data")
for chord_label in os.listdir(kaggle_path):
    label_path = os.path.join(kaggle_path, chord_label)
    if os.path.isdir(label_path):
        for file_name in os.listdir(label_path):
            file_path = os.path.join(label_path, file_name)
            file_list.append((file_path, chord_label))

df = pd.DataFrame(file_list, columns=['file_path', 'chord_label'])

train_paths, test_paths = train_test_split(df, train_size=0.8, stratify=df['chord_label'])
print(train_paths.shape)
print(test_paths.shape)


# # Move Train and Test files to their respective folders
train_dir_path = os.path.join(data_path, "Train")
test_dir_path = os.path.join(data_path, "Test")

def move_files(paths_df, split_dir_path):
    
    if not os.path.isdir(split_dir_path):
        os.makedirs(split_dir_path)
        
    for file in paths_df.iterrows():
        path = file[1]['file_path']
        file_name = os.path.basename(path)
        label = file[1]['chord_label']
        label_dir_path = os.path.join(split_dir_path, label)
        
        if not os.path.isdir(label_dir_path):
            os.makedirs(label_dir_path)
        file_output_path = os.path.join(label_dir_path, file_name)
        shutil.copy(path, file_output_path)


move_files(train_paths, train_dir_path)
move_files(test_paths, test_dir_path)

shutil.rmtree(kaggle_path)


