# Machine Learning Term Project
# Batch No: 6

# Prabhjyot Singh Sodhi 2013A7PS151P
# Chandradeo Arya 2013A7PS015P
# Tanmay Utkarsh 2014A3PS300P

# filename: divide_train_test.py
# file to separate and create training and testing datsets from the original dataset

import os
from shutil import copyfile

# OWN fn
def transfer_train_test(x):
    fl = os.listdir(x)
    count = 0

    for fd in fl:
        sound_files = os.listdir(x + '/' + fd)
        count += len(sound_files)
        # sending first 3 files to training, rest to testing
        for fil in sound_files[:3]:
            copyfile(x + '/' + fd + '/' + fil, "training" + '/' + fil)
        for fil in sound_files[3:]:
            copyfile(x + '/' + fd + '/' + fil, "testing" + '/' + fil)

    print x + " count is :" + str(count)

# OWN fn
def main():
    os.chdir('audio_data')

    dirs = ["female_audio", "male_audio", "new_audio"]

    print os.getcwd()

    for x in dirs:
        transfer_train_test(x)

if __name__ == '__main__':
    main()
