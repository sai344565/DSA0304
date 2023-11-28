import nltk
nltk.download('punkt')
nltk.download('universal_tagset')
nltk.download('averaged_perceptron_tagger')


sentences = [
    "The red car stopped at the traffic light",
    "She quickly ran to catch the bus"
]

# Tokenizing and tagging each sentence using NLTK's default tagger
for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(words, tagset='universal')
    print(tagged_words)
