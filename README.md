# PLI-YOLO
code is coming soon!

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
```

## Get Started
