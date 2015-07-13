###############################################
# Name: Anusha Kondapalli
# Class: CMPS 5363 Cryptography
# Date: 13 July 2015
# Program 1 - Playfair Cipher
###############################################


import pprint
import re
#----------------GENERATE ALPHABET-------------------------
def generateAlphabet():
    #Create empty alphabet string
    alphabet = ""
    
    #Generate the alphabet
    for i in range(0,26):
        alphabet = alphabet + chr(i+65)
        
    return alphabet

#-----------------CLEAN STRING----------------------------
def cleanString(s,options = {'up':1,'reNonAlphaNum':1,'reSpaces':'_','spLetters':'X'}):
    """
    Cleans message by doing the following:
    - up            - uppercase letters
    - spLetters     - split double letters with some char
    - reSpaces      - replace spaces with some char or '' for removing spaces
    - reNonAlphaNum - remove non alpha numeric
    - reDupes       - remove duplicate letters

    @param   string -- the message
    @returns string -- cleaned message
    """
    if 'up' in options:
        s = s.upper()
        
    if 'spLetters' in options:
        #replace 2 occurrences of same letter with letter and 'X'
        s = re.sub(r'([ABCDEFGHIJKLMNOPQRSTUVWXYZ])\1', r'\1X\1', s)
        
    if 'reSpaces' in options:
        space = options['reSpaces']
        s = re.sub(r'[\s]', space, s)
    
    if 'reNonAlphaNum' in options:
        s = re.sub(r'[^\w]', '', s)
        
    if 'reDupes' in options:
        s= ''.join(sorted(set(s), key=s.index))
        
    return s

#---------------GENERATE SQUARE------------------------------------------
def generateSquare(key):
    """
    Generates a play fair square with a given keyword.

    @param   string   -- the keyword
    @returns nxn list -- 5x5 matrix
    """
    row = 0     #row index for sqaure
    col = 0     #col index for square
    
    #Create empty 5x5 matrix 
    playFair = [[0 for i in range(5)] for i in range(5)]
    
    alphabet = generateAlphabet()
    
    #upper-case key (it may be read from stdin, so we need to be sure)
    key = cleanString(key,{'up':1,'reSpaces':'','reNonAlphaNum':1,'reDupes':1})
    
    print(key)
    
    #Load keyword into square
    for i in range(len(key)):
        playFair[row][col] = key[i]
        alphabet = alphabet.replace(key[i], "")
        col = col + 1
        if col >= 5:
            col = 0
            row = row + 1
            
    #Remove "J" from alphabet
    alphabet = alphabet.replace("J", "")
    
    #Load up remainder of playFair matrix with 
    #remaining letters
    for i in range(len(alphabet)):
        playFair[row][col] = alphabet[i]
        col = col + 1
        if col >= 5:
            col = 0
            row = row + 1
            
    return playFair
    

#----------TRANSPOSE-----------------------------------------------------
def transpose(playFair):
    """
    Turns columns into rows of a cipher square

    @param   list2D -- playFair square
    @returns list2D -- square thats transposed
    """
    #Create empty 5x5 matrix 
    trans = [[0 for i in range(5)] for i in range(5)]
    
    for col in range(5):
        for row in range(5):
           trans[col][row] = playFair[row][col] 
           
    return trans
    
#---------------GET CODED DIGRAPH--------------------------------------    
def getCodedDigraph(graph,square):
    """
    Turns a given digraph into its encoded digraph 

    @param   list -- digraph
    @returns list -- encoded digraph
    """
    row = 0     #row index for square
    col = 0     #col index for square

    digraph = [[0 for i in range(2)] for i in range(len(graph)//2)]
    newDigraph = [0 for i in range(len(graph))]
    
    
    for i in range(len(graph)):
        digraph[row][col] = graph[i]
        col = col + 1
        if col >= 2:
            col = 0
            row = row + 1
            
    
    rows=0
    cols=0
    r=0
    for rows in range(len(graph)//2):
        for cols in range(2):
            for row in range(5):
                for col in range(5):
                    if cols==0:
                        if square[row][col] == digraph[rows][0]:
                            cola = col
                            rowa = row
                    elif cols==1:
                        if square[row][col] == digraph[rows][1]:
                            colb = col
                            rowb = row
 
        #Check to see if digraph is in same row
        if rowa==rowb:
            newDigraph[r]=square[rowa][(cola+1)%5]
            newDigraph[r+1]=square[rowa][(colb+1)%5]
        #Check to see if digraph is in same col
        elif cola==colb:
            newDigraph[r]=square[(rowa+1)%5][cola]
            newDigraph[r+1]=square[(rowb+1)%5][colb]
        #If different coloum and row
        else:
            newDigraph[r]=square[rowa][colb]
            newDigraph[r+1]=square[rowb][cola]
        r=r+2
        
    return newDigraph
    
#---------------------getDecodeedDigraph----------------------

def getDecodedDigraph(graph,square):
    newDigraph = [0 for i in range(len(graph))]
    r=0
    for rows in range(len(graph)//2):
        for cols in range(2):
            for row in range(5):
                for col in range(5):
                    if cols==0:
                        if square[row][col] == graph[r]:
                            cola = col
                            rowa = row
                    elif cols==1:
                        if square[row][col] == graph[r+1]:
                            colb = col
                            rowb = row
        if rowa==rowb:
            newDigraph[r]=square[rowa][(cola+4)%5]
            newDigraph[r+1]=square[rowa][(colb+4)%5]
        #Check to see if digraph is in same col
        elif cola==colb:
            newDigraph[r]=square[(rowa+4)%5][cola]
            newDigraph[r+1]=square[(rowb+4)%5][colb]
        #If different col and row
        else:
            newDigraph[r]=square[rowa][colb]
            newDigraph[r+1]=square[rowb][cola]
        r=r+2  
        
    return newDigraph
    
###########################################################################

while True:
    # providing the options
    print("Playfair Tool (P.T)")
    print("Written By:Anusha Kondapalli")
    print("***************************************************")
    print("1. Encoding")
    print("2. Decoding")
    print("3. Exit")
    Choice=input("Enter the choice: ")
    print("***************************************************")
    print()
    #for encryption
    if(Choice == '1'):
        print("Playfair Encryption Tool (P.E.T)")
        print("Written By:Anusha Kondapalli")
        print("***************************************************")
        message=input(' Please enter a message: ')
        print("***************************************************")
        print()
        print("Playfair Encryption Tool (P.E.T)")
        print("Written By:Anusha Kondapalli")
        print("***************************************************")
        key=input("Please enter a keyword:")
        print("***************************************************")
        print()
        #removing numbers
        message=re.sub('[0-9]+', '', message)
        #creating square using key 
        playFair = generateSquare(key)
        print()
        for list in playFair:
            print(list)
        print()
        #transpose of square
        transPlayFair = transpose(playFair) 
        print()
        for list in transPlayFair:
            print(list)
        #cleaning the given message    
        message=cleanString(message,{'up':1,'reSpaces':'','reNonAlphaNum':1,'spLetters':'X'})
        
        if (len(message)%2) !=0:
            message= message+"X"
        #writing a encripted mesage for given message
        list1=getCodedDigraph((message),transPlayFair)
        print("Playfair Encryption Tool (P.E.T)")
        print("Written By:Anusha Kondapalli")
        print("***************************************************")
        str1 = ''.join(list1)
        print(str1)
        print("***************************************************")
        print()
    #for decryption
    elif(Choice == '2'):
        print("Playfair Decryption Tool (P.D.T)")
        print("Written By:Anusha Kondapalli")
        print("***************************************************")
        message=input(' Please enter a message: ')
        print("***************************************************")
        print()
        print("Playfair Decryption Tool (P.D.T)")
        print("Written By:Anusha Kondapalli")
        print("***************************************************")
        key=input("Please enter a keyword:")
        print("***************************************************")
        print()
       #creating square using key
        playFair = generateSquare(key)
        print()
        #creating square using key
        for list in playFair:
            print(list)
        print()
        #transpose the square
        transPlayFair = transpose(playFair) 
        print()
        for list in transPlayFair:
            print(list)
        #writing decripted message for given message
        list1=getDecodedDigraph((message),transPlayFair)
        print("Playfair Decryption Tool (P.D.T)")
        print("Written By:Anusha Kondapalli")
        print("***************************************************")
        str1 = ''.join(list1)
        print(str1)
        print("***************************************************")
        print()
        
    else:
        # breaking the infinite loop if the value is other than 1 or 2
        break