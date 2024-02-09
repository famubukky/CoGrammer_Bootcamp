
#The line of code to ask user a sentence and save the response and name it str_manip
str_manip = input("Enter a sentence:    ")

#The line of code that prints lenght of the sentence str_manip
print("length of the sentence:  ", len(str_manip))

#The line of code that ask for the last letter in str_manip and replace it with  @
last_letter = str_manip[-1]

str_manip_last = str_manip.replace(last_letter,  "@")

#The line of code that modified str_manip and print it
print("modified sentence:", str_manip_last)
 
#The line of code that prints the last three characters in str_manip backward      
print("Last 3 characters backward:", str_manip[-1:-4:-1])

#The line of code that displays the first 3 characters and last two character of str_manip
five_letter_word = str_manip[:3] + str_manip [-2:]

#line of code that print the five characters from str_manip
print("five_letter_word:", five_letter_word)


