import string

def main_program():
  text = input("Enter the text: ")
  
# print(set(string.punctuation)) #show the set of punctuation in the string.
  # without the set, it will not be detected. 
  # else it will be in a form of array if inclusion of the set() function
# since we confirm that "string.punctation" works. Then, we will going to use it to separate the text into chunks based from the presence of the punctuation

# create a method for dividing the text into subtext from the presence of the punctuation mark
def separate_text(text):
  
  #define the set of punctuation marks
  punctuation_marks = set(string.punctuation)
  
  #make the variables needed: 1. the array for substring and 2. the looping start == 0
  sub_sentences = []
  begin_loop = 0
  
  # use enumerate to access both index and the value
  # handling separating text
  for i, char in enumerate(text):
    if char in punctuation_marks:
      
      subsentence = text[begin_loop: i].strip()
      
      if subsentence:
        sub_sentences.append(subsentence)
        
      begin_loop= i+1
      
      last_subsentence = text[begin_loop:].strip()
      if last_subsentence:
        sub_sentences.append(last_subsentence)
    
      
  print(len(sub_sentences))
  for sentence in sub_sentences:
    print(sentence)

separate_text("Hello! how are you? It is a wonderful day")