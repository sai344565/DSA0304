import nltk
nltk.download('averaged_perceptron_tagger')

sentence = "Unhappily, she ran quickly"

# Tokenize the sentence into words
words = nltk.word_tokenize(sentence)

# Perform part-of-speech tagging
tagged_words = nltk.pos_tag(words)

print("Morphological analysis:")
for word, tag in tagged_words:
    print(f"Word: {word}, Tag: {tag}")
