import nltk
import os

nltk_data_dir = os.path.join(os.path.dirname(__file__), 'nltk_data')
os.makedirs(nltk_data_dir, exist_ok=True)

print(f"Downloading NLTK data to {nltk_data_dir}...")

packages = ["punkt", "punkt_tab", "stopwords", "wordnet", "averaged_perceptron_tagger", "averaged_perceptron_tagger_eng", "omw-1.4"]
for pkg in packages:
    nltk.download(pkg, download_dir=nltk_data_dir, quiet=False)

print("NLTK data download complete.")
