"""
Day 9 – NLP Basics: Text Analyzer
Concepts: Tokenization · Stopwords · Stemming · Lemmatization · Keyword Extraction
"""

from flask import Flask, request, jsonify, render_template
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist
import re
import string
from collections import Counter

import os
nltk_data_dir = os.path.join(os.path.dirname(__file__), 'nltk_data')
nltk.data.path.append(nltk_data_dir)

app = Flask(__name__)

STOP_WORDS = set(stopwords.words("english"))
STEMMER    = PorterStemmer()
LEMMATIZER = WordNetLemmatizer()

SAMPLE_TEXT = """Artificial Intelligence and Natural Language Processing: Transforming the Way Computers Understand Human Language

Artificial intelligence has fundamentally changed the way we interact with technology. At the heart of many modern AI systems lies Natural Language Processing, commonly referred to as NLP. NLP is a branch of artificial intelligence that enables computers to understand, interpret, and generate human language in a meaningful way. From virtual assistants like Siri and Alexa to powerful language models like ChatGPT, NLP powers some of the most transformative technologies of our time.

The history of Natural Language Processing dates back to the 1950s, when Alan Turing proposed his famous Turing Test, which evaluated a machine's ability to exhibit intelligent behavior indistinguishable from that of a human. Early NLP systems relied heavily on hand-crafted rules and dictionaries. These rule-based systems were limited in scope and struggled to handle the complexity and ambiguity of human language. However, with the rise of machine learning and deep learning, NLP has experienced remarkable progress over the past decade.

One of the fundamental steps in any NLP pipeline is tokenization. Tokenization is the process of breaking down a piece of text into smaller units called tokens. These tokens can be words, sentences, or even subwords, depending on the application. Word tokenization splits text into individual words, while sentence tokenization splits a paragraph or document into individual sentences. Tokenization forms the very first step in almost every NLP task, because computers cannot process raw text directly — they need structured units to work with.

After tokenization, the next important step is removing stopwords. Stopwords are commonly used words in a language, such as "the", "is", "at", "which", and "on", that carry little meaningful information on their own. When analyzing text for important themes or topics, these words add noise without contributing value. By filtering out stopwords, we can focus on the words that actually carry meaning in the text. Stop word removal is especially useful in tasks like text classification, sentiment analysis, and information retrieval.

Stemming and lemmatization are two techniques used to reduce words to their base or root form. Stemming applies a rough algorithm that chops off common suffixes from words. For example, the words "running", "runner", and "runs" would all be reduced to "run". Stemming is fast and simple, but sometimes produces words that are not real dictionary words — for example, "studies" might become "studi". Lemmatization, on the other hand, uses a vocabulary and morphological analysis to return the proper base form of a word, known as its lemma. While lemmatization is slower, it produces linguistically valid base forms.

Keyword extraction is the process of identifying the most important and relevant words or phrases in a piece of text. It is widely used in search engines, document summarization, and content tagging systems. Techniques for keyword extraction include statistical approaches like Term Frequency-Inverse Document Frequency, or TF-IDF, as well as graph-based methods like TextRank. Machine learning-based approaches have also proven effective in automatically identifying keyphrases that represent the core topics of a document.

As we move into the era of large language models and generative AI, NLP has become more important than ever. Technologies like Retrieval Augmented Generation, or RAG, combine NLP with information retrieval to allow AI systems to answer questions based on specific knowledge bases. Transformer models such as BERT, GPT, and T5 have pushed the state of the art across virtually every NLP benchmark, from question answering to machine translation. The future of human-computer interaction is undeniably tied to advances in Natural Language Processing.

Today, NLP is applied across a wide range of industries. In healthcare, NLP systems extract clinical information from medical records. In finance, sentiment analysis tools scan news articles and social media to predict market trends. In customer service, chatbots powered by NLP handle millions of queries every day. Education platforms use NLP to provide personalized feedback and automated essay scoring. The versatility of NLP is one of the main reasons it remains one of the most active research areas in artificial intelligence."""


def clean_and_tokenize(text: str):
    text_clean = re.sub(r"[^a-zA-Z\s]", " ", text)
    tokens = word_tokenize(text_clean.lower())
    return [t for t in tokens if t.isalpha() and len(t) > 1]


def get_pos_tag(word: str) -> str:
    from nltk import pos_tag as _pos_tag
    from nltk.corpus import wordnet
    tag = _pos_tag([word])[0][1][0].upper()
    tag_map = {"J": wordnet.ADJ, "V": wordnet.VERB, "R": wordnet.ADV}
    return tag_map.get(tag, wordnet.NOUN)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sample", methods=["GET"])
def sample():
    return jsonify({"text": SAMPLE_TEXT})


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json(force=True)
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"error": "No text provided."}), 400

    word_count = len(text.split())
    if word_count < 100:
        return jsonify({"error": "Please provide at least 100 words for meaningful analysis."}), 400

    sentences   = sent_tokenize(text)
    word_tokens = clean_and_tokenize(text)

    clean_tokens = [w for w in word_tokens if w not in STOP_WORDS]

    stemmed = [STEMMER.stem(w) for w in clean_tokens]

    lemmatized = [LEMMATIZER.lemmatize(w, get_pos_tag(w)) for w in clean_tokens]

    freq_dist = FreqDist(lemmatized)
    top20     = freq_dist.most_common(20)
    top10_kw  = freq_dist.most_common(10)
    max_freq  = top20[0][1] if top20 else 1

    n = min(20, len(clean_tokens))
    comparison = [
        {
            "original":   clean_tokens[i],
            "stemmed":    stemmed[i],
            "lemmatized": lemmatized[i],
        }
        for i in range(n)
    ]

    unique_lemmas = len(set(lemmatized))

    sent_lengths = [len(s.split()) for s in sentences]
    avg_sent_len = round(sum(sent_lengths) / len(sent_lengths), 1) if sent_lengths else 0

    return jsonify({
        "stats": {
            "word_count":        word_count,
            "total_chars":       len(text),
            "total_sentences":   len(sentences),
            "total_tokens":      len(word_tokens),
            "clean_tokens":      len(clean_tokens),
            "stopwords_removed": len(word_tokens) - len(clean_tokens),
            "unique_lemmas":     unique_lemmas,
            "avg_sentence_len":  avg_sent_len,
        },
        "token_preview":  word_tokens[:30],
        "clean_preview":  clean_tokens[:30],
        "stemmed_preview": stemmed[:30],
        "lemmatized_preview": lemmatized[:30],
        "comparison":     comparison,
        "keywords": [
            {"word": w, "frequency": f, "pct": round(f / max_freq * 100)}
            for w, f in top10_kw
        ],
        "frequent_words": [
            {"word": w, "frequency": f, "pct": round(f / max_freq * 100)}
            for w, f in top20
        ],
        "full_word_tokens": word_tokens,
        "full_sentences": sentences,
        "full_clean_tokens": clean_tokens,
        "removed_stopwords": [w for w in word_tokens if w in STOP_WORDS]
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
