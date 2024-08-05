from src.data.video_segmentation import segment_videos
import csv

import hydra


@hydra.main(config_path="./configs", config_name="video_segmentation_config", version_base=None)
def main(cfg):

    with open(cfg.metadata_path, 'a') as f:
        writer = csv.DictWriter(f, ["video_path", "parent_video_path"])
        for original_video_path, video_segment_path in \
            segment_videos(original_videos_dirs=cfg.original_videos_dirs,
                           segment_duration_secs=cfg.segment_duration_secs,
                           save_dir=cfg.save_dir,
                           video_extensions=cfg.video_extensions
            ):

            writer.writerow(
                {
                    "video_path": video_segment_path,
                    "parent_video_path": original_video_path
                }
            )
    
if __name__ == "__main__":
    main()