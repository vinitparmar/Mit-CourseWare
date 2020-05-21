import math
import sys
import string

# reads the file
# returns the lines in the file in form of list
def read_file(file):
    try:
        with open(file,'r') as f:
            data = f.read()
        return data

    except IOError:
        print("Error in the file dpening or reading: ",file)
        sys.exit()

# defined as global variable
# converts all the puntuation to spaces 
# converts uppercase to lowercase
translationTable = str.maketrans(string.punctuation+string.ascii_uppercase,
                                " "*len(string.punctuation)+string.ascii_lowercase)

# return the list of words form the file
def getWordsFromLineListDef(text):

    text = text.translate(translationTable)
    word_list = text.split()
    return word_list


def count_frequency(wordlist):
    D = {}

    for new_word in wordlist:
        if new_word in D:
            D[new_word] = D[new_word]+1
        else:
            D[new_word] = 1
    return D


# takes the file as input and gives the word frequecy
# return a dictionary of words
def wordFrequencyForFile(file):
    line_list =  read_file(file) 
    wordsList = getWordsFromLineListDef(line_list)
    frequency_mapping = count_frequency(wordsList)
    print("=================================")
    print("File", file, ":", ) 
    print(len(line_list), "lines, ", ) 
    print(len(wordsList), "words, ", ) 
    print(len(frequency_mapping), "distinct words") 
  
    return frequency_mapping 


def dotPtoduct(d1,d2):
    Sum = 0.0
    for key in d1:
        if key in d2:

            Sum = Sum + (d1[key]*d2[key])

    return Sum

# returns the angle in radians  
# between document vectors 
def vector_angle(D1, D2): 
    numertor = dotPtoduct(D1,D2)
    denominator = math.sqrt(dotPtoduct(D1,D1)*dotPtoduct(D2,D2))
    return math.acos(numertor/denominator)



# this function takes input as 2 files to be compared
def documentSimilarity(filename1,filename2):
    sortedWordListForFile1 = wordFrequencyForFile(filename1)
    sortedWordListForFile2 = wordFrequencyForFile(filename2)  
    # calculate angle to do
    distance = vector_angle(sortedWordListForFile1, sortedWordListForFile2) 

    print("The distance between the documents is: % 0.6f (radians)"% distance) 

# driver code
# pass 2 file to find the document distance
documentSimilarity('file1.txt','file2.txt')