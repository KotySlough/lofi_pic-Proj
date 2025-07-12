# 🎨 Lifo Pic Project

Transform your headshot into a **cartoonish lofi aesthetic** using Python, OpenCV, and Pillow.

This project applies:
- 🖍️ Cartoon-style edge detection  
- 🔥 Warm color toning  
- ✨ Grain + vignette overlays for that cozy lofi vibe

---

## 🛠️ Features

- Convert portraits into cartoon-style images  
- Apply warm tones reminiscent of vintage/lofi art  
- Add grain and vignette for texture and focus  

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```text
opencv-python
Pillow
numpy
```

---

## 🚀 Usage

Run the script from terminal:

```bash
python lifo_pic_proj.py input.jpg output.jpg
```

### ✅ Example

```bash
python lifo_pic_proj.py picproj.jpg picproj_lofi.jpg
```

The transformed image will be saved as `picproj_lofi.jpg`.

---

## 📁 Project Structure

```text
lifo-pic-proj/
├── lifo_pic_proj.py         # Main script  
├── requirements.txt         # Python dependencies  
├── README.md                # This file  
├── picproj.jpg              # (Your input image)  
└── picproj_lofi.jpg         # (Output image generated)
```

---

## 🧠 How It Works

1. Cartoonify image with OpenCV (edge detection + bilateral filters)  
2. Convert to PIL for fine-tuning:  
   - Warm color transform  
   - Add random grain (like film)  
   - Apply soft vignette for focus

---

## 📸 Example Output

> *(Add a side-by-side screenshot or before/after if you'd like!)*

---

## 📝 License

This project is open-source under the MIT License.
