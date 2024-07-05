import string

def separate_sentences(text):
    # Define a set of punctuation marks
    punctuation_marks = set(string.punctuation)
    
    # Initialize variables
    subsentences = []
    start = 0
    
    for i, char in enumerate(text):
        if char in punctuation_marks:
            # Extract the subsentence from the start index to the current index
            subsentence = text[start:i].strip()
            
            # Remove the punctuation mark
            if subsentence:
                if subsentence[-1] in punctuation_marks:
                    subsentence = subsentence[:-1].strip()
            
            # Add the non-empty subsentence to the list
            if subsentence:
                subsentences.append(subsentence)
            
            # Update the start index for the next subsentence
            start = i + 1
    
    # Add the last subsentence if it exists and is non-empty
    last_subsentence = text[start:].strip()
    if last_subsentence:
        subsentences.append(last_subsentence)
    
    return subsentences

def preprocess_text(text):

    text = text.lower()
    # Tokenize the text
    tokens = text.split()
    
    # Remove stop words
    # stop_words = set(stopwords.words('english'))
    # tokens = [token for token in tokens if token.lower() not in stop_words]
    
    # Remove one-letter words
    tokens = [token for token in tokens if len(token) > 1]
    
    # Define a list of common interjections
    interjections = set(["wow", "oh", "hmm", "ah"])
    
    # Remove interjections
    tokens = [token for token in tokens if token.lower() not in interjections]
    
    return ' '.join(tokens)

# Input text
text = "Wow! This is a sample sentence. It has punctuation marks, such as commas and periods. Another sentence follows!"

# Separate the text into subsentences based on punctuation marks
subsentences = separate_sentences(text)

# Preprocess each subsentence
preprocessed_subsentences = [preprocess_text(subsentence) for subsentence in subsentences]

# Print the preprocessed subsentences
for idx, subsentence in enumerate(preprocessed_subsentences):
    print(f"Preprocessed Subsentence {idx + 1}: {subsentence}")
    
    
# ---- Main algorithm for the pure text analysis -----


# # Input text
# text = "This is a sample sentence. It has punctuation marks, such as commas and periods. Another sentence follows!"

# # Separate the text into subsentences based on punctuation marks
# subsentences = separate_sentences(text)

# # Print the subsentences
# for idx, subsentence in enumerate(subsentences):
#     print(f"Subsentence {idx + 1}: {subsentence}")