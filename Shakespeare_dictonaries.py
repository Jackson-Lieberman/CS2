"""
Shakespeare Play Analysis 
Student Name: Jackson Lieberman
Date: 2/27/26
Discription: 2. Open File for processing and create dictionary.
3. Write the Key and Value pairs to a file.
4. Graph file using Excel.
5. Upload (2) graphs as PDF and a link to your github
for the program’s code.
Bonuses:
Bugs:
Log: 1.0
"""
import string
import re
import csv
import matplotlib.pyplot as plt

                                                                               #asks what play the user wants to analyze
file = input('''                                                               
Which play would you like to look at:   
           1. All's Well That Ends Well (Comedy)
           2. Midsummer Night's Dream (Comedy)
           3. As You Like It (Comedy)
           4. The Tempest (Comedy)
           5. Comedy of Errors (Comedy)
           6. Hamlet (Tragedy)
           7. Othello (Tragedy)
           8. Macbeth (Tragedy)
           9. Romeo and Juliet (Tragedy)
           10. Antony and Cleopatra (Tragedy)
           11. Coriolanus (Tragedy)
           12. Cymbeline (Tragedy)
           13. Richard III (History)
           14. Henry V (History)
           15. Richard II (History)
           16. Henry IV Part 1 (History)
           17. Henry IV Part 2 (History)
           18. Henry VI Part 1 (History)
           19. Henry VI Part 2 (History)
           20. Henry VI Part 3 (History)
''')

if file == "1":                                                                #sets the file based on the response
    fname, outname = "All's_Well_That_Ends_Well.txt", "All's_Well_That_Ends_Well"
elif file == "2":
    fname, outname = "midsummer_nights_dream.txt", "midsummer_nights_dream"
elif file == "3":
    fname, outname = "as_you_like_it.txt", "as_you_like_it"
elif file == "4":
    fname, outname = "the_tempest.txt", "the_tempest"
elif file == "5":
    fname, outname = "Comedy_of_Errors.txt", "Comedy_of_Errors"
elif file == "6":
    fname, outname = "hamlet.txt", "hamlet"
elif file == "7":
    fname, outname = "othello.txt", "othello"
elif file == "8":
    fname, outname = "macbeth.txt", "macbeth"
elif file == "9":
    fname, outname = "romeo_and_juliet.txt", "romeo_and_juliet"
elif file == "10":
    fname, outname = "Antony_and_Cleopatra.txt", "Antony_and_Cleopatra"
elif file == "11":
    fname, outname = "Coriolanus.txt", "Coriolanus"
elif file == "12":
    fname, outname = "Cymbeline.txt", "Cymbeline"
elif file == "13":
    fname, outname = "richard_iii.txt", "richard_iii"
elif file == "14":
    fname, outname = "henry_v.txt", "henry_v"
elif file == "15":
    fname, outname = "richard_ii.txt", "richard_ii"
elif file == "16":
    fname, outname = "Henry_IV_part_1.txt", "Henry_IV_part_1"
elif file == "17":
    fname, outname = "Henry_IV_part_2.txt", "Henry_IV_part_2"
elif file == "18":
    fname, outname = "Henry_VI_part_1.txt", "Henry_VI_part_1"
elif file == "19":
    fname, outname = "Henry_VI_part_2.txt", "Henry_VI_part_2"
elif file == "20":
    fname, outname = "Henry_VI_part_3.txt", "Henry_VI_part_3"




try:                                                                           #tries to open the file and if this is not possible then it will exit the code
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()


                                                                               #define the regex pattern  with word boundaries
article_pattern = re.compile(r'\b(a|an|the|and|i|to|of|my|you|that|this|in|me|not|is|be|it|with|for|but|as|have|his|her|your|so|do|he|she|it|all|are|what|will|o|no|now|him|if|by|which|thou|thy|thee|by|they|we|on|here|sir|ll|or|let|our|s|at|was|how|shall|their|there|would|them|like|when|from|were|upon|most|more|come|make|tis|well|may|know|go|us|t|did|am|say|yet|such|some|one|had|hath)\b', re.IGNORECASE)            


counts = dict()                                                                #sets the counts to a dictionary
for line in fhand:                                                             #isolate each line
    line = line.rstrip()                                                       #strip the line from the right, so its just characters
    line = article_pattern.sub("", line)                                       #uses the regex to remove the articles
    line = line.translate(line.maketrans("", "", string.punctuation))          #removes all punctuation from the line
    line = line.lower()                                                        #makes the line lowercase
    words = line.split()                                                       #splits the line into a list of words
    for word in words:                                                         #for every word add it the counts dictonary if its not already there
        if word not in counts:
            counts[word] = 1
        else:                                                                  #if it is there add one to the value of the corrisponding word
            counts[word] += 1



sorted_words = sorted(counts.items(), key=lambda item: item[1], reverse=True)[:15]    #use lambda to sort the dictonary and take the ten highest values

print("Top 15 most frequent words:")
for word, count in sorted_words:                                               #prints the highest ten values         
    print(f"{word}: {count}")

topwords = dict(sorted_words)                                                  #sets the top words to an empty dictonary

output_file = f"{outname}.csv"                                                 # Set the name for your output CSV file

with open(output_file, 'w', newline='') as out:                                # Open the file for writing
    
    writer = csv.writer(out)                                                   # write the file
    
    writer.writerow(['Word', 'Count'])                                         # write the headers as the first row

    for word, count in topwords.items():                                       # Iterate through the dictionary and write each key/value pair as a row
        writer.writerow([word, count])

print(f"\nResults saved to '{output_file}'.")

words = list(topwords.keys())                                                  #makes a list of the top words
counts_list = list(topwords.values())                                          #makes a list of their frequency

plt.figure()                                                                   #creates a new figure object
plt.pie(counts_list, labels=words, autopct='%1.1f%%', startangle=140)               #creates a bar graph showing the words and their counts
plt.title(f"Top 15 Words: {outname.title()}")                                  #sets the title
plt.ylabel("Frequency")                                                        #labels the y 
plt.savefig(f"{outname}_graph.pdf")                                            #saves the chart
plt.show()                                                                     #shows the chart

print(f"\n'{outname}_graph.pdf' created.")







