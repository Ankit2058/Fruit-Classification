<div align="center">

# 🍌 Banana Freshness Classification

### Computer vision meets real-world hardware

**A major-project prototype for detecting fresh and rotten bananas with deep learning and connecting predictions to an Arduino-controlled mechanism.**

[Explore the models](Software/) · [View the collected images](Data%20collection/) · [Explore the hardware](HARDWARE/)

</div>

---

## At a glance

This repository documents an end-to-end **banana freshness classification** experiment: collecting images, investigating neural-network approaches, adapting a pretrained **ResNet-18** for binary classification, and integrating camera-based inference with **Arduino over serial communication**.

The interesting part isn't only recognizing a banana's condition. It's taking a prediction out of a notebook and using it as a signal in a physical system.

> **Project status:** Academic prototype / project archive. Code and notebooks are available for exploration; the real-time workflow requires a compatible camera, Arduino setup, and separately available trained model weights.

## How it works

```text
Camera / image
      |
      v
OpenCV frame capture
      |
      v
Resize + normalize
      |
      v
Fine-tuned ResNet-18
      |
      +---- Fresh (class 0) ----> Serial: 0
      |
      +---- Rotten (class 1) ---> Serial: 1
                                  |
                                  v
                           Arduino controller
                                  |
                                  v
                           Hardware response
```

The Python application samples the webcam feed approximately every **4 seconds**, predicts a class, and sends `0` or `1` at **9600 baud**. The repository includes Arduino and servo-control experiments for the hardware side.

## Inside the repository

| Path | What you'll find |
| --- | --- |
| [`Data collection/Fresh banana/`](Data%20collection/Fresh%20banana/) | Original images of fresh bananas |
| [`Data collection/Rotten Banana/`](Data%20collection/Rotten%20Banana/) | Original images of rotten bananas |
| [`Software/Custom_Neural_Network.ipynb`](Software/Custom_Neural_Network.ipynb) | Custom neural-network experimentation |
| [`Software/Custom_Neural_Network2.ipynb`](Software/Custom_Neural_Network2.ipynb) | Further network experiments |
| [`Software/Finetuning_Resnet.ipynb`](Software/Finetuning_Resnet.ipynb) | Transfer-learning / ResNet investigation |
| [`Software/Real-time-classification.ipynb`](Software/Real-time-classification.ipynb) | Real-time classification experiments |
| [`Software/model_module.py`](Software/model_module.py) | ResNet-18 model construction, preprocessing, and inference |
| [`Software/main_module.py`](Software/main_module.py) | Webcam loop and Arduino serial integration |
| [`HARDWARE/INTEGRATION/`](HARDWARE/INTEGRATION/) | Arduino and servo-control scripts |
| [`HARDWARE/`](HARDWARE/) | Hardware documentation and design materials |

## Technology

**Python · PyTorch · torchvision · OpenCV · Pillow · NumPy · pySerial · Jupyter · Arduino**

The inference module uses a pretrained ResNet-18 backbone with a **two-class output layer**, loading a saved state dictionary for inference on the CPU.

## Exploring the project

**1. Clone the repository**

```bash
git clone https://github.com/Ankit2058/Fruit-Classification.git
cd Fruit-Classification
```

**2. Set up Python**

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
pip install torch torchvision opencv-python pillow numpy pyserial jupyter
```

**3. Start with the notebooks**

```bash
jupyter notebook
```

Open the notebooks under `Software/` to understand the training and evaluation experiments before attempting hardware integration.

**4. Optional: try real-time inference**

Review `Software/main_module.py` and configure:

- `model_path`: the location of your **compatible trained ResNet-18 weights** (`.pth`). The script currently uses a machine-specific Windows path; a ready-to-run weights file is not included in the repository tree.
- `arduino_port`: your connected Arduino's serial port (currently `COM3`).
- Camera index: `cv2.VideoCapture(0)` uses the default webcam.
- Hardware sketch: inspect and upload the appropriate code from `HARDWARE/INTEGRATION/` to your Arduino.

Then, from the repository root:

```bash
python Software/main_module.py
```

The application displays camera frames and prints predictions. Press **q** in the OpenCV window to exit.

**Important:** The code is an experimental integration, not a calibrated food-safety tool or a production-ready sorting system. Hardware movement should be tested with appropriate physical safeguards.

## What this project explores

- The difference between designing a classifier and making it work on live camera input.
- Custom neural networks versus transfer learning as alternative approaches.
- Turning model output into a minimal serial protocol for a microcontroller.
- The practical challenges of connecting datasets, experiments, inference, and physical devices.

## Original project description

The original README text is retained below verbatim.

---

# Fruit-Classification
As a part of Major project, Fruit classification repo consists all the code written for the project.
