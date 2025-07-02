<<<<<<< HEAD
#Word Analyzer 

##1 Input text file for analysis

text_file =[]
with open('sample.txt',encoding='utf-8') as texts:
    for word in texts:
        text_file.append(word.lower()) # for word constistancy convert string to lower case letter

##2 Cleaning : 
    
new_text_file = []
for text in text_file: #get only word to a new list
    new_list = ''
    for word in text: 
        if word.isalpha() or word.isspace(): # interating through each element if  elemnt contain alphabetic character or spaces 
            new_list += word # if condition met, add those element to a empty vairable 
    new_text_file.append(new_list) # use the string in the variable to append in a list

text_file_cleaned = [x.strip(' \n') for x in new_text_file] # remove trailing withspace and newline

##3 Split and make it to a list

split_word_list = []
for word in text_file_cleaned:
    split_word_list.extend(word.split(' '))

##4 convert list to a dict: unique word as key and count of unique word as value 

word_key = []
word_value = []
for x in split_word_list: # if word do not exist in key_word add, the word and add value 1 in the same index
    if x not in word_key:
        word_key.append(x)
        word_value.append(1)
    else:   # if word already exist in the list, addition value 1 to word_value on the index y
        y = word_key.index(x) 
        word_value[y] +=1 # this ensure that with every value + in the list is the same as position of key. 
word_dict = {word_key: word_value for word_key, word_value in zip(word_key,word_value) }

print(word_dict)
=======
#Word Analyzer 

##1 Input text file for analysis

text_file =[]
with open('sample.txt',encoding='utf-8') as texts:
    for word in texts:
        text_file.append(word.lower()) # for word constistancy convert string to lower case letter

##2 Cleaning : 
    
new_text_file = []
for text in text_file: #get only word to a new list
    new_list = ''
    for word in text: 
        if word.isalpha() or word.isspace(): # interating through each element if  elemnt contain alphabetic character or spaces 
            new_list += word # if condition met, add those element to a empty vairable 
    new_text_file.append(new_list) # use the string in the variable to append in a list

text_file_cleaned = [x.strip(' \n') for x in new_text_file] # remove trailing withspace and newline

##3 Split and make it to a list

split_word_list = []
for word in text_file_cleaned:
    split_word_list.extend(word.split(' '))

##4 convert list to a dict: unique word as key and count of unique word as value 

word_key = []
word_value = []
for x in split_word_list: # if word do not exist in key_word add, the word and add value 1 in the same index
    if x not in word_key:
        word_key.append(x)
        word_value.append(1)
    else:   # if word already exist in the list, addition value 1 to word_value on the index y
        y = word_key.index(x) 
        word_value[y] +=1 # this ensure that with every value + in the list is the same as position of key. 
word_dict = {word_key: word_value for word_key, word_value in zip(word_key,word_value) }

print(word_dict)
>>>>>>> ee145b63b671d23df84399afa77cf56341faedc4
