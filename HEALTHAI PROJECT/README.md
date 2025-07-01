# HEALTH_AI_ASSISTANT

# 🤖 HealthAI – Intelligent Healthcare Assistant using IBM Granite

HealthAI is a powerful healthcare assistant powered by **IBM Granite's open-source LLM**. It helps patients with:

* 🗣️ **Natural-language health Q\&A**
* 🧫 **Disease prediction**
* 💊 **Personalized treatment recommendations**
* 📊 **Health metrics analytics**

Built using **Streamlit**, **Python**, and the **Granite-2B-Instruct model**, HealthAI bridges intelligent automation with accessible care.

---

## 📦 Features

* **Chat with an AI doctor** – Get empathetic, evidence-based answers.
* **Disease Prediction Engine** – Analyze symptoms, vitals & history.
* **Treatment Plan Generator** – Generate guideline-based care plans.
* **Interactive Health Analytics** – Visualize heart rate, blood pressure, glucose, and more.

---

## 🚀 Live Demo

> 🔗 *\[Add link here if deployed (Streamlit Cloud, etc.)]*

---

## 🧠 Model: IBM Granite 2B Instruct

This project uses the **IBM Granite 2B Instruct** language model for:
- Generating responses to patient questions
- Predicting likely diseases based on symptoms
- Crafting treatment plan suggestions

🔒 Model files are stored locally and loaded via `transformers` library.

---

### 📅 Download Instructions

1. [Download the model folder](https://huggingface.co/ibm-granite/granite-3.3-2b-instruct).
2. Alternatively, use `download_model.py` script to auto-download.
3. Place the downloaded folder as:

```
project_root/
├── app.py
├── model/
│   └── granite_loader.py
├── granite-3.3-2b-instruct/  ← Place model files here

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/HealthAI-Intelligent-Healthcare-Assistant-Using-IBM-Granite.git
cd HealthAI-Intelligent-Healthcare-Assistant-Using-IBM-Granite
```

### 2. Set up virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```
### 4. Install model

```bash
pip install download_model.py
```

### 5. Run the app

```bash
streamlit run app.py
```

---

## 🧠 Tech Stack

| Tool           | Purpose                        |
| -------------- | ------------------------------ |
| Streamlit      | Frontend + app logic           |
| Transformers   | Model loading & inference      |
| IBM Granite    | Base LLM (3B instruct)         |
| Plotly         | Analytics dashboard            |
| Pandas / NumPy | Data simulation & manipulation |

---

## 🛡️ Disclaimer

> This app is for **educational and research purposes only**.
> It does **not provide real medical advice**. Always consult a licensed physician for actual diagnosis or treatment.

---

## 👨‍💼 Author

**Murali Karthik**
📧 mailto: muralikarthikedu.com
🔗 https://linkedin.com/in/yourprofile | https://github.com/murali-karthik01

---

## 📂 Folder Structure

```
📆 HealthAI/
├── app.py                       # Main Streamlit app
├── model/
│   └── granite_loader.py        # Granite model loader
├── granite-3.3-2b-instruct/     # Model files (not committed to Git)
├── static/
│   └── css/style.css            # Optional custom styles
├── templates/                   # HTML templates (if needed)
├── requirements.txt             # Python dependencies
├── .env                         # Env variables (if any)
```

---

## ✅ To-Do / Improvements

* [ ] Add Hugging Face Hub integration for easier model loading
* [ ] Improve error handling & timeout management
* [ ] Add user login support for saving reports

---

## 📝 License

MIT License – *Free for use, modification, and distribution.*
