
## 💬 Sentiment Analysis App  
**Standalone NLP Project** 

> A complete NLP pipeline for sentiment analysis. Includes preprocessing, training, evaluation, and a user-friendly interface for real-time sentiment prediction using a fine-tuned transformer model.

### What It Does
- Fine-tunes a transformer model on the IMDB movie review dataset  
- Analyzes user input for **positive** or **negative** sentiment  
- Provides **visual insights** like:
  - Sentiment distribution histogram
  - Confidence score with a progress bar
  - Interactive pie chart of prediction breakdown
- Includes full lifecycle: **preprocessing → training → inference → UI**

---

###  Tech Stack

| Component     | Tool                            |
|---------------|---------------------------------|
| Base Model    | `distilbert-base-uncased`       |
| Training      | Hugging Face Transformers       |
| Dataset       | IMDB (binary sentiment)         |
| UI            | Streamlit                       |
| Config        | YAML + Python class-based loader |
| Logging       | Python Logging Module           |

---

### 🧱 Project Structure
```
Sentiment-analysis/
├── app/                    # Streamlit UI
│   ├── app.py
│   └── main.py             # Orchestrates full pipeline
├── scripts/                # Preprocess, train, evaluate, predict
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
├── models/                 # Fine-tuned model artifacts
├── data/
│   ├── raw/
│   └── processed/
├── config/
│   ├── config.py
│   └── config.yaml
├── notebooks/              # Exploration / research notebook
├── logging/                # Logging logic and files
├── requirements.txt
└── README.md
```

---

### 🛠️ How to Run It Locally

1. **Install dependencies**
```bash
pip install -r requirements.txt
```

2. **(Optional) Preprocess + Train**
```bash
python app/main.py
```

3. **Launch the UI**
```bash
streamlit run app/app.py
```

---

### Features in the UI
-  Paste any English text and get a sentiment prediction  
-  Pie chart showing prediction confidence  
-  Word-by-word sentiment histogram  
-  Validation for short, numeric, or invalid inputs  
-  Logging system for tracking input and model behavior

---

###  Model Details
- Base: `distilbert-base-uncased`
- Fine-tuned on: IMDB binary sentiment dataset (positive/negative)
- Output: `LABEL_1` = Positive, `LABEL_0` = Negative

---



### ✍️ Author
**Mohannad karim**  
_Machine Learning & NLP Engineer_  
[Portfolio]
