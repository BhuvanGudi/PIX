# PIX: AI Text-to-Image Generator

**PIX** is a Python-powered AI image generator that transforms text prompts into unique visuals using the Stable Diffusion model. Designed for both CUDA (GPU) and CPU environments, it's perfect for creative projects, prototyping, or experimenting with AI-generated art.

---

## 🚀 Features
- 🎨 Generates images from text prompts
- ⚡ Fast processing with CUDA (GPU) support
- 🖥️ CPU-compatible version available
- 🐍 Built entirely with Python
- 🔧 Easy setup and usage

---

# 📋 Requirements

## Software Requirements
- **Python 3.x**  
  Make sure you have Python 3 installed. You can download it from the [official Python website](https://www.python.org/downloads/).

- **Hugging Face API Access**  
  A valid [Hugging Face](https://huggingface.co/) account is required to obtain an API token.

## Hardware Requirements

### 🔧 CUDA (GPU) Version
- NVIDIA GPU with CUDA support
- At least **2.5 GB of VRAM** (Some models may require more for optimal performance)

### 🖥️ CPU Version
- No dedicated GPU required  
  _(Note: Processing speed will be slower compared to GPU execution)_


---

## 📥 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/pix.git
cd pix
```

### 2️⃣ Set Up a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # For Unix or MacOS
venv\Scripts\activate    # For Windows
```

### 3️⃣ Install Dependencies

#### For CUDA (GPU) Usage:
```bash
pip install -r requirements_cuda.txt
```

#### For CPU Usage:
```bash
pip install -r requirements.txt
```

---

## 🔑 Hugging Face Authentication
1. Sign up or log in at [Hugging Face](https://huggingface.co/).
2. Generate an access token from your [account settings](https://huggingface.co/settings/tokens).
3. Add the token to the appropriate file:
   - For CUDA: Edit `authtoken_cuda.py`
   - For CPU: Edit `authtoken.py`

Example:
```python
auth_token = "YOUR_HUGGING_FACE_TOKEN"
```

---

## ⚙️ Usage

### Running on CUDA (GPU)
```bash
python app_cuda.py
```

### Running on CPU
```bash
python app.py
```

Once running:
1. Enter your text prompt in the input box.
2. Click the **Generate** button.
3. The AI-generated image will be displayed and saved as `generatedimage.png`.

---

## 🗂️ Project Structure
```
PIX/
│
├── app.py                 # CPU version
├── app_cuda.py            # CUDA (GPU) version
├── authtoken.py           # CPU Hugging Face token
├── authtoken_cuda.py      # CUDA Hugging Face token
├── requirements.txt       # CPU dependencies
├── requirements_cuda.txt  # CUDA dependencies
├── README.md              # Project documentation
└── .idea/                 # Project settings (optional)
```

---

## ❗ Troubleshooting
- **CUDA Errors**: Ensure the correct version of PyTorch is installed using:
  ```bash
  pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
  ```
- **Slow Performance**: Use the GPU version for faster image generation.
- **Invalid Token**: Regenerate your Hugging Face token and update the `authtoken.py` or `authtoken_cuda.py`.

---

## 📜 License
This project is licensed under the MIT License.

---

## 🙏 Acknowledgments
- [Hugging Face](https://huggingface.co/)
- [Stable Diffusion](https://stability.ai/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)

---

Created by **BhuvanGudi** 🚀

