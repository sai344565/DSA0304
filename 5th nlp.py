import nltk
from nltk.stem import PorterStemmer

# Download NLTK data (if not already downloaded)
nltk.download('punkt')

# Initialize the Porter Stemmer
porter_stemmer = PorterStemmer()

# List of words to be stemmed
words_to_stem = ["jumps", "jumping", "jumper", "jumped", "easily", "running", "lies", "flying", "flies"]

# Perform stemming on each word
stemmed_words = [porter_stemmer.stem(word) for word in words_to_stem]

# Display the results
print("Original Words:", words_to_stem)
print("Stemmed Words:", stemmed_words)
