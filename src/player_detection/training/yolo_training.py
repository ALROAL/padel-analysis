from ultralytics import YOLO
from datetime import datetime
from pathlib import Path

def run_yolo_training(model_path, data_path, epochs, save_dir):

    run_id = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
    save_dir = (Path(save_dir) / run_id).as_posix()

    yolo = YOLO(model_path)
    yolo.train(data=data_path, epochs=epochs, save_dir=save_dir)