import torchaudio as ta
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
import torch

# Define device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Loading ChatterboxMultilingualTTS on {device}...")

# Load the Multilingual model
model = ChatterboxMultilingualTTS.from_pretrained(device=device)

# # 1. English
# print("Generating English...")
# text_en = "Hello! This is a test of the multilingual capabilities of Chatterbox."
# wav_en = model.generate(text_en, language_id="en")
# ta.save("test-multi-en.wav", wav_en, model.sr)

# 2. Korean (Hangul)
print("Generating Korean...")
text_ko = "안녕하세요! 채터박스 다국어 모델 테스트입니다."
wav_ko = model.generate(text_ko, language_id="ko")
ta.save("test-multi-ko.wav", wav_ko, model.sr)

# # 3. Japanese
# print("Generating Japanese...")
# text_ja = "こんにちは！これは多言語音声合成のテストです。"
# wav_ja = model.generate(text_ja, language_id="ja")
# ta.save("test-multi-ja.wav", wav_ja, model.sr)

# # 4. French
# print("Generating French...")
# text_fr = "Bonjour, comment ça va? Ceci est le modèle de synthèse vocale multilingue."
# wav_fr = model.generate(text_fr, language_id="fr")
# ta.save("test-multi-fr.wav", wav_fr, model.sr)

# print("Done! output files: test-multi-en.wav, test-multi-ko.wav, test-multi-ja.wav, test-multi-fr.wav")
print("Done!")
