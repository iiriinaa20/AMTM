import os
import random
import shutil

def move_random_files(source_dir, destination_dir, nr_files):
    files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
    random_files = random.sample(files, nr_files)

    for random_file in random_files:
        source_path = os.path.join(source_dir, random_file)
        destination_path = os.path.join(destination_dir, random_file)
        shutil.move(source_path, destination_path)
        
source_directory = "./training"
destination_directory = "./testing"
nr_files = 150

move_random_files(source_directory, destination_directory, nr_files)
