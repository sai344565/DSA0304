# Define the finite state machine rules for past tense verb detection and conversion
verb_rules = [
    (r'walks?', 'walked'),  # Rule for 'walk' verbs
    (r'jumps?', 'jumped')  # Rule for 'jump' verbs
]

def parse_sentence(sentence):
    # Apply rules to the sentence
    for present, past in verb_rules:
        sentence = re.sub(present, past, sentence)
    return sentence

# Example sentences
sentences = ["She walked to the park yesterday", "He jumped over the fence"]

# Parse and generate past tense forms of verbs in sentences
for sentence in sentences:
    past_tense_sentence = parse_sentence(sentence)
    print(f"Original: {sentence}")
    print(f"Past Tense: {past_tense_sentence}\n")
