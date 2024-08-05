import csv
import os
from typing import Dict

METADATA_PATH = "./metadata.csv"
METADATA_FIELDS = [
    "video_path", 
    "parent_video_path"
]

def main():
    with open(METADATA_PATH, 'w') as f:
        writer=csv.writer(f)
        writer.writerow(METADATA_FIELDS)

if __name__ == "__main__":
    main()
