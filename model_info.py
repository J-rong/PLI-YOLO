from ultralytics.nn.tasks import DetectionModel

#################
# 打印各层模型结构、参数量、计算复杂度
################

# 模型网络结构配置文件路径
yaml_path = 'ultralytics/cfg/models/v8/PLI-yolov8s-obb.yaml'
# yaml_path = 'ultralytics/cfg/models/v10/PLI-yolov10s-obb.yaml'

# 传入模型网络结构配置文件cfg, nc为模型检测类别数
DetectionModel(cfg=yaml_path, nc=1)