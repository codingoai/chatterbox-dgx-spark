# Chatterbox for NVIDIA Blackwell (Dockerized)

This repository contains a **Dockerized installation of Chatterbox** optimized for NVIDIA Blackwell (GB10 / sm_121) GPUs running CUDA 13.0+.

## Key Features
- **CUDA 13 Compatibility**: Patches `torchaudio` source code to resolve `cub` namespace and header issues.
- **Dependency Guard**: Prevents critical Blackwell-optimized PyTorch versions from being replaced by incompatible binaries.
- **Easy Deployment**: Simple `build.sh` and `run.sh` scripts to get started immediately.

## Quick Start
See the [DGX Installation Guide](README_DGX.md) for detailed instructions.

```bash
# 1. Build
./build.sh

# 2. Run
./run.sh

# 3. Generate Audio
python example_tts_turbo.py
```

## Credits
- **Chatterbox**: [Resemble AI](https://github.com/resemble-ai/chatterbox)
- **Modifications**: Docker infrastructure and CUDA 13 patches for DGX Spark.
- **Blackwell/Docker Port**: [codingoai](https://github.com/codingoai/)
