# 🎨 AI Moodboard Composer

**AI Moodboard Composer** is a simple yet creative Streamlit web app that uses generative AI to help designers, creatives, and marketers generate visual inspiration from a text prompt.

---

## 🚀 Built With

- [Cohere](https://cohere.ai) – for creative prompt expansion
- [Colormind](http://colormind.io/) – for generating aesthetic color palettes
- (Optional) HuggingFace – for text-to-image generation *(disabled in this version)*

---

## 🖼️ Features

- 🔠 Expand short theme prompts like `cozy autumn` or `vintage sci-fi` into rich creative descriptions.
- 🎨 Generate beautiful color palettes instantly based on the prompt.
- 🤖 Use LLMs to spark creative inspiration.
- ⚡ Fast, lightweight, and **100% free to use**.

---

## ⚙️ Setup Instructions

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-moodboard-composer.git
cd ai-moodboard-composer
```

### 🔐 2. Create a .env File
Create a .env file in the root folder and add:

```ini
COHERE_API_KEY=your-cohere-key-here
HUGGINGFACE_API_TOKEN=your-huggingface-token-here
```
💡 If you’re not using image generation, the Hugging Face token can be skipped.

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```
Or manually:

```bash
pip install streamlit requests cohere python-dotenv huggingface_hub pillow
```

### ▶️ 4. Run the App

```bash
streamlit run app.py
```

### 🤖 AI Used
Cohere Command Model: Expands brief themes into detailed prompts.

Colormind API: Curates harmonious color palettes.

(Optional) HuggingFace: For AI-generated images (disabled in this build).

🙌 Contributing
Pull requests are welcome! Feel free to open an issue or suggest new features.

### Built with ❤️ by [Neo] :)
