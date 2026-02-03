"""
Optional script if you want to host models locally instead of HF Inference API.[web:7]

Example:
  - Download LLaVA weights
  - Convert to ONNX for onnxruntime

For now, the backend uses HF hosted endpoints so this script is not required.
"""
from pathlib import Path

def main():
  models_dir = Path("models")
  models_dir.mkdir(exist_ok=True)
  print("Placeholder for local model download & ONNX export.")

if __name__ == "__main__":
  main()
