# 🔤 Day 9 – NLP Text Analyzer

> **Phase 2 · NLP Basics** | Built with Python, Flask & NLTK

A web-based **Text Analyzer** that demonstrates core NLP (Natural Language Processing) techniques on any 500+ word article.

---

## 🚀 Features

| Feature | Description |
|---|---|
| 📄 **Article Input** | Paste any 500+ word article or load the built-in sample |
| 🔤 **Tokenization** | Word & sentence tokenization via NLTK's `word_tokenize` / `sent_tokenize` |
| 🚫 **Stopword Removal** | Filters English stopwords (NLTK corpus) to highlight meaningful words |
| 🌱 **Stemming** | Reduces words to root form using Porter Stemmer (fast, rule-based) |
| 🔮 **Lemmatization** | POS-aware lemmatization using WordNet Lemmatizer (linguistically accurate) |
| 🔑 **Keyword Extraction** | Top-10 keywords ranked by lemma frequency |
| 📊 **Frequency Chart** | Animated horizontal bar chart for the top-20 most frequent words |
| ⚖️ **Stem vs Lemma Table** | Side-by-side comparison of original → stemmed → lemmatized forms |

---

## 🧠 NLP Concepts Explained

### 1. Tokenization
Splitting raw text into smaller units (tokens).  
- **Word tokenization** → splits text into individual words  
- **Sentence tokenization** → splits text into individual sentences  
- Used as the **first step** in every NLP pipeline.

### 2. Stopword Removal
Stopwords are high-frequency, low-meaning words (e.g., *the, is, at, which*).  
Removing them reduces noise and helps focus on content-bearing words.

### 3. Stemming (Porter Stemmer)
A rule-based algorithm that **chops word suffixes** to reach the stem.  
- Fast & simple  
- May produce non-dictionary words (e.g., *"studies"* → *"studi"*)

### 4. Lemmatization (WordNet Lemmatizer)
Uses a vocabulary & morphological analysis to find the **true base form** (lemma).  
- Slower but produces valid dictionary words  
- POS-aware for better accuracy (e.g., *"running"* → *"run"*, *"better"* → *"good"*)

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.10, Flask |
| NLP Engine | NLTK 3.9 |
| Frontend | Vanilla HTML + CSS + JavaScript |
| Tokenizer | `nltk.tokenize` (word & sentence) |
| Stopwords | `nltk.corpus.stopwords` |
| Stemmer | `nltk.stem.PorterStemmer` |
| Lemmatizer | `nltk.stem.WordNetLemmatizer` |
| Frequency | `nltk.probability.FreqDist` |

---

## ⚡ Quick Start

```bash
# 1. Clone / navigate to the project folder
cd Task-9

# 2. Install dependencies
pip install flask nltk

# 3. Run the app
python app.py

# 4. Open your browser
# http://127.0.0.1:5000
```

> NLTK data packages (punkt, stopwords, wordnet, etc.) are downloaded automatically on first run.

---

## 📁 Project Structure

```
Task-9/
├── app.py              # Flask backend + NLP logic
├── templates/
│   └── index.html      # Frontend UI (single-file, no dependencies)
├── requirements.txt
└── README.md
```

---

## 📸 What You'll See

1. **Input Panel** — Paste article or load the built-in 500-word sample  
2. **Statistics Bar** — Total words, sentences, tokens, stopwords removed, unique lemmas  
3. **Token Explorer** — Tabbed view: All Tokens → Clean → Stemmed → Lemmatized  
4. **Comparison Table** — Original vs Stemmed vs Lemmatized (first 20 words)  
5. **Keyword Cloud** — Top-10 keywords with frequency badges  
6. **Frequency Chart** — Animated bar chart for top-20 words  

---

*Day 9 | Python + AI Internship — Phase 2: NLP & Text AI*
