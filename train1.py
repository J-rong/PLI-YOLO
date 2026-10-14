from ultralytics import YOLO
from ultralytics.data.converter import convert_dota_to_yolo_obb


# model_yaml_path = r"ultralytics/cfg/models/v10/PLI-yolov10s-obb.yaml"

model_yaml_path = r"ultralytics/cfg/models/v8/PLI-yolov8s-obb.yaml"
# 数据集配置文件

data_yaml_path = 'dota8-obb.yaml'
# 预训练模型

def main():
    # model/yolov8s-obb.pt
    model = YOLO(model_yaml_path).load('model/v8/yolov8s-obb.pt')  # build from YAML and transfer weights

    model.train(data=data_yaml_path,
                epochs=300,
                imgsz=640,
                batch=8,
                workers=2,
                device = 0,
                patience=10,

                )


if __name__ == '__main__':
    main()
