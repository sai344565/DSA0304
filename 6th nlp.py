import nltk

# Given text
text = "The sun is shining brightly. I love reading interesting books."

# Tokenize the text into sentences
sentences = nltk.sent_tokenize(text)

# Perform part-of-speech tagging for each sentence
for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(words)
    print(tagged_words)
