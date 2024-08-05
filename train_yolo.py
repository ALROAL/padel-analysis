from src.training.yolo_training import run_yolo_training

import hydra


@hydra.main(config_path="./", config_name="config", version_base=None)
def main(cfg):

    run_yolo_training(model_path=cfg.model.path,
                      data_path=cfg.data.path,
                      epochs=cfg.hyperparameters.epochs,
                      save_dir=cfg.model.save_dir)


if __name__ == "__main__":
    main()