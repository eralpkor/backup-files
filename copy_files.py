#!/usr/bin/ python

# Backup files by file extension

import datetime
import os
import shutil
import glob

BACKUP_FILES = '/Users/eralp/test/google/*'
BACKUP_DIRECTORY = '/Users/eralp/test/main/qb_backup_{0}'

def get_backup_directory(base_directory):
    date = datetime.datetime.now().strftime('%Y-%m-%d-%H%M-%a')
    return base_directory.format(date)

files = glob.iglob(os.path.join(BACKUP_FILES, "*.pdf"))
def copy_files(BACKUP_FILES, BACKUP_DIRECTORY):
    for file in files:
        if os.path.isfile(file):
            shutil.copy2(file, BACKUP_DIRECTORY)

def perform_backup(base_directory):
    backup_directory = get_backup_directory(base_directory)
    os.makedirs(backup_directory)
    copy_files(BACKUP_FILES, backup_directory)

def main():
    perform_backup(BACKUP_DIRECTORY)

if __name__ == '__main__':
    main()