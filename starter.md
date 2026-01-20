# Chatterbox Quick Start Guide

If you are just starting fresh, follow these steps to generate audio.

### 1. Prerequisites
Ensure your Hugging Face token is set in the `.env` file:
```bash
# Check if file exists and has content
cat .env
```
*(It should look like `HF_TOKEN=hf_...`)*

### 2. Build the Docker Image (One-time setup)
If you haven't built the image yet (or if you changed the Dockerfile), run:
```bash
./build.sh
```

### 3. Start the Container
This will start the environment and mount your source code:
```bash
./run.sh
```

### 4. Generate Audio (Inside the container)
Once you are inside the container (you will see a prompt like `root@<id>:/workspace/chatterbox#`), run your script:
```bash
python example_tts_turbo.py
```

### 5. Check Output
The audio file `test-turbo-manual-01.wav` will appear in your `source_code/` folder. You can play it from your host machine.
