import nltk
nltk.download('punkt')


def equal_0s_1s_nlp(sentence):
    tokens = nltk.word_tokenize(sentence)
    joined_string = ''.join(tokens)  # Join tokens to form a string

    state = 0

    for char in joined_string:
        if char == '0':
            state += 1
        elif char == '1':
            state -= 1

        # If the state becomes negative at any point, the number of '1's exceeds '0's
        if state < 0:
            return False

    # If the state is zero at the end, there is an equal number of '0's and '1's
    return state == 0

# Test the finite state automaton with an NLTK tokenized sentence
test_sentence = "There are 101 people in the room, and 010 of them have left."
result = equal_0s_1s_nlp(test_sentence)
print(f"The sentence has an equal number of '0's and '1's: {result}")
