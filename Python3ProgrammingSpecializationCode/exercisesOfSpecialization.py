#1) rainfall_mi is a string that contains the average number of inches of rainfall in 
# Michigan for every month (in inches) with every month separated by a comma. Write 
# code to compute the number of months that have more than 3 inches of rainfall. Store
#  the result in the variable num_rainy_months. In other words, count the number of 
# items with values > 3.0.
#
#Hard-coded answers will receive no credit.

rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
l = rainfall_mi.split(",")
num_rainy_months = 0

for i in l:
    if i > 3.0:
        num_rainy_months += 1

###########################################################################################

#2) The variable sentence stores a string. 
# Write code to determine how many words in sentence start and end with the same 
# letter, including one-letter words. Store the result in the 
# variable same_letter_count.
#Hard-coded answers will receive no credit.

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

s = sentence.split(" ")
same_letter_count=0
for w in s:
    if w[0]==w[-1]:
        same_letter_count+=1


############################################################################################

#Write code to count the number of strings in list items that have the character w in it.
# Assign that number to the variable acc_num.

#HINT 1: Use the accumulation pattern!

#HINT 2: the in operator checks whether a substring is present in a string.

#Hard-coded answers will receive no credit.

items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]

acc_num=0
for w in items:
    if "w" in w:
        acc_num+=1


############################################################################################
#Write code that counts the number of words in sentence that contain either an “a” or an “e”. Store the result in the variable num_a_or_e.

#Note 1: be sure to not double-count words that contain both an a and an e.

#HINT 1: Use the in operator.

#HINT 2: You can either use or or elif.

#Hard-coded answers will receive no credit.

sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
s=sentence.split()
num_a_or_e=0
for w in s:
    if "a" in w or "e" in w:
        num_a_or_e+=1


#Write code that will count the number of vowels in the sentence s and assign the result to the
# variable num_vowels. For this problem, vowels are only a, e, i, o, and u. Hint: use the in 
# operator with vowels

s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
num_vowels=0
for l in s:
    if l in vowels:
        num_vowels+=1

#Currently there is a string called str1. 
# Write code to create a list called chars which should contain the characters from str1. 
# Each character in str1 should be its own element in the list chars.

str1 = "I love python"
chars = []
for c in str1:
    chars.append(c)

#Below are a set of scores that students have received in the past semester. Write code to 
# determine how many are 90 or above and assign that result to the value a_scores.

scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
scoress = scores.split()
a_scores=0
for int(n) in scoress:
    if n >= 90:
        a_scores+=1


#Write code that uses the string stored in org and creates an acronym which is assigned to
#  the variable acro. Only the first letter of each word should be used, each letter in the 
# acronym should be a capital letter, and there should be nothing to separate the letters of
#  the acronym. Words that should not be included in the acronym are stored in the list 
# stopwords. For example, if org was assigned the string “hello to world” then the resulting
#  acronym should be “HW”.

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"

acro=""
org = org.replace(",","")
s = org.split()
print(s)
for w in s:
    if not w in stopwords:
        acro = acro + w[0].upper()
print(s)


#Provided is a list of data about a store’s inventory where each item in the list
#  represents the name of an item, how much is in stock, and how much it costs. Print
#  out each item in the list with the same formatting, using the .format method (not string
#  concatenation). For example, the first print statment should read The store has 12 
# shoes, each for 29.99 USD.

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for s in inventory:
    sc = s.replace(",","")
    l = sc.split()
    print("The store has {} {}, each for {} USD.".format(l[1],l[0],l[2]))


#A palindrome is a phrase that, if reversed, would read the exact same.
#  Write code that checks if p_phrase is a palindrome by reversing it and then checking
#  if the reversed version is equal to the original. Assign the reversed version of p_phrase
#  to the variable r_phrase so that we can check your work.

p_phrase = "was it a car or a cat I saw"
r_phrase=""
for c in p_phrase:
    r_phrase = c+r_phrase



#Write code that uses the string stored in sent and creates an acronym which is assigned to
#  the variable acro. The first two letters of each word should be used, each letter in the
#  acronym should be a capital letter, and each element of the acronym should be separated 
# by a “. ” (dot and space). Words that should not be included in the acronym are stored in
#  the list stopwords. For example, if sent was assigned the string “height and ewok wonder” 
# then the resulting acronym should be “HE. EW. WO”.

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro=""
s = sent.split()
for w in s:
    if not w in stopwords:
        acro += w[0].upper()+w[1].upper()
        if w != s[-1]:
            acro += ". "

#The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. 
# Find the total number of characters in the file and save to the variable num.
file_manager = open("travel_plans.txt", "r")
content = file_manager.read()
num = len(content)

#We have provided a file called emotion_words.txt that contains lines of words that describe emotions.
#  Find the total number of words in the file and assign this value to the variable num_words.
file_ref = open("emotion_words.txt","r")
num_words=0
for l in file_ref:
    num_words += len(l.split())


#Assign to the variable num_lines the number of lines in the file school_prompt.txt.
file_ref = open("school_prompt.txt","1")
lines = file_ref.readlines()
num_lines = len(lines)

#Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
file_ref = open("school_prompt.txt","1")
content = file_ref.read()
beginning_chars = content[:30]

#Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called 
# three.
file_ref = open("school_prompt.txt","1")
three=[]
for line in file_ref:
    words = line.split()
    three.append(words[2])

#Challenge: Create a list called emotions that contains the first word of every line in 
# emotion_words.txt.
file_ref = open("emotion_words.txt","1")
emotions=[]
for line in file_ref:
    words = line.split()
    emotions.append(words[0])

#Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars
file_ref = open("travel_plans.txt","r")
content = file_ref.read()
first_chars = content[:33]

#Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the
# word to a list called p_words
file_ref = open("school_prompt.txt","1")
content = file_ref.read().split()
p_words = []
for w in content:
    if "p" in w:
        p_words.append(w)


#Dictionaries####################
#

Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}

juniorListOfValues = Junior.values()
juniorListOfKeys   = Junior.keys()
juniorListOfTuples = Junior.items()

for key in Junior:
    print('key:',key)

#The dictionary Junior shows a schedule for a junior year semester. The key is the course name
#  and the value is the number of credits. Find the total number of credits taken this semester 
# and assign it to the variable credits. Do not hardcode this – use dictionary accumulation!
Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits=0
for k in Junior:
    credits+=Junior[k]
#or
Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits=0
for v in Junior.values():
    credits+=v


#Create a dictionary, freq, that displays each character in string str1 as the key and its frequency 
# as the value.
str1 = "peter piper picked a peck of pickled peppers"
freq = {}
for c in str1:
    if c not in freq:
        freq[c] = str1.count(c)


#Create a dictionary, freq_words, that contains each word in string str1 as the key and its frequency
#  as the value.
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words = {}
s = str1.split()
for w in s:
    if freq_words.get(w,0) == 0: 
        freq_words[w] = 1
    else:
        freq_words[w] += 1

#Create a dictionary called wrd_d from the string sent, so that the key is a word and the 
# value is how many times you have seen that word.
sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
s = sent.split()
wrd_d = {}
for w in s:
    if w not in wrd_d:
        wrd_d[w]=1
    else:
        wrd_d[w]+=1
#Create a dictionary called low_d that keeps track of all the characters in the string p and notes
#  how many times each character was seen. Make sure that there are no repeats of characters as keys,
#  such that “T” and “t” are both seen as a “t” for example.
p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
pl = p.lower()
low_d={}
for c in pl:
    if c not in low_d:
        low_d[c] = pl.count(c)

#Find the least frequent letter. Create the dictionary characters that shows each character 
# from string sally and its frequency. Then, find the least frequent letter in the string and 
# assign the letter to the variable worst_char.
sally = "sally sells sea shells by the sea shore and by the road"
characters={}
for c in sally:
    if c not in characters:
        characters[c] = sally.count(c)

worst_char = ""
worst_value = 0       
for c in characters:
    if worst_char == "":
        worst_char = c
        worst_value = characters[c]
    if characters[c] < worst_value:
        worst_char = c
        worst_value = characters[c]

#or
placement = "Beaches are cool places to visit in spring"
d = {}
for c in placement:
    if c not in d:
        d[c]=0
    d[c] += 1
worst_value = min(d.values())


#Create the dictionary characters that shows each character from the string sally and its frequency. Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.

sally = "sally sells sea shells by the sea shore"
characters={}
best_char = ""
for c in sally:
    if best_char == "":
        best_char = c
        
    if c not in characters:
        characters[c] = sally.count(c)
        if characters[c] > characters[best_char]:
            best_char = c

#Tuples#######################################

#Given is the dictionary, gold, which shows the country and the number of gold medals they have 
# earned so far in the 2016 Olympics. Create a list, num_medals, that contains only the number of 
# medals for each country. You must use the .items() method. Note: The .items() method provides a 
# list of tuples. Do not use .keys() method.

gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}
num_medals=[]
for i in gold.items():
    num_medals.append(i[1])


gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}
num_medals=[]
for country, n_medals in gold.items():
    num_medals.append(n_medals)


#while loop######

#Write a function called check_nums that takes a list as its parameter, and contains 
# a while loop that only stops once the element of the list is the number 7. What is
#  returned is a list of all of the numbers up until it reaches 7.

def check_nums(l):
    i=0
    lst=[]
    while i < len(l):
        if l[i] == 7:
            break
        lst.append(l[i])
        i+=1
    return lst

#Below is a for loop that works. Underneath the for loop, rewrite the problem so 
# that it does the same thing, but using a while loop instead of a for loop. Assign the 
# accumulated total in the while loop code to the variable sum2. Once complete, sum2 should 
# equal sum1.

sum2=0
i=0
while i<len(lst):
    sum2 += lst[i]
    i+=1

#Write a function called checkingIfIn that takes three parameters. The first is a required parameter,
#  which should be a string. The second is an optional parameter called direction with a default value
#  of True. The third is an optional parameter called d that has a default value 
# of {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}. 
# Write the function checkingIfIn so that when the second parameter is True, it checks to see if the
#  first parameter is a key in the third parameter; if it is, return True, otherwise return False.

def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
       return a in d
    else:
        return a not in d


#sorting######
#Sort the following list by each element’s second letter a to z. Do so by using lambda. 
# Assign the resulting value to the variable lambda_sort.

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

def second(s):
    return s[1:]

l = lambda ex_lst: sorted(ex_lst, key=second)
lambda_sort = l(ex_lst)

#or
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

lambda_sort = sorted(ex_lst, key= lambda x: x[1:])


#Create a function called last_four that takes in an ID number and returns the last four digits. 
# For example, the number 17573005 should return 3005. Then, use this function to sort the list
# of ids stored in the variable, ids, from lowest to highest. Save this sorted list in the variable, sorted_ids. Hint: Remember that only strings can be indexed, so conversions may be needed.

def last_four(x):
    return str(x)[-4:]

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_ids = sorted(ids, key=last_four)


#Sort the list ids by the last four digits of each id. Do this using lambda and not using a defined function. 
# Save this sorted list in the variable sorted_id.
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_id = sorted(ids, key = lambda x: x%17570)

#or
sorted_id = sorted(ids, key = lambda x: str(x)[-4:])



#Given the same dictionary, medals, now sort by the medal count. Save the three countries with the highest 
# medal count to the list, top_three.
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}

top_three = sorted(medals, reverse=True, key= lambda x: medals[x])[:3]


#Course 2 project###################

#We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which 
# has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. We have also words that
#  express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.

#Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv 
# file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words 
# are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet.
#  At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.

#To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and 
# removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word):
    result = word[:]
    for c in punctuation_chars:
        result = result.replace(c,'')
    return result


#Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string 
# which represents one or more sentences, and calculates how many words in the string are considered positive words. 
# Use the list, positive_words to determine what words will count as positive. The function should return a positive 
# integer - how many occurrences there are of positive words in the text. Note that all of the words in positive_words 
# are lower cased, so you’ll need to convert all the words in the input string to lower case as well.


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
# list of negative words to use            
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

# takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word.
def strip_punctuation(word):
    result = word[:]
    for c in punctuation_chars:
        result = result.replace(c,'')
    return result

#calculates how many words in the string are considered positive words #returns a positive integer: how many occurrences there are of positive words in the text 
def get_pos(sentences):
    words_lst = sentences.split()
    for i, word in enumerate(words_lst):
        words_lst[i] = words_lst[i].strip()
    n_pos_words=0
    for w in words_lst:
        if strip_punctuation(w).lower() in positive_words:
            n_pos_words += 1
    return n_pos_words

#calculates how many words in the string are considered negative words #returns a positive integer: how many occurrences there are of negative words in the text 
def get_neg(sentences):
    words_lst = sentences.split()
    for i, word in enumerate(words_lst):
        words_lst[i] = words_lst[i].strip()
    n_pos_words=0
    for w in words_lst:
        if strip_punctuation(w).lower() in negative_words:
            n_pos_words += 1
    return n_pos_words

#Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake 
# generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet).
#  Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. Copy the code from
#  the code windows above, and put that in the top of this code window. Now, you will write code to create a csv file called
#  resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words
#  are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or 
# negative the text is overall) for each tweet. The file should have those headers in that order. Remember that there is 
# another component to this project. You will upload the csv file to Excel or Google Sheets and produce a graph of the Net 
# Score vs Number of Retweets


#input file and output file of the program
source_file = "project_twitter_data.csv"
dest_file = "resulting_data.csv"

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

# takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word.
def strip_punctuation(word):
    for c in punctuation_chars:
        word = word.replace(c,'')
    return word

#calculates how many words in the string are considered positive words #returns a positive integer: how many occurrences there are of positive words in the text 
def get_pos(sentences):
    words_lst = sentences.split()
    for i, word in enumerate(words_lst):
        words_lst[i] = words_lst[i].strip()
    n_pos_words=0
    for w in words_lst:
        if strip_punctuation(w).lower() in positive_words:
            n_pos_words += 1
    return n_pos_words

#calculates how many words in the string are considered negative words #returns a positive integer: how many occurrences there are of negative words in the text 
def get_neg(sentences):
    words_lst = sentences.split()
    for i, word in enumerate(words_lst):
        words_lst[i] = words_lst[i].strip()
    n_pos_words=0
    for w in words_lst:
        if strip_punctuation(w).lower() in negative_words:
            n_pos_words += 1
    return n_pos_words

#opens the file project_twitter_data.csv and creates a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet.
with open(source_file,"r") as t_fref:
    lines = t_fref.readlines()
    with open(dest_file,"w") as res_fref:
        res_fref.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
        res_fref.write("\n")
        for line in lines[1:]:
            lst=line.strip().split(",")
            pos_score = get_pos(lst[0])
            neg_score = get_neg(lst[0])
            net_score = pos_score - neg_score
            row_str = "{},{},{},{},{}".format(str(lst[1]), str(lst[2]), str(pos_score), str(neg_score), str(net_score)) 
            res_fref.write(row_str)
            res_fref.write("\n")
            


#course 3
#nested values

#The variable nested contains a nested list. Assign ‘snake’ to the variable output using 
# indexing.
nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]

output = nested[1][2]


#Given below is a list of lists of athletes. Create a list, t, that saves only the
#  athlete’s name if it contains the letter “t”. If it does not contain the letter “t”, 
# save the athlete name into list other.

athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]

t=[]
other=[]
for l1 in athletes:
    for a in l1:
        if 't' in a:
            t.append(a)
        else:
            other.append(a)

#Iterate through the contents of l_of_l and assign the third element of sublist to a new 
# list called third.

l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]

third=[]
for l1 in l_of_l:
    third.append(l1[2])

#Given the dictionary, nested_d, save the medal count for the USA from all three Olympics 
# in the dictionary to the list US_count.

nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

US_count = []

for key1 in nested_d:
    for key2 in nested_d[key1]:
        if key2 == 'USA':
            US_count.append(nested_d[key1][key2])

#Below, we have provided a nested dictionary. Index into the dictionary to create 
# variables that we have listed in the ActiveCode window.

sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
v1  = sports['swimming'][2]
# Assign the string 'platform' to the name v2
v2 = sports['diving'][1]
# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3 = sports['gymnastics']['women']
# Assign the string 'rings' to the name v4
v4 = sports['gymnastics']['men'][3]


#The variable nested_d contains a nested dictionary with the gold medal counts for the 
# top four countries in the past three Olympics. Assign the value of Great Britain’s gold 
# medal count from the London Olympics to the variable london_gold. Use indexing. Do not 
# hardcode.

nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

london_gold = nested_d['London']['Great Britain']

#Below, a list of lists is provided. Use in and not in tests to create variables with Boolean 
# values. See comments for further instructions.


lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
yellow = 'yellow' in lst[2]

#Test to see if 4 is in the second list of lst. Save to variable ``four``
four = 4 in lst[1]

#Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
orange = 'orange' in lst[0]


#Provided is a nested data structure. Follow the instructions in the comments below. 
# Do not hard code.


nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
data = False
if 'data' in nested: data = True

# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
twentyfour = False
if 24 in nested['data']: twentyfour = True

# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
whole = False
if 'whole' not in nested['window']: whole = True

# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
physics = False
if 'physics' in nested: physics = True


## map filter comprehension and zip ####

#!!!!!!!!!!!!!!!!! map filter zip doesnt return a list but a list like object (an iterator) -> do list casting!!!!!!!!!!

#Write code to assign to the variable map_testing all the elements in lst_check while adding 
# the string “Fruit: ” to the beginning of each element using mapping.

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

map_testing = list(map(lambda s: "Fruit: "+s, lst_check))

#Below, we have provided a list of strings called countries. Use filter to produce a list called 
# b_countries that only contains the strings from countries that begin with B.

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']

b_countries = list(filter(lambda word: word[0] == 'B', countries))


#Below, we have provided a list of tuples that contain the names of Game of Thrones characters. 
# Using list comprehension, create a list of strings called first_names that contains only the 
# first names of everyone in the original list.

people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]

first_names = [name for (surname, name) in people] 
first_names = [name for surname, name in people] 


#Use list comprehension to create a list called lst2 that doubles each element in the list, lst.
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

lst2 = [elem*2 for elem in lst]

#Below, we have provided a list of tuples that contain students’ names and their final grades in
#  PYTHON 101. Using list comprehension, create a new list passed that contains the names of
#  students who passed the class (had a final grade of 70 or greater).

students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]

passed = [student for student, grade in students if grade >= 70]


#Write code using zip and filter so that these lists (l1 and l2) are combined into one big list 
# and assigned to the variable opposites if they are both longer than 3 characters each.

l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']

opposites = list(filter(lambda tupl: len(tupl[0]) > 3 and len(tupl[1]) > 3 , list(zip(l1,l2)) ))


#Below, we have provided a species list and a population list. Use zip to combine these lists 
# into one list of tuples called pop_info. From this list, create a new list called endangered
#  that contains the names of species whose populations are below 2500.


species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]

pop_info = list(zip(species, population))

endangered = [name for name,pop in pop_info if pop < 2500]



#APIs####################

# module requests_with_caching ####################
import requests
import json

PERMANENT_CACHE_FNAME = "permanent_cache.txt"
TEMP_CACHE_FNAME = "this_page_cache.txt"

def _write_to_file(cache, fname):
    with open(fname, 'w') as outfile:
        outfile.write(json.dumps(cache, indent=2))

def _read_from_file(fname):
    try:
        with open(fname, 'r') as infile:
            res = infile.read()
            return json.loads(res)
    except:
        return {}

def add_to_cache(cache_file, cache_key, cache_value):
    temp_cache = _read_from_file(cache_file)
    temp_cache[cache_key] = cache_value
    _write_to_file(temp_cache, cache_file)

def clear_cache(cache_file=TEMP_CACHE_FNAME):
    _write_to_file({}, cache_file)

def make_cache_key(baseurl, params_d, private_keys=["api_key"]):
    """Makes a long string representing the query.
    Alphabetize the keys from the params dictionary so we get the same order each time.
    Omit keys with private info."""
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)

def get(baseurl, params={}, private_keys_to_ignore=["api_key"], permanent_cache_file=PERMANENT_CACHE_FNAME, temp_cache_file=TEMP_CACHE_FNAME):
    full_url = requests.requestURL(baseurl, params)
    cache_key = make_cache_key(baseurl, params, private_keys_to_ignore)
    # Load the permanent and page-specific caches from files
    permanent_cache = _read_from_file(permanent_cache_file)
    temp_cache = _read_from_file(temp_cache_file)
    if cache_key in temp_cache:
        print("found in temp_cache")
        # make a Response object containing text from the change, and the full_url that would have been fetched
        return requests.Response(temp_cache[cache_key], full_url)
    elif cache_key in permanent_cache:
        print("found in permanent_cache")
        # make a Response object containing text from the change, and the full_url that would have been fetched
        return requests.Response(permanent_cache[cache_key], full_url)
    else:
        print("new; adding to cache")
        # actually request it
        resp = requests.get(baseurl, params)
        # save it
        add_to_cache(temp_cache_file, cache_key, resp.text)
        return resp
################################################################################

# course 3 project #############
#!!!!!!!!!! warning: can be OLD queries -> outdated !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#This project will take you through the process of mashing up data from two different APIs to 
# make movie recommendations. The TasteDive API lets you provide a movie (or bands, TV shows,
#  etc.) as a query input, and returns a set of related items. The OMDB API lets you provide 
# a movie title as a query input and get back data about the movie, including scores from 
# various review sites (Rotten Tomatoes, IMDB, etc.).
#You will put those two together. You will use TasteDive to get related movies for a whole
#  list of titles. You’ll combine the resulting lists of related movies, and sort them 
# according to their Rotten Tomatoes scores (which will require making API calls to the 
# OMDB API.)
#To avoid problems with rate limits and site accessibility, we have provided a cache file
#  with results for all the queries you need to make to both OMDB and TasteDive. Just use 
# requests_with_caching.get() rather than requests.get(). If you’re having trouble, you 
# may not be formatting your queries properly, or you may not be asking for data that 
# exists in our cache. We will try to provide as much information as we can to help guide
#  you to form queries for which data exists in the cache.
#Your first task will be to fetch data from TasteDive. The documentation for the API is at
#  https://tastedive.com/read/api.

#We will use TasteDive to get related movies for a whole list of titles
parameters = {"q":"Black Panther", "type":"movies", "limit": 5}
tasteDive_res = rwc.get("https://tastedive.com/api/similar", params=parameters)

tasteDive_data = json.loads(tasteDive_res.text)

for d in tasteDive_data:
    print(d)


#The OMDB API lets you provide a movie title as a query input and get back data about the movie,
# including scores from various review sites




#We’ll combine the resulting lists of related movies, and sort them according to their Rotten 
#Tomatoes scores 


#Define a function, called get_movies_from_tastedive. It should take one input parameter, 
# a string that is the name of a movie or music artist. The function should return the 5 
# TasteDive results that are associated with that string; be sure to only get movies,
#  not other kinds of media. It will be a python dictionary with just one key, ‘Similar’.
#Try invoking your function with the input “Black Panther”.
#HINT: Be sure to include only q, type, and limit as parameters in order to extract data 
# from the cache. If any other parameters are included, then the function will not be able 
# to recognize the data that you’re attempting to pull from the cache. Remember, you will 
# not need an api key in order to complete the project, because all data will be found in
#  the cache.

import requests_with_caching as rwc
import json

#Take a movie name and returns a dictionary with with one key ‘Similar’ among 5 movies as values
def get_movies_from_tastedive(movie):
    parameters = {"q":movie, "type":"movies", "limit": 5}
    tasteDive_res = rwc.get("https://tastedive.com/api/similar", params=parameters)
    print(tasteDive_res.url)
    print(tasteDive_res.text)
    return tasteDive_res.json()



#Please copy the completed function from above into this active code window.
#  Next, you will need to write a function that extracts just the list of movie 
# titles from a dictionary returned by get_movies_from_tastedive. Call it extract
# _movie_titles.


import requests_with_caching as rwc
import json

#Take a movie name and returns a dictionary with with one key ‘Similar’ among 5 movies as values
def get_movies_from_tastedive(movie):
    parameters = {"q":movie, "type":"movies", "limit": 5}
    tasteDive_res = rwc.get("https://tastedive.com/api/similar", params=parameters)
    print(tasteDive_res.url)
    print(tasteDive_res.text)
    return tasteDive_res.json()

#extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive
def extract_movie_titles(dict):
    print(dict)
    return list([d['Name'] for d in dict["Similar"]["Results"]])




#Please copy the completed functions from the two code windows above into this
#  active code window. Next, you’ll write a function, called get_related_titles.
#  It takes a list of movie titles as input. It gets five related movies for each
#  from TasteDive, extracts the titles for all of them, and combines them all 
# into a single list. Don’t include the same movie twice.


import requests_with_caching as rwc
import json

#Take a movie name and returns a dictionary with with one key ‘Similar’ among 5 movies as values
def get_movies_from_tastedive(movie):
    parameters = {"q":movie, "type":"movies", "limit": 5}
    tasteDive_res = rwc.get("https://tastedive.com/api/similar", params=parameters)
    print(tasteDive_res.url)
    print(tasteDive_res.text)
    return tasteDive_res.json()

#extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive
def extract_movie_titles(dict):
    print(dict)
    return list([d['Name'] for d in dict["Similar"]["Results"]])

#takes a list of movie titles as input. Returns a single list with related titles
def get_related_titles(movies):
    related_lst = []
    for movie in movies:
        for title in extract_movie_titles(get_movies_from_tastedive(movie)):
            if title not in related_lst:
                related_lst.append(title)
    return related_lst





#Your next task will be to fetch data from OMDB. The documentation for the API is at
#  https://www.omdbapi.com/
#Define a function called get_movie_data. It takes in one parameter which is a string that 
# should represent the title of a movie you want to search. The function should return a 
# dictionary with information about that movie.
#Again, use requests_with_caching.get(). For the queries on movies that are already in the 
# cache, you won’t need an api key. You will need to provide the following keys: t and r. 
# As with the TasteDive cache, be sure to only include those two parameters in order to extract 
# existing data from the cache.


import requests_with_caching as rwc
import json

#takes a string that represent a title of a movie to search.Returns a dictionary with info about that movie
def get_movie_data(movie):
    parameters = {"t":movie,"r":"json"}
    omdb_res = rwc.get("http://www.omdbapi.com/",params=parameters)
    print(omdb_res.url)
    print(omdb_res.text)
    return(json.loads(omdb_res.text)) #same as: return omdb_res.json()



#Please copy the completed function from above into this active code window. Now write a function 
# called get_movie_rating. It takes an OMDB dictionary result for one movie and extracts the 
# Rotten Tomatoes rating as an integer. For example, if given the OMDB dictionary for “Black 
# Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0.

import requests_with_caching as rwc
import json

#takes a string that represent a title of a movie to search.Returns a dictionary with info about that movie
def get_movie_data(movie):
    parameters = {"t":movie,"r":"json"}
    omdb_res = rwc.get("http://www.omdbapi.com/",params=parameters)
    print(omdb_res.url)
    print(omdb_res.text)
    return(json.loads(omdb_res.text)) #same as: return omdb_res.json()

# takes the name of a movie and returns its Rotten Tomatoes rating if exists otherwise returns 0
def get_movie_rating(movie):
    try:
        for d in movie["Ratings"]:
            if d["Source"] == "Rotten Tomatoes":
                value = d["Value"].replace('%', '') 
                return int(value)
        return 0
    except:
        return 0



#Now, you’ll put it all together. Don’t forget to copy all of the functions that you have 
# previously defined into this code window. Define a function get_sorted_recommendations. 
# It takes a list of movie titles as an input. It returns a sorted list of related movie 
# titles as output, up to five related movies for each input movie title. The movies should
#  be sorted in descending order by their Rotten Tomatoes rating, as returned by the 
# get_movie_rating function. Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ 
# comes before ‘Eyyvah Eyvah’.

import requests_with_caching as rwc
import json

#Take a movie name and returns a dictionary with with one key ‘Similar’ among 5 movies as values
def get_movies_from_tastedive(movie):
    parameters = {"q":movie, "type":"movies", "limit": 5}
    tasteDive_res = rwc.get("https://tastedive.com/api/similar", params=parameters)
    print(tasteDive_res.url)
    print(tasteDive_res.text)
    return tasteDive_res.json()

#extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive
def extract_movie_titles(dict):
    print(dict)
    return list([d['Name'] for d in dict["Similar"]["Results"]])

#takes a list of movie titles as input. Returns a single list with related titles
def get_related_titles(movies):
    related_lst = []
    for movie in movies:
        for title in extract_movie_titles(get_movies_from_tastedive(movie)):
            if title not in related_lst:
                related_lst.append(title)
    return related_lst

#takes a string that represent a title of a movie to search.Returns a dictionary with info about that movie
def get_movie_data(movie):
    parameters = {"t":movie,"r":"json"}
    omdb_res = rwc.get("http://www.omdbapi.com/",params=parameters)
    print(omdb_res.url)
    print(omdb_res.text)
    return(json.loads(omdb_res.text)) #same as: return omdb_res.json()

# takes an OMDB dictionary result for one movie and returns its Rotten Tomatoes rating if exists otherwise returns 0
def get_movie_rating(movieDict):
    try:
        for d in movieDict["Ratings"]:
            if d["Source"] == "Rotten Tomatoes":
                value = d["Value"].replace('%', '') 
                return int(value)
        return 0
    except:
        return 0

#takes a list of movie titles as an input. It returns a sorted list of related movie titles as
# output. The movies are sorted in descending order by their Rotten Tomatoes rating
def get_sorted_recommendations(movies):
    related_lst = get_related_titles(movies)
    ratings_lst = []
    for rel in related_lst:
         ratings_lst.append( get_movie_rating(get_movie_data(rel)) )
    
    movies_tpls = zip(related_lst, ratings_lst)
    sorted_movies_tpls = sorted( movies_tpls, reverse=True, key= lambda tpl: (-tpl[1], tpl[0]) )
    return list([title for title,rating in sorted_movies_tpls])



####################################################################
#python classes###

#Define a class called Bike that accepts a string and a float as input, and assigns those 
# inputs respectively to two instance variables, color and price. Assign to the variable 
# testOne an instance of Bike whose color is blue and whose price is 89.99. Assign to the
#  variable testTwo an instance of Bike whose color is purple and whose price is 25.0.

class Bike():

    def __init__(self, s, f):
        self.color = s
        self.price = f

testOne = Bike("blue", 89.99)
testTwo = Bike("purple", 25.0)


#Create a class called AppleBasket whose constructor accepts two inputs: a string representing
#  a color, and a number representing a quantity of apples. The constructor should initialize 
# two instance variables: apple_color and apple_quantity. Write a class method called increase 
# that increases the quantity by 1 each time it is invoked. You should also write a __str__
#  method for this class that returns a string of the format: "A basket of [quantity goes here]
#  [color goes here] apples." e.g. "A basket of 4 red apples." or "A basket of 50 blue apples."
#  (Writing some test code that creates instances and assigns values to variables may help you 
# solve this problem!)


class AppleBasket():

    def __init__(self, s, n):
        self.apple_color = s
        self.apple_quantity = n

    def increase(self):
        self.apple_quantity += 1
    
    def __str__(self):
        return "A basket of {} {} apples.".format(self.apple_quantity, self.apple_color)


#Define a class called BankAccount that accepts the name you want associated with your bank 
# account in a string, and an integer that represents the amount of money in the account. The
#  constructor should initialize two instance variables from those inputs: name and amt. Add 
# a string method so that when you print an instance of BankAccount, you see "Your account, 
# [name goes here], has [start_amt goes here] dollars." Create an instance of this class with
#  "Bob" as the name and 100 as the amount. Save this to the variable t1.


class BankAccount():

    def __init__(self, n, a):
        self.name = n
        self.amt = a
    
    def __str__(self):
        return "Your account, {}, has {} dollars.".format(self.name, self.amt)


t1 = BankAccount("Bob",100)


##Sorting examples###


class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def sort_priority(self):
        return self.price

lst = [Fruit("Cherry", 8), Fruit("Apple", 4), Fruit("Blueberry", 16)]
#order by referencing a class method
for f in sorted(lst, key=Fruit.sort_priority()):
    print(f.name)

for f in sorted(lst, key = lambda x: x.sort_priority()):
    print(f.name)


######tamagochi example########################
import sys
sys.setExecutionLimit(60000)
from random import randrange

class Pet(object):
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']
    def __init__(self, name = "Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        # state += "Hunger %d Boredom %d Words %s" % (self.hunger, self.boredom, self.sounds)
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.update_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.update_boredom()

    def feed(self):
        self.update_hunger()

    def update_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def update_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)

class Cat(Pet):
    sounds = ['Meow']

    def mood(self):
        if self.hunger > self.hunger_threshold:
            return "hungry"
        if self.boredom <2:
            return "grumpy; leave me alone"
        elif self.boredom > self.boredom_threshold:
            return "bored"
        elif randrange(2) == 0:
            return "randomly annoyed"
        else:
            return "happy"

class Dog(Pet):
    sounds = ['Woof', 'Ruff']

    def mood(self):
        if (self.hunger > self.hunger_threshold) and (self.boredom > self.boredom_threshold):
            return "bored and hungry"
        else:
            return "happy"

    def feed(self):
        Pet.feed(self)
        print("Arf! Thanks!")

class Bird(Pet):
    sounds = ["chirp"]
    def __init__(self, name="Kitty", chirp_number=2):
        Pet.__init__(self, name) # call the parent class's constructor
        # basically, call the SUPER -- the parent version -- of the constructor, with all the parameters that it needs.
        self.chirp_number = chirp_number # now, also assign the new instance variable

    def hi(self):
        for i in range(self.chirp_number):
            print(self.sounds[randrange(len(self.sounds))])
        self.update_boredom()

class Lab(Dog):
    def fetch(self):
        return "I found the tennis ball!"

    def hi(self):
        print(self.fetch())
        print(self.sounds[randrange(len(self.sounds))])

class Poodle(Dog):
    def dance(self):
        return "Dancin' in circles like poodles do."

    def hi(self):
        print(self.dance())
        Dog.hi(self)

def whichone(petlist, name):
    for pet in petlist:
        if pet.name == name:
            return pet
    return None # no pet matched

pet_types = {'dog': Dog, 'lab': Lab, 'poodle': Poodle, 'cat': Cat, 'bird': Bird}
def whichtype(adopt_type="general pet"):
    return pet_types.get(adopt_type.lower(), Pet)

def play():
    animals = []

    option = ""
    base_prompt = """
        Quit
        Adopt <petname_with_no_spaces> <pet_type - choose dog, cat, lab, poodle, bird, or another unknown pet type>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice: """
    feedback = ""
    while True:
        action = input(feedback + "\n" + base_prompt)
        feedback = ""
        words = action.split()
        if len(words) > 0:
            command = words[0]
        else:
            command = None
        if command == "Quit":
            print("Exiting...")
            return
        elif command == "Adopt" and len(words) > 1:
            if whichone(animals, words[1]):
                feedback += "You already have a pet with that name\n"
            else:
                # figure out which class it should be
                if len(words) > 2:
                    Cl = whichtype(words[2])
                else:
                    Cl = Pet
                # Make an instance of that class and append it
                animals.append(Cl(words[1]))
        elif command == "Greet" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again.\n"
                print()
            else:
                pet.hi()
        elif command == "Teach" and len(words) > 2:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.teach(words[2])
        elif command == "Feed" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.feed()
        else:
            feedback+= "I didn't understand that. Please try again."

        for pet in animals:
            pet.clock_tick()
            feedback += "\n" + pet.__str__()

play()

###################
#The class, Pokemon, is provided below and describes a Pokemon and its leveling and evolving 
# characteristics. An instance of the class is one pokemon that you create.
#Grass_Pokemon is a subclass that inherits from Pokemon but changes some aspects, 
# for instance, the boost values are different.
#For the subclass Grass_Pokemon, add another method called action that returns the string 
# "[name of pokemon] knows a lot of different moves!". Create an instance of this class 
# with the name as "Belle". Assign this instance to the variable p1.

class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level = 5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

    def action(self):
        return "{} knows a lot of different moves!".format(self.name)

p1 = Grass_Pokemon("Belle")



#Modify the Grass_Pokemon subclass so that the attack strength for Grass_Pokemon instances does
#  not change until they reach level 10. At level 10 and up, their attack strength should 
# increase by the attack_boost amount when they are trained.
#To test, create an instance of the class with the name as "Bulby". Assign the instance to 
# the variable p2. Create another instance of the Grass_Pokemon class with the name set 
# to "Pika" and assign that instance to the variable p3. Then, use Grass_Pokemon methods 
# to train the p3 Grass_Pokemon instance until it reaches at least level 10.

class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level = 5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"

    def attack_up(self):
        if(self.level >= 9):
            Pokemon.attack_up(self)
            

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]


p2 = Grass_Pokemon("Bulby")
p3 = Grass_Pokemon("Pika")


#Along with the Pokemon parent class, we have also provided several subclasses. Write another
# method in the parent class that will be inherited by the subclasses. Call it opponent. 
# It should return which type of pokemon the current type is weak and strong against, as a 
# tuple.
#Grass is weak against Fire and strong against Water
#Ghost is weak against Dark and strong against Psychic
#Fire is weak against Water and strong against Grass
#Flying is weak against Electric and strong against Fighting
#For example, if the p_type of the subclass is 'Grass', .opponent() should return the tuple
#  ('Fire', 'Water')

class Pokemon():
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name,level = 5):
        self.name = name
        self.level = level
        self.weak = "Normal"
        self.strong = "Normal"

    def opponent(self):
        if self.p_type == "Grass":
            return "Fire", "Water"
        elif self.p_type == "Ghost":
            return "Dark", "Psychic"
        elif self.p_type == "Fire":
            return "Water", "Grass"
        elif self.p_type == "Flying":
            return "Electric", "Fighting"
        else:
            return none

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

class Ghost_Pokemon(Pokemon):
    p_type = "Ghost"

    def update(self):
        self.health_boost = 3
        self.attack_boost = 4
        self.defense_boost = 3

class Fire_Pokemon(Pokemon):
    p_type = "Fire"

class Flying_Pokemon(Pokemon):
    p_type = "Flying"

#### Unit Testing ###########
#!!!!!!!!!!!!! 'import test': Module test not available outside the runestone environment !!!!!!!
#The function mySum is supposed to return the sum of a list of numbers (and 0 if that list 
# is empty), but it has one or more errors in it. Use this space to write test cases to 
# determine what errors there are. You will be using this information to answer the next 
# set of multiple choice questions.

l=[]
assert mySum(l)==0, 'Error in mySum(): it should have returned 0'
l=[2]
assert mySum(l)==2, 'Error in mySum(): it should have returned 2'
l=[2,5]
assert mySum(l)==7, 'Error in mySum(): it should have returned 7'

#or
import test
l=[]
test.testEqual(mySum(l)==0)
l=[2]
test.testEqual(mySum(l)==2)
l=[2,5]
test.testEqual(mySum(l)==7)

#or
try:
    l=[]
    assert mySum(l)==0
except:
    print('Error in mySum(): it should have returned 0')
try:
    l=[2]
    assert mySum(l)==2
except:
    print('Error in mySum(): it should have returned 2')
try:    
    l=[2,5]
    assert mySum(l)==7
except:
    print('Error in mySum(): it should have returned 7') 



#--The class Student is supposed to accept two arguments in its constructor:----------
#>>  A name string

#>>  An optional integer representing the number of years the student has been at
#    Michigan (default:1)

#--Every student has three instance variables:--------------------------------------
#>>  self.name (set to the name provided)

#>>  self.years_UM (set to the number of years the student has been at Michigan)

#>> .self.knowledge (initialized to 0)

#--There are three methods:---------------------------------------------------------
#>>  .study() should increase self.knowledge by 1 and return None

#>> .getKnowledge() should return the value of self.knowledge

#>> .year_at_umich() should return the value of self.years_UM

#There are one or more errors in the class. Use this space to write test cases 
# to determine what errors there are. You will be using this information to answer the next set of multiple choice questions.

import test

s = Student("Albert")
test.testEqual(s.name,"Albert")
test.testEqual(s.years_UM,1)
test.testEqual(s.knowledge, 0)

s = Student("Albert", 4)
test.testEqual(s.name,"Albert")
test.testEqual(s.years_UM,4)
test.testEqual(s.knowledge,0)

s = Student("Albert", 4)
test.testEqual(s.study(), None)
test.testEqual(s.knowledge, 1)
test.testEqual(s.getKnowledge(), 1)
test.testEqual(s.year_at_umich(),4)

###Exceptions ###

#The code below takes the list of country, country, and searches to see if it is in the
#  dictionary gold which shows some countries who won gold during the Olympics. However,
#  this code currently does not work. Correctly add try/except clause in the code so that
#  it will correctly populate the list, country_gold, with either the number of golds won
#  or the string “Did not get gold”.

gold = {"US":46, "Fiji":1, "Great Britain":27, "Cuba":5, "Thailand":2, "China":26, "France":10}
country = ["Fiji", "Chile", "Mexico", "France", "Norway", "US"]
country_gold = []

for x in country:
    try:
        country_gold.append(gold[x])
    except:
        country_gold.append("Did not get gold")



#Provided is a buggy for loop that tries to accumulate some values out of some dictionaries. 
# Insert a try/except so that the code passes.

di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}, {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}, {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}, {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]
total = 0
for diction in di:
    try:
        total = total + diction['Puppies']
    except Exception as e:
        print(e)
        
print("Total number of puppies:", total)



#The list, numb, contains integers. Write code that populates the list remainder with the 
# remainder of 36 divided by each number in numb. For example, the first element should be
#  0, because 36/6 has no remainder. If there is an error, have the string “Error” appear 
# in the remainder.

numb = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]

remainder = []

import sys
for n in numb:
    try:
        remainder.append(int(36%n))
    except:
        remainder.append('Error')




##Provided is buggy code, insert a try/except so that the code passes.

lst = [2,4,10,42,12,0,4,7,21,4,83,8,5,6,8,234,5,6,523,42,34,0,234,1,435,465,56,7,3,43,23]

lst_three = []

for num in lst:
    try:
        if 3 % num == 0:
            lst_three.append(num)
    except Exception as e:
        print(e)



#Write code so that the buggy code provided works using a try/except. When the codes does 
# not work in the try, have it append to the list attempt the string “Error”.

full_lst = ["ab", 'cde', 'fgh', 'i', 'jkml', 'nop', 'qr', 's', 'tv', 'wxy', 'z']

attempt = []

for elem in full_lst:
    try:
        attempt.append(elem[1])
    except:
        attempt.append('Error')





#The following code tries to append the third element of each list in conts to the new 
# list third_countries. Currently, the code does not work. Add a try/except clause so 
# the code runs without errors, and the string ‘Continent does not have 3 countries’ is
#  appended to countries instead of producing an error.

conts = [['Spain', 'France', 'Greece', 'Portugal', 'Romania', 'Germany'], ['USA', 'Mexico', 'Canada'], ['Japan', 'China', 'Korea', 'Vietnam', 'Cambodia'], ['Argentina', 'Chile', 'Brazil', 'Ecuador', 'Uruguay', 'Venezuela'], ['Australia'], ['Zimbabwe', 'Morocco', 'Kenya', 'Ethiopa', 'South Africa'], ['Antarctica']]

third_countries = []

for c in conts:
    try:
        third_countries.append(c[2])
    except:
        third_countries.append('Continent does not have 3 countries')




#The buggy code below prints out the value of the sport in the list sport. Use try/except
#  so that the code will run properly. If the sport is not in the dictionary, ppl_play, 
# add it in with the value of 1.

sport = ["hockey", "basketball", "soccer", "tennis", "football", "baseball"]

ppl_play = {"hockey":4, "soccer": 10, "football": 15, "tennis": 8}

for x in sport:
    try:
        print(ppl_play[x])
    except:
        ppl_play[x]=1





#Provided is a buggy for loop that tries to accumulate some values out of some dictionaries.
#  Insert a try/except so that the code passes. If the key is not there, initialize it in 
# the dictionary and set the value to zero.

di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}, {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}, {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}, {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]
total = 0
for diction in di:
    try:
        total = total + diction['Puppies']
    except:
        diction['Puppies'] = 0


print("Total number of puppies:", total)



## final assesment: Wheel of Fortune ##################################

#This project will take you through the process of implementing a simplified version of the game Wheel of Fortune. Here are the rules of our game:

#● There are num_human human players and num_computer computer players.
#○ Every player has some amount of money ($0 at the start of the game)

#○ Every player has a set of prizes (none at the start of the game)

#● The goal is to guess a phrase within a category. For example:
#○ Category: Artist & Song

#○ Phrase: Whitney Houston’s I Will Always Love You

#● Players see the category and an obscured version of the phrase where every alphanumeric character in the phrase starts out as hidden (using underscores: _):
#○ Category: Artist & Song

#○ Phrase: _______ _______'_ _ ____ ______ ____ ___

#Note that case (capitalization) does not matter

#● During their turn, every player spins the wheel to determine a prize amount and:
#If the wheel lands on a cash square, players may do one of three actions:
#○ Guess any letter that hasn’t been guessed by typing a letter (a-z)
#Vowels (a, e, i, o, u) cost $250 to guess and can’t be guessed if the player doesn’t have enough money. All other letters are “free” to guess

# The player can guess any letter that hasn’t been guessed and gets that cash amount for every time that letter appears in the phrase

# If there is a prize, the user also gets that prize (in addition to any prizes they already had)

# If the letter does appear in the phrase, the user keeps their turn. Otherwise, it’s the next player’s turn

#Example: The user lands on $500 and guesses ‘W’
#There are three W’s in the phrase, so the player wins $1500

#○ Guess the complete phrase by typing a phrase (anything over one character that isn’t ‘pass’)
#If they are correct, they win the game

#If they are incorrect, it is the next player’s turn

#○ Pass their turn by entering 'pass'
#
#If the wheel lands on “lose a turn”, the player loses their turn and the game moves on to the next player
#
#If the wheel lands on “bankrupt”, the player loses their turn and loses their money but they keep all of the prizes they have won so far.
#
#● The game continues until the entire phrase is revealed (or one player guesses the complete phrase)

#—

#First, let’s learn about a few functions and methods that we’ll use along the way to do this project. There are no questions to answer in the next four active code windows. They are just here to introduce you to some functions and methods that you may not be aware of. The active code window that starts with “Part A” is where you are first asked to complete code.

#—

#The time.sleep(s) function (from the time module) delays execution of the next line of code for s seconds. You’ll find that we can build a little suspense during gameplay with some well-placed delays. The game can also be easier for users to understand if not everything happens instantly.

'''
import time

for x in range(2, 6):
    print('Sleep {} seconds..'.format(x))
    time.sleep(x) # "Sleep" for x seconds
print('Done!')
'''


#The random module includes several useful methods for generating and using random numbers,
#including:
#random.randint(min, max) generates a random number between min and max (inclusive)
#random.choice(L) selects a random item from the list L
'''
import random

rand_number = random.randint(1, 10)
print('Random number between 1 and 10: {}'.format(rand_number))

letters = [letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
rand_letter = random.choice(letters)
print('Random letter: {}'.format(rand_letter))
'''

#There are also several string methods that we haven’t gone over in detail but will use for 
#this project:
#.upper() converts a string to uppercase (the opposite is .lower())
#.count(s) counts how many times the string s occurs inside of a larger string
'''
myString = 'Hello, World! 123'

print(myString.upper()) # HELLO, WORLD! 123
print(myString.lower()) # hello, world! 123
print(myString.count('l')) # 3

s = 'python is pythonic'
print(s.count('python')) # 2
'''

#We’re going to define a few useful methods for you:

#● getNumberBetween(prompt, min, max)) repeatedly asks the user for a number between min and max with the prompt prompt

#● spinWheel() simulates spinning the wheel and returns a dictionary with a random prize

#● getRandomCategoryAndPhrase() returns a tuple with a random category and phrase for players to guess

#● obscurePhrase(phrase, guessed) returns a tuple with a random category and phrase for players to guess

import json
import random
import time

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Repeatedly asks the user for a number between min & max (inclusive)
def getNumberBetween(prompt, min, max):
    userinp = input(prompt) # ask the first time

    while True:
        try:
            n = int(userinp) # try casting to an integer
            if n < min:
                errmessage = 'Must be at least {}'.format(min)
            elif n > max:
                errmessage = 'Must be at most {}'.format(max)
            else:
                return n
        except ValueError: # The user didn't enter a number
            errmessage = '{} is not a number.'.format(userinp)

        # If we haven't gotten a number yet, add the error message
        # and ask again
        userinp = input('{}\n{}'.format(errmessage, prompt))

# Spins the wheel of fortune wheel to give a random prize
# Examples:
#    { "type": "cash", "text": "$950", "value": 950, "prize": "A trip to Ann Arbor!" },
#    { "type": "bankrupt", "text": "Bankrupt", "prize": false },
#    { "type": "loseturn", "text": "Lose a turn", "prize": false }
def spinWheel():
    with open("wheel.json", 'r') as f:
        wheel = json.loads(f.read())
        return random.choice(wheel)

# Returns a category & phrase (as a tuple) to guess
# Example:
#     ("Artist & Song", "Whitney Houston's I Will Always Love You")
def getRandomCategoryAndPhrase():
    with open("phrases.json", 'r') as f:
        phrases = json.loads(f.read())

        category = random.choice(list(phrases.keys()))
        phrase   = random.choice(phrases[category])
        return (category, phrase.upper())

# Given a phrase and a list of guessed letters, returns an obscured version
# Example:
#     guessed: ['L', 'B', 'E', 'R', 'N', 'P', 'K', 'X', 'Z']
#     phrase:  "GLACIER NATIONAL PARK"
#     returns> "_L___ER N____N_L P_RK"
def obscurePhrase(phrase, guessed):
    rv = ''
    for s in phrase:
        if (s in LETTERS) and (s not in guessed):
            rv = rv+'_'
        else:
            rv = rv+s
    return rv

# Returns a string representing the current state of the game
def showBoard(category, obscuredPhrase, guessed):
    return """
Category: {}
Phrase:   {}
Guessed:  {}""".format(category, obscuredPhrase, ', '.join(sorted(guessed)))



category, phrase = getRandomCategoryAndPhrase()

guessed = []
for x in range(random.randint(10, 20)):
    randomLetter = random.choice(LETTERS)
    if randomLetter not in guessed:
        guessed.append(randomLetter)

print("getRandomCategoryAndPhrase()\n -> ('{}', '{}')".format(category, phrase))

print("\n{}\n".format("-"*5))

print("obscurePhrase('{}', [{}])\n -> {}".format(phrase, ', '.join(["'{}'".format(c) for c in guessed]), obscurePhrase(phrase, guessed)))

print("\n{}\n".format("-"*5))

obscured_phrase = obscurePhrase(phrase, guessed)
print("showBoard('{}', '{}', [{}])\n -> {}".format(phrase, obscured_phrase, ','.join(["'{}'".format(c) for c in guessed]), showBoard(phrase, obscured_phrase, guessed)))

print("\n{}\n".format("-"*5))

num_times_to_spin = random.randint(2, 5)
print('Spinning the wheel {} times (normally this would just be done once per turn)'.format(num_times_to_spin))

for x in range(num_times_to_spin):
    print("\n{}\n".format("-"*2))
    print("spinWheel()")
    print(spinWheel())


print("\n{}\n".format("-"*5))

print("In 2 seconds, will run getNumberBetween('Testing getNumberBetween(). Enter a number between 1 and 10', 1, 10)")

time.sleep(2)

print(getNumberBetween('Testing getNumberBetween(). Enter a number between 1 and 10', 1, 10))


##########
'''
Part A: WOFPlayer

We’re going to start by defining a class to represent a Wheel of Fortune player, called WOFPlayer. Every instance of WOFPlayer has three instance variables:

.name: The name of the player (should be passed into the constructor)

.prizeMoney: The amount of prize money for this player (an integer, initialized to 0)

.prizes: The prizes this player has won so far (a list, initialized to [])

Of these instance variables, only name should be passed into the constructor.

It should also have the following methods (note: we will exclude self in our descriptions):

.addMoney(amt): Add amt to self.prizeMoney

.goBankrupt(): Set self.prizeMoney to 0

.addPrize(prize): Append prize to self.prizes

.__str__(): Returns the player’s name and prize money in the following format:
Steve ($1800) (for a player with instance variables .name == 'Steve' and prizeMoney == 1800)

Part B: WOFHumanPlayer

Next, we’re going to define a class named WOFHumanPlayer, which should inherit from WOFPlayer (part A). This class is going to represent a human player. In addition to having all of the instance variables and methods that WOFPlayer has, WOFHumanPlayer should have an additional method:

.getMove(category, obscuredPhrase, guessed): Should ask the user to enter a move (using input()) and return whatever string they entered.

.getMove()’s prompt should be:

{name} has ${prizeMoney}

Category: {category}
Phrase:  {obscured_phrase}
Guessed: {guessed}

Guess a letter, phrase, or type 'exit' or 'pass':
For example:

Steve has $200

Category: Places
Phrase: _L___ER N____N_L P_RK
Guessed: B, E, K, L, N, P, R, X, Z

Guess a letter, phrase, or type 'exit' or 'pass':
The user can then enter:

'exit' to exit the game

'pass' to skip their turn

a single character to guess that letter

a complete phrase (a multi-character phrase other than 'exit' or 'pass') to guess that phrase

Note that .getMove() does not need to enforce anything about the user’s input; that will be done via the game logic that we define in the next ActiveCode window.

Part C: WOFComputerPlayer

Finally, we’re going to define a class named WOFComputerPlayer, which should inherit from WOFPlayer (part A). This class is going to represent a computer player.

Every computer player will have a difficulty instance variable. Players with a higher difficulty generally play “better”. There are many ways to implement this. We’ll do the following:

If there aren’t any possible letters to choose (for example: if the last character is a vowel but this player doesn’t have enough to guess a vowel), we’ll 'pass'

Otherwise, semi-randomly decide whether to make a “good” move or a “bad” move on a given turn (a higher difficulty should make it more likely for the player to make a “good” move)
To make a “bad” move, we’ll randomly decide on a possible letter.

To make a “good” move, we’ll choose a letter according to their overall frequency in the English language.

In addition to having all of the instance variables and methods that WOFPlayer has, WOFComputerPlayer should have:

Class variable

.SORTED_FREQUENCIES: Should be set to 'ZQXJKVBPYGFWMUCLDRHSNIOATE', which is a list of English characters sorted from least frequent ('Z') to most frequent ('E'). We’ll use this when trying to make a “good” move.

Additional Instance variable

.difficulty: The level of difficulty for this computer (should be passed as the second argument into the constructor after .name)

Methods

.smartCoinFlip(): This method will help us decide semi-randomly whether to make a “good” or “bad” move. A higher difficulty should make us more likely to make a “good” move. Implement this by choosing a random number between 1 and 10 using random.randint(1, 10) (see above) and returning True if that random number is greater than self.difficulty. If the random number is less than or equal to self.difficulty, return False.

.getPossibleLetters(guessed): This method should return a list of letters that can be guessed.
These should be characters that are in LETTERS ('ABCDEFGHIJKLMNOPQRSTUVWXYZ') but not in the guessed parameter.

Additionally, if this player doesn’t have enough prize money to guess a vowel (variable VOWEL_COST set to 250), then vowels (variable VOWELS set to 'AEIOU') should not be included

.getMove(category, obscuredPhrase, guessed): Should return a valid move.
Use the .getPossibleLetters(guessed) method described above.

If there aren’t any letters that can be guessed (this can happen if the only letters left to guess are vowels and the player doesn’t have enough for vowels), return 'pass'

Use the .smartCoinFlip() method to decide whether to make a “good” or a “bad” move
If making a “good” move (.smartCoinFlip() returns True), then return the most frequent (highest index in .SORTED_FREQUENCIES) possible character

If making a “bad” move (.smartCoinFlip() returns False), then return a random character from the set of possible characters (use random.choice())
'''

class WOFPlayer:
    
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
    
    def addMoney(self, amt):
        self.prizeMoney += amt

    def goBankrupt(self):
        self.prizeMoney = 0
    
    def addPrize(self, prize):
        self.prizes.append(prize)

    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)

class WOFHumanPlayer(WOFPlayer):

    def getMove(self, category, obscured_phrase, guessed):
        prompt ="""
                {} has ${}

                Category: {}
                Phrase:   {}
                Guessed:  {}

                Guess a letter, phrase, or type 'exit' or 'pass':
                """.format(self.name, self.prizeMoney, category, obscured_phrase,', '.join(sorted(guessed)))
        
        userinp = input(prompt)
        return userinp
    
class WOFComputerPlayer(WOFPlayer):
    
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, difficulty):
        WOFPlayer.__init__(self, name)
        self.difficulty = difficulty

    # Helps to decide whether to make a “good” or “bad” move. Returns True if that random number is greater than self.difficulty
    def smartCoinFlip(self):
        num = random.randint(1,10) #number between 1 and 10
        return num > self.difficulty

    # returns a list of letters that can be guessed
    def getPossibleLetters(self, guessed):
        lst=[]
        for l in LETTERS:
            if l not in guessed:
                if l in VOWELS:
                    if self.prizeMoney > 250:
                        lst.append(l)
                else:
                    lst.append(l)
        return lst

    #returns a valid move (a letter or 'pass')
    def getMove(self, category, obscured_phrase, guessed):
        letters = self.getPossibleLetters(guessed)
        if len(letters) == 0:
            return 'pass'
        else:
            good_move = self.smartCoinFlip()
            if good_move == True:
                for l in self.SORTED_FREQUENCIES:
                    if l in letters:
                        return l
            else:
                return random.choice(letters)








'''
Putting it together: Wheel of Python

Below is the game logic for the rest of the “Wheel of Python” game. We have implemented most of the game logic. Start by carefully reading this code and double checking that it all makes sense. Then, paste your code from the previous code window in the correct places below.

Note 1: we added the following code to ensure that the Python interpreter gives our game time to run:

import sys
sys.setExecutionLimit(600000)
sys.setExecutionLimit(ms) says that we should be able to run our program for ms milliseconds before it gets stopped automatically.

Note 2: As you play, you will need to keep scrolling down to follow the game.
'''

# PASTE YOUR WOFPlayer CLASS (from part A) HERE
class WOFPlayer:
    
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
    
    def addMoney(self, amt):
        self.prizeMoney += amt

    def goBankrupt(self):
        self.prizeMoney = 0
    
    def addPrize(self, prize):
        self.prizes.append(prize)

    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)
# PASTE YOUR WOFHumanPlayer CLASS (from part B) HERE
class WOFHumanPlayer(WOFPlayer):

    def getMove(self, category, obscured_phrase, guessed):
        prompt ="""
                {} has ${}

                Category: {}
                Phrase:   {}
                Guessed:  {}

                Guess a letter, phrase, or type 'exit' or 'pass':
                """.format(self.name, self.prizeMoney, category, obscured_phrase,', '.join(sorted(guessed)))
        
        userinp = input(prompt)
        return userinp
# PASTE YOUR WOFComputerPlayer CLASS (from part C) HERE
class WOFComputerPlayer(WOFPlayer):
    
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, difficulty):
        WOFPlayer.__init__(self, name)
        self.difficulty = difficulty

    # Helps to decide whether to make a “good” or “bad” move. Returns True if that random number is greater than self.difficulty
    def smartCoinFlip(self):
        num = random.randint(1,10) #number between 1 and 10
        return num > self.difficulty

    # returns a list of letters that can be guessed
    def getPossibleLetters(self, guessed):
        lst=[]
        for l in LETTERS:
            if l not in guessed:
                if l in VOWELS:
                    if self.prizeMoney > 250:
                        lst.append(l)
                else:
                    lst.append(l)
        return lst

    #returns a valid move (a letter or 'pass')
    def getMove(self, category, obscured_phrase, guessed):
        letters = self.getPossibleLetters(guessed)
        if len(letters) == 0:
            return 'pass'
        else:
            good_move = self.smartCoinFlip()
            if good_move == True:
                for l in self.SORTED_FREQUENCIES:
                    if l in letters:
                        return l
            else:
                return random.choice(letters)

import sys
sys.setExecutionLimit(600000) # let this take up to 10 minutes

import json
import random
import time

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS  = 'AEIOU'
VOWEL_COST  = 250

# Repeatedly asks the user for a number between min & max (inclusive)
def getNumberBetween(prompt, min, max):
    userinp = input(prompt) # ask the first time

    while True:
        try:
            n = int(userinp) # try casting to an integer
            if n < min:
                errmessage = 'Must be at least {}'.format(min)
            elif n > max:
                errmessage = 'Must be at most {}'.format(max)
            else:
                return n
        except ValueError: # The user didn't enter a number
            errmessage = '{} is not a number.'.format(userinp)

        # If we haven't gotten a number yet, add the error message
        # and ask again
        userinp = input('{}\n{}'.format(errmessage, prompt))

# Spins the wheel of fortune wheel to give a random prize
# Examples:
#    { "type": "cash", "text": "$950", "value": 950, "prize": "A trip to Ann Arbor!" },
#    { "type": "bankrupt", "text": "Bankrupt", "prize": false },
#    { "type": "loseturn", "text": "Lose a turn", "prize": false }
def spinWheel():
    with open("wheel.json", 'r') as f:
        wheel = json.loads(f.read())
        return random.choice(wheel)

# Returns a category & phrase (as a tuple) to guess
# Example:
#     ("Artist & Song", "Whitney Houston's I Will Always Love You")
def getRandomCategoryAndPhrase():
    with open("phrases.json", 'r') as f:
        phrases = json.loads(f.read())

        category = random.choice(list(phrases.keys()))
        phrase   = random.choice(phrases[category])
        return (category, phrase.upper())

# Given a phrase and a list of guessed letters, returns an obscured version
# Example:
#     guessed: ['L', 'B', 'E', 'R', 'N', 'P', 'K', 'X', 'Z']
#     phrase:  "GLACIER NATIONAL PARK"
#     returns> "_L___ER N____N_L P_RK"
def obscurePhrase(phrase, guessed):
    rv = ''
    for s in phrase:
        if (s in LETTERS) and (s not in guessed):
            rv = rv+'_'
        else:
            rv = rv+s
    return rv

# Returns a string representing the current state of the game
def showBoard(category, obscuredPhrase, guessed):
    return """
Category: {}
Phrase:   {}
Guessed:  {}""".format(category, obscuredPhrase, ', '.join(sorted(guessed)))

# GAME LOGIC CODE
print('='*15)
print('WHEEL OF PYTHON')
print('='*15)
print('')

num_human = getNumberBetween('How many human players?', 0, 10)

# Create the human player instances
human_players = [WOFHumanPlayer(input('Enter the name for human player #{}'.format(i+1))) for i in range(num_human)]

num_computer = getNumberBetween('How many computer players?', 0, 10)

# If there are computer players, ask how difficult they should be
if num_computer >= 1:
    difficulty = getNumberBetween('What difficulty for the computers? (1-10)', 1, 10)

# Create the computer player instances
computer_players = [WOFComputerPlayer('Computer {}'.format(i+1), difficulty) for i in range(num_computer)]

players = human_players + computer_players

# No players, no game :(
if len(players) == 0:
    print('We need players to play!')
    raise Exception('Not enough players')

# category and phrase are strings.
category, phrase = getRandomCategoryAndPhrase()
# guessed is a list of the letters that have been guessed
guessed = []

# playerIndex keeps track of the index (0 to len(players)-1) of the player whose turn it is
playerIndex = 0

# will be set to the player instance when/if someone wins
winner = False

def requestPlayerMove(player, category, guessed):
    while True: # we're going to keep asking the player for a move until they give a valid one
        time.sleep(0.1) # added so that any feedback is printed out before the next prompt

        move = player.getMove(category, obscurePhrase(phrase, guessed), guessed)
        move = move.upper() # convert whatever the player entered to UPPERCASE
        if move == 'EXIT' or move == 'PASS':
            return move
        elif len(move) == 1: # they guessed a character
            if move not in LETTERS: # the user entered an invalid letter (such as @, #, or $)
                print('Guesses should be letters. Try again.')
                continue
            elif move in guessed: # this letter has already been guessed
                print('{} has already been guessed. Try again.'.format(move))
                continue
            elif move in VOWELS and player.prizeMoney < VOWEL_COST: # if it's a vowel, we need to be sure the player has enough
                    print('Need ${} to guess a vowel. Try again.'.format(VOWEL_COST))
                    continue
            else:
                return move
        else: # they guessed the phrase
            return move


while True:
    player = players[playerIndex]
    wheelPrize = spinWheel()

    print('')
    print('-'*15)
    print(showBoard(category, obscurePhrase(phrase, guessed), guessed))
    print('')
    print('{} spins...'.format(player.name))
    time.sleep(2) # pause for dramatic effect!
    print('{}!'.format(wheelPrize['text']))
    time.sleep(1) # pause again for more dramatic effect!

    if wheelPrize['type'] == 'bankrupt':
        player.goBankrupt()
    elif wheelPrize['type'] == 'loseturn':
        pass # do nothing; just move on to the next player
    elif wheelPrize['type'] == 'cash':
        move = requestPlayerMove(player, category, guessed)
        if move == 'EXIT': # leave the game
            print('Until next time!')
            break
        elif move == 'PASS': # will just move on to next player
            print('{} passes'.format(player.name))
        elif len(move) == 1: # they guessed a letter
            guessed.append(move)

            print('{} guesses "{}"'.format(player.name, move))

            if move in VOWELS:
                player.prizeMoney -= VOWEL_COST

            count = phrase.count(move) # returns an integer with how many times this letter appears
            if count > 0:
                if count == 1:
                    print("There is one {}".format(move))
                else:
                    print("There are {} {}'s".format(count, move))

                # Give them the money and the prizes
                player.addMoney(count * wheelPrize['value'])
                if wheelPrize['prize']:
                    player.addPrize(wheelPrize['prize'])

                # all of the letters have been guessed
                if obscurePhrase(phrase, guessed) == phrase:
                    winner = player
                    break

                continue # this player gets to go again

            elif count == 0:
                print("There is no {}".format(move))
        else: # they guessed the whole phrase
            if move == phrase: # they guessed the full phrase correctly
                winner = player

                # Give them the money and the prizes
                player.addMoney(wheelPrize['value'])
                if wheelPrize['prize']:
                    player.addPrize(wheelPrize['prize'])

                break
            else:
                print('{} was not the phrase'.format(move))

    # Move on to the next player (or go back to player[0] if we reached the end)
    playerIndex = (playerIndex + 1) % len(players)

if winner:
    # In your head, you should hear this as being announced by a game show host
    print('{} wins! The phrase was {}'.format(winner.name, phrase))
    print('{} won ${}'.format(winner.name, winner.prizeMoney))
    if len(winner.prizes) > 0:
        print('{} also won:'.format(winner.name))
        for prize in winner.prizes:
            print('    - {}'.format(prize))
else:
    print('Nobody won. The phrase was {}'.format(phrase))


####################################################################################
## assignment 1 on jupyter notebook ################################################
import PIL
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageDraw, ImageFont

#### functions ####
# returns a rgba image with a channel value multiplied by a ratio
def getfiltered(img, channel, ratio):
    rgba = img.split()
    rgba_lst = list(rgba)
    rgba_lst[channel] = rgba[channel].point(lambda ch: ch*ratio)
    rgba_mod = tuple(rgba_lst)
    return Image.merge('RGBA',rgba_mod)

#r, g, b, a = image.split()
#r = r.point(lambda blue: blue*0.1)
#image1 = Image.merge('RGBA',(r,g,b,a))
#display(image1)

# draw text rectangle
def applyText(img, text):
    text_size= 50
    textBackground = Image.new('RGBA', img.size, (0,0,0,0))
    textFont = ImageFont.truetype("readonly/fanwood-webfont.ttf",text_size)
    imgDrawer = ImageDraw.Draw(textBackground)
    imgDrawer.rectangle([0, img.size[1]-text_size, img.size[0], img.size[1]], fill=(0,0,0))
    imgDrawer.text((4,img.size[1]-text_size), text, font=textFont, fill=(255,255,255))
    return Image.alpha_composite(img, textBackground)


#### main ####
# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGBA')

# build a list of 9 images which have different rgb values
images=[]
for channel in range(0,3):
    images.append(getfiltered(applyText(image, "channel {} intensity 0.1".format(channel)), channel, 0.1))
    images.append(getfiltered(applyText(image, "channel {} intensity 0.5".format(channel)), channel, 0.5))
    images.append(getfiltered(applyText(image, "channel {} intensity 0.9".format(channel)), channel, 0.9))
    
# create a contact sheet from different rgb values
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x, y = (0,0)

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y))
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)
##############################################################################################################
### final project: Pillow, OpenCV, and Pytesseract ###
# Take a ZIP file) of images and process them, using a library built into python that you need to learn how to use. A ZIP file takes several 
# different files and compresses them, thus saving space, into one single file. The files in the ZIP file we provide are newspaper images (like 
# you saw in week 3). Your task is to write python code which allows one to search through the images looking for the occurrences of keywords 
# and faces. E.g. if you search for "pizza" it will return a contact sheet of all of the faces which were located on the newspaper page which 
# mentions "pizza". This will test your ability to learn a new (library), your ability to use OpenCV to detect faces, your ability to use 
# tesseract to do optical character recognition, and your ability to use PIL to composite images together into contact sheets.


from zipfile import ZipFile 
from PIL import Image, ImageDraw
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #in windows: install and indicate path for tesseract.exe. Installer: https://github.com/UB-Mannheim/tesseract/wiki
import cv2 as cv
import numpy as np

### global variables ###
# loads the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')


### functions ###
# detects faces and returns a list of rectangles delimiting those faces from the image passed. threshold controls accuracy
def getBoundingBoxes(img, threshold, minNeighbors):
    #load color image and pass to grayscale
    cv_img = cv.imread(img)
    cv_image = cv.cvtColor(cv_img, cv.COLOR_BGR2GRAY)
    
    #binarize the image with the hope to get some improvement in the face detection
    #cv_image = cv.threshold(cv_image,170,255,cv.THRESH_BINARY)[1]
    
    #get the bounding boxes with an especified scale size
    face_bounding_boxes = face_cascade.detectMultiScale(cv_image,threshold,minNeighbors)
    return face_bounding_boxes

# detects and returns text from an image (preferably in grayscale)
def getText(img):
    image = Image.open(img)
    img_gray = image.convert('L')
    text = pytesseract.image_to_string(img_gray)
    return text

# passes the data of an image and returns an array of cropped faces in that image
def getFacesFromImage(image_data):
    face_images = []
    #we read our image and convert it to rgb (in case the image is a gif)
    img_color = image_data[0].convert("RGB")
    #we extract the bounding boxes, crop the image and store it in the array faces
    for x,y,w,h in image_data[1]:
        bounding_box = (x,y,x+w,y+h)
        face = img_color.crop(bounding_box)
        face_images.append(face)
    return face_images   

#opens a zip file with images and returns the images, bounding boxes and text in a dictionary
def extractData(zipfile):
    data = {}
    with ZipFile(zipfile, 'r') as myzip:
        info_lst = myzip.infolist()
        for elem in info_lst:
            try:
                with myzip.open(elem) as img:
                    pil_img = Image.open(img)
                    pil_img.save("img.png")

                data[elem.filename]=[pil_img]
                #print(elem.filename+': image loaded')
                data[elem.filename].append(getBoundingBoxes("img.png", 1.3, 5))
                #print(elem.filename+': bounding boxes loaded')
                data[elem.filename].append(getText("img.png"))
                #print(elem.filename+': text loaded')                
            except Exception as e:
                print(e)
    return data

# creates a contact sheet form an array of images and displays it
def displayContactSheet(images):
    first_image = images[0]
    contact_sheet=Image.new(first_image.mode, (500,100 + 100*(len(images)-1) // 5 ))
    x, y = (0,0)

    for img in images:
        # Lets paste the current image into the contact sheet
        img.thumbnail((100,100))
        contact_sheet.paste(img, (x,y))
        # Now we update our X position. If it is going to be the width of the image, then we set it to 0
        # and update Y as well to point to the next "line" of the contact sheet.
        if x+100 == contact_sheet.width:
            x=0
            y=y+100
        else:
            x=x+100

    #display the contact sheet
    display(contact_sheet)

#only shows images of the faces in an image if it contains the word passed 
def show_faces(data, word):
    for image_data in data:
        if word in data[image_data][2]:
            print('Results found in file '+ image_data)
            faces = getFacesFromImage(data[image_data])
            if len(faces) == 0:
                print('But there were no faces in that file!')
            else:
                displayContactSheet(faces)


### main ###
#stores each image,their bounding boxes and their text     
data = {} #data = {name:[PIL image, bounding boxes, text], name:[PIL image, bounding boxes, text], ...}

data = extractData('readonly/small_img.zip')
show_faces(data, "Christopher")
data = extractData('readonly/images.zip')
show_faces(data, "Mark")


###############################################################################################





















