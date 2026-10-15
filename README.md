# PLI-YOLO
The code is being updated!

# Installation

We recommend using Conda to create an isolated environment. The tested environment is Python 3.10, PyTorch 2.2.2, Torchvision 0.17.2, and CUDA 12.1.

```bash
# Clone the repository
git clone https://github.com/J-rong/PLI-YOLO.git
cd PLI-YOLO

# Create and activate the environment
conda create -n pli-yolo python=3.10 -y
conda activate pli-yolo

# Install PyTorch with CUDA 12.1
pip install torch==2.2.2 torchvision==0.17.2 --index-url https://download.pytorch.org/whl/cu121

# Remove conflicting Ultralytics installations
pip uninstall -y ultralytics

# Install PLI-YOLO
pip install -e .

# Install additional dependencies
pip install timm==1.0.7 thop efficientnet_pytorch==0.7.1 einops grad-cam==1.5.4 dill==0.3.8 albumentations==1.4.11 pytorch_wavelets==1.3.0 tidecv PyWavelets opencv-python prettytable
pip install torch-dct==0.1.6
pip install -U openmim
mim install mmengine==0.10.4
mim install mmcv==2.2.0
```

## Getting Started

### 1. Prepare the Dataset

Organize your oriented object detection dataset in YOLO-OBB format:

```text
dataset/
├── images/
│   ├── train/
│   └── val/
└── labels/
    ├── train/
    └── val/
```

Each annotation line should follow the YOLO-OBB format:

```text
class_id x1 y1 x2 y2 x3 y3 x4 y4
```

Update `dota8-obb.yaml` with your dataset paths and class names:

```yaml
path: /path/to/your/dataset
train: images/train
val: images/val

names:
  0: class_name
```

### 2. Prepare the Pretrained Weights

Place the YOLOv8s-OBB pretrained weights at:

```text
model/v8/yolov8s-obb.pt
```

The default PLI-YOLOv8 model configuration is:

```text
ultralytics/cfg/models/v8/PLI-yolov8s-obb.yaml
```

### 3. Configure Training

The default configuration in `train1.py` is:

```python
model_yaml_path = "ultralytics/cfg/models/v8/PLI-yolov8s-obb.yaml"
data_yaml_path = "dota8-obb.yaml"

model = YOLO(model_yaml_path).load("model/v8/yolov8s-obb.pt")

model.train(
    data=data_yaml_path,
    epochs=300,
    imgsz=640,
    batch=8,
    workers=2,
    device=0,
    patience=10,
)
```

You can modify the following parameters according to your hardware and dataset:

- `epochs`: maximum number of training epochs
- `imgsz`: input image size
- `batch`: training batch size
- `workers`: number of data-loading workers
- `device`: GPU index, such as `0`
- `patience`: early-stopping patience

### 4. Start Training

Run the training script from the project root:

```bash
python train1.py
```

Training results, logs, and model weights will be saved automatically under:

```text
runs/obb/train/
```

The best and latest checkpoints are usually located at:

```text
runs/obb/train/weights/best.pt
runs/obb/train/weights/last.pt
```

### 5. Use PLI-YOLOv10

To train the YOLOv10 version, change the model configuration and pretrained weight paths in `train1.py`:

```python
model_yaml_path = "ultralytics/cfg/models/v10/PLI-yolov10s-obb.yaml"

model = YOLO(model_yaml_path).load("model/v10/yolov10s.pt")
```

Make sure that the selected YAML file and pretrained weight file exist before starting training.
