import os

def patch_file(path, search, replace, allow_missing=False):
    if not os.path.exists(path):
        if allow_missing:
            print(f"Skipping missing file: {path}")
            return
        else:
            # Try finding it if it's a relative path pattern? No, strict path for now.
            # But utils.h search was recursive.
            pass
    
    # Read
    try:
        with open(path, 'r') as f:
            content = f.read()
    except Exception as e:
        if allow_missing:
            print(f"Could not read {path}: {e}")
            return
        raise

    # Replace
    if search in content:
        print(f"Patching {path}...")
        new_content = content.replace(search, replace)
        with open(path, 'w') as f:
            f.write(new_content)
    else:
        print(f"Search string not found in {path}. Already patched or invalid?")

def main():
    base_dir = "/workspace/torchaudio_src"
    
    # 1. Patch utils.h (recursive search needed)
    print("Scanning for utils.h...")
    for root, dirs, files in os.walk(base_dir):
        if "utils.h" in files:
            path = os.path.join(root, "utils.h")
            patch_file(path, 
                      "#include <torch/csrc/stable/device.h>", 
                      "#include <torch/extension.h>")

    # 2. Patch compute.cu (Specific path)
    # src/libtorchaudio/forced_align/gpu/compute.cu
    compute_cu = os.path.join(base_dir, "src/libtorchaudio/forced_align/gpu/compute.cu")
    patch_file(compute_cu,
               "cub::Max()",
               "[] __device__ (scalar_t a, scalar_t b) { return a > b ? a : b; }",
               allow_missing=True)

    # 3. Patch ctc_prefix_decoder_kernel_v2.cu
    # src/libtorchaudio/cuctc/src/ctc_prefix_decoder_kernel_v2.cu
    decoder_cu = os.path.join(base_dir, "src/libtorchaudio/cuctc/src/ctc_prefix_decoder_kernel_v2.cu")
    patch_file(decoder_cu,
               "cub::FpLimits<float>::Lowest()",
               "-3.402823466e+38F",
               allow_missing=True)

if __name__ == "__main__":
    main()
