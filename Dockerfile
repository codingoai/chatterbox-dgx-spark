# Switch to NVIDIA NGC image for Blackwell (sm_121) support
FROM nvcr.io/nvidia/pytorch:25.12-py3

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libsndfile1 \
    ffmpeg \
    git \
    cmake \
    && rm -rf /var/lib/apt/lists/*

# Workaround for numpy compatibility with Python 3.12 (default in NGC 25.12)
WORKDIR /workspace/chatterbox
COPY source_code/ .

# Relax numpy constraint
RUN sed -i 's/"numpy>=1.24.0,<1.26.0"/"numpy>=1.24.0"/g' pyproject.toml

# Generate constraints to lock pre-installed packages (specifically torch)
RUN pip list --format=freeze | grep -E "^torch==|^torchvision==" > constraints.txt

# Install hf_transfer (safe to install without constraints usually, but good practice)
RUN pip install --no-cache-dir hf_transfer

# Build Torchaudio from source using release/2.6 branch
# EXTENSIVE WARNING SUPPRESSION + CUSTOM CUDA 13 PATCHES
RUN git clone --recursive -b release/2.6 https://github.com/pytorch/audio.git /workspace/torchaudio_src && \
    cd /workspace/torchaudio_src && \
    # Remove Werror
    find . -name "CMakeLists.txt" -print0 | xargs -0 sed -i 's/-Werror//g' && \
    find . -name "*.py" -print0 | xargs -0 sed -i 's/-Werror//g' && \
    # Patch Code for CUDA 13 / PyTorch 2.10 Compatibility
    python3 /workspace/chatterbox/patch_torchaudio.py && \
    # Force empty warning list
    sed -i 's/warnings_possible_errors_defs = .*/warnings_possible_errors_defs = []/g' setup.py || true && \
    # Environment variables
    export CFLAGS="-w" && \
    export CXXFLAGS="-w" && \
    export TORCH_NVCC_FLAGS="-Xcudafe --display_error_number -w" && \
    pip install . --no-deps --no-build-isolation -c /workspace/chatterbox/constraints.txt

# Install Chatterbox dependencies with constraints to protect torch
RUN pip install -c constraints.txt \
    "librosa==0.11.0" \
    "transformers==4.46.3" \
    "diffusers==0.29.0" \
    "resemble-perth==1.0.1" \
    "conformer==0.3.2" \
    "safetensors==0.5.3" \
    "spacy-pkuseg" \
    "pykakasi==2.3.0" \
    "gradio==5.44.1" \
    "pyloudnorm" \
    "omegaconf"

# Install s3tokenizer separately to avoid dependency resolution issues with local torch
RUN pip install --no-deps "s3tokenizer==0.3.0"

# Install Chatterbox itself
RUN sed -i '/"torch==/d' pyproject.toml && \
    sed -i '/"torchaudio==/d' pyproject.toml && \
    pip install -e . --no-deps

# Default command
CMD ["/bin/bash"]
