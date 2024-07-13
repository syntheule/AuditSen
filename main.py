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
  begin_lopp = 0
  
print(enumerate("Hello"))