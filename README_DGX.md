# Chatterbox Installation Guide for NVIDIA DGX Spark (Blackwell)

This guide details how to install and run **Chatterbox** on the NVIDIA DGX Spark system equipped with **Blackwell (GB10 / sm_121)** GPUs.

## 🚀 Quick Start

### 1. Prerequisites
You need a **Hugging Face Access Token** to download models.
Create a `.env` file in the project root:
```bash
echo "HF_TOKEN=hf_your_token_here" > .env
```

### 2. Build the Docker Image
Due to the bleeding-edge hardware (CUDA 13.0+), we must build a custom Docker image that compiles `torchaudio` from source with specific patches.

```bash
./build.sh
```
*Build time: ~3-5 minutes.*

### 3. Run the Container
Start the container with GPU access and volume mounting:
```bash
./run.sh
```
This drops you into a shell inside the container: `root@<container_id>:/workspace/chatterbox#`.

### 4. Verification Check
Inside the container, run the example script:
```bash
python example_tts_turbo.py
```
This generates `test-turbo-manual-01.wav` in the `source_code/` directory.

---

## 🛠️ Technical Implementation Details for Blackwell

This installation overcomes several compatibility challenges with the new Blackwell architecture:

1.  **Base Image**: Uses `nvcr.io/nvidia/pytorch:25.12-py3` which provides the necessary CUDA 13.1 drivers and a compatible PyTorch (`2.10.0a0`) build for `sm_121`.
2.  **Torchaudio Source Build**:
    - `torchaudio` is built from the `release/2.6` branch.
    - **Header Patch**: Modifies `utils.h` to fix missing `device.h` includes in the newer PyTorch version.
    - **CUB Patch**: Patches `compute.cu` and `ctc_prefix_decoder_kernel_v2.cu` to resolve `cub::Max` and `cub::FpLimits` deprecations in CUDA 13.
3.  **Dependency Locking**:
    - A `constraints.txt` file is generated during build to prevent `pip` from accidentally downgrading the critical Blackwell-optimized PyTorch version.
    - `s3tokenizer` is installed in isolation to bypass dependency resolution conflicts while ensuring functionality.

## 🐛 Troubleshooting

- **"operator torchvision::nms does not exist"**: This indicates the `torch` version was downgraded. Ensure you are using the `Dockerfile` with the `constraints.txt` logic.
- **"ModuleNotFoundError: No module named 's3tokenizer.model_v2'"**: The `s3tokenizer` version is too old. The Dockerfile forces version `0.3.0`.
- **Warnings about `sm_121`**: You may see warnings like `Capability sm_121 is not compatible with the current PyTorch installation`. If generation works, these are benign artifacts of the driver's forward compatibility mode.
