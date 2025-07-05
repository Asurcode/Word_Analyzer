#Word Analyzer 

##1 Input text file for analysis
text_file =[]
try:
    with open(input('enter file name \n'),encoding='utf-8') as texts:
        for word in texts:
            text_file.append(word.lower()) # for word constistancy convert string to lower case letter
except Exception as e:
    print(f"Error reading file: {e}" )
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

##4 make dictionary of unique word as key and workd frequancy of the word as value
from collections import Counter
    #counter does not include empty string so there is no need to refine the above code for cases like empty string
word_freq = Counter(split_word_list)
print(word_freq)
print(f'Ther are {len(word_freq)} unique words in the text file')


##5 save result as a csv file
import csv 

with open('wordfreq.csv', 'w', newline='') as word_file:
    writer = csv.writer(word_file)
    writer.writerow(['word','frequency']) # naming column 
    for word, freq in word_freq.items():
        writer.writerow([word, freq])

##6 word cloud

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(word_freq)

# Display the generated image
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off") # Hide the axes
plt.show()

# # save the word cloud image
# wordcloud.to_file("wordcloud_from_dict.png")