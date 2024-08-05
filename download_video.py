import argparse
import logging
from pytube import YouTube

def main(args):


    try:
        youtubeObject = YouTube(args.url)
        video = (youtubeObject.streams.
                 filter(progressive=False, file_extension='mp4').
                 order_by('resolution').
                 desc().
                 first().
                 download(output_path="/home/ubuntu/padel-analysis/data/raw", filename=args.save_name))
    except:
        logging.info("An error has occurred")
        
    logging.info("Download is completed successfully")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, type=str)
    # parser.add_argument("--save_path", required=True, type=str)
    parser.add_argument("--save_name", default=None, type=str)
    args = parser.parse_args()
    main(args)