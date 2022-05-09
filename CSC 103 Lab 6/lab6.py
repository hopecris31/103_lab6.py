#Hope Crisafi
#Lab 5
#5/4/21
#Michael Shaw

#NJW 6.75/10

#NJW DO NOT comment out code that answers my questions.

#Part 1

# sent = input('enter a sentence:')
# print('the letter Z occurs',sent.count('z'),'time(s)')


# sent = input('enter another sentence:')

#NJW (-0.5) This isn't the correct order. sent.split() isn't used
#NJW anywhere. You're counting words in the string, and not the list
#NJW as requested.

# numZebra = sent.count('zebra')

# sent.split()

# print('zebra occurs',numZebra,'time(s) in the sentence')



#Part 2

# sent = 'The temperature today is going to be around > 100 degrees F'
# #endSent = len(sent)
# temp = sent[-13:-9]

# print(temp)


#Part 3

# sent.find('d')
# #The find method returns an integer index value
# #find(var[start,end]It would return the lowest index value found in the string, if contained in the range
# #They are interpreted as slice notation, and returns -1 if slice not found



# #Part 4

#NJW (-0.5) You don't use find, as requested

# sentList = sent.split()
# tempIndex = sentList[9:10]

# print('temperature: ',tempIndex)



#Part 5


# sent = input('enter a sentence: ')
# #sentList = list(sent)

# sent = sent.replace(".","")
# sent = sent.replace("'","")
# sent = sent.replace(" ","")
# sent = sent.lower()

# print(sent)

#NJW From the lab:
#NJW DO NOT USE SLICING, OR ANY MEANS TO REVERSE A STRING TO DO THIS!!
#NJW (-2)

# sentBegin = sent[0::1]
# sentEnd = sent[-1::-1]
# end = len(sent)  
# index = 0

# #print(sentList)

# print('forwards',sentBegin)
# print('backwards',sentEnd)

# while index < 1:

#     if sentBegin == sentEnd:
#         print('its a palindrome')
#         index += 1
#     else:
#         print("it's not a palindrome")
#         index += 1





#1. break the sentence up by character
#2. compare each character, from start to end, in the order that they meet in the middle
#3. if the characters match in that order, then they are a palindrome
#4. remove unnecessary characters (spaces,punctuation)

# if " " or "'" in sentList:
#     sentList.remove(' ')
#     sentList.remove("'")
# else:
#     #assign else



#use lsit

#footy.split returns a list
#for utilizes int

footyText = "Football refers to a number of sports that involve kicking a ball \
with the foot to score a goal. The most popular of these sports worldwide is \
association football, more commonly known as just 'football' or 'soccer'. \
Unqualified, the word football applies to whichever form of football is the \
most popular in the regional context in which the word appears, including \
association football, as well as American football, Australian rules football, \
Canadian football, Gaelic football, rugby league, rugby union, and other \
related games. These variations of football are known as football codes.Various \
forms of football can be identified in history, often as popular peasant games. \
Contemporary codes of football can be traced back to the codification of these \
games at English public schools in the eighteenth and nineteenth century. The \
influence and power of the British Empire allowed these rules \
of football to spread to areas of British influence outside of the directly \
controlled Empire, though by the end of the nineteenth century, distinct \
regional codes were already developing: Gaelic Football, for example, \
deliberately incorporated the rules of local traditional football games in \
order to maintain their heritage. In 1888, The Football League was founded in \
England, becoming the first of many professional football competitions. During \
the twentieth century, several of the various kinds of football grew to become \
among the most popular team sports in the world."
footyText = footyText.lower()
footyText = footyText.split()
length = len(footyText)
football = 'football'
footballCount = 0


#print(footyText)

for word in footyText:
    print('word count:',length)
    break #sorry #NJW (-0.25) Don't. Why do you need a loop? Just
                 #NJW print length?

for football in footyText:
        footballCount += 1
        print('times football is used:',football[footballCount])

#    if football in footyText:
