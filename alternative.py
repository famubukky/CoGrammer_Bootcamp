#codes that read a string and make each alternate character into upper and lower case
def alternate_case(sentence):
    result = ""
    for i, char in enumerate(sentence):
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result
def alternate_word_case(sentence):
    words = sentence.split()
    result = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            result.append(word.lower())
        else:
            result.append(word.upper())
    return ' '.join(result)
if __name__ == "__main__":
    sentence = input("Enter a sentence: ")# line of code that show that user should enter a sentence
#Alternate character case
    alternate_char_case = alternate_case(sentence)
    print("Alternate character case:", alternate_char_case)
#Alternate word case
    alternate_word_case_result = alternate_word_case(sentence)
    print("Alternate word case:", alternate_word_case_result)#print the alternate word case


