import nltk

# Define the patterns and their corresponding parts of speech
patterns = [
    (r'\b(?:Thelthe)\b', 'DET'),    # Matches 'The' or 'the' as determiners
    (r'\b(?:cat|dog)\b', 'NOUN'),  # Matches 'cat' or 'dog' as nouns
    (r'\b(?:islamlare)\b', 'VERB'),  # Matches 'is,' 'am,' or 'are' as verbs
    (r'\b(?:quickly|brightly)\b', 'ADV'),  # Matches 'quickly' or 'brightly' as adverbs
    (r'\b(?:[A-Za-z]+)\b', 'NOUN')  # Matches any other words as nouns
]

# Create a RegexpTagger using the defined patterns
regexp_tagger = nltk.RegexpTagger(patterns)

# Test sentences
sentences = [
    "The cat quickly runs.",
    "She is happy.",
    "The dog is running."
]

# Tagging each sentence using the RegexpTagger
for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    tagged_words = regexp_tagger.tag(words)
    print(tagged_words)
