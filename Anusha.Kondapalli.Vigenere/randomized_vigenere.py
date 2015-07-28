#Name:Anusha Kondapalli
#course:Cryptography
#Program:2-Vigenere cipher
#randomized_vigenere.py
import random

#############################################################################
# keywordFromSeed -
#    Works by peeling off two digits at a time, and using modulo to map it into
#    the proper range of A-Z for use as a keyword.
# Example:
#    This example spells math, and I chose values 0-25 on purpose, but
#    it really doesn't matter what values we choose because 99 % 26 = 21 or 'V' 
#    or any value % 26 for that matter.
#
#    seed = 12001907
#    l1   = 12001907 % 100 = 07 = H
#    seed = 12001907 // 100 = 120019
#    l2   = 120019 % 100 = 19 = T
#    seed = 120019 // 100 = 1200
#    l3   = 1200 % 100 = 0 = A
#    seed = 1200 // 100 = 12
#    l4   = 12 % 100 = 12 = M
#    seed = 12 // 100 = 0
#
# @param {int} seed - An integer value used to seed the random number generator
#                     that we will use as our keyword for vigenere
# @return {string} keyword - a string representation of the integer seed
#############################################################################
#class
class RandomizedVigenere:
    def __init__(self):
        pass
    #using seed creating keyword
    def keywordFromSeed(self,seed):
        Letters = []
        while seed > 0:
            Letters.insert(0,chr((seed % 1000) % 95 + 32))
            seed = seed // 1000
        key=''.join(Letters)
        return key
        
        
    #encrypting the given message
    #---------------------------------------------------------------
    def encrypt(self,plain_text_message,seed):
        #seed=int(Decimal(seed)
        keyword = self.keywordFromSeed(seed)
        symbols = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
        #creating unique randomized vigenere table using seed
        vigenere = self.buildVigenere(symbols,seed)
        #print(vigenere)
        l=len(keyword)
        n=len(plain_text_message)
        s=len(symbols)
        cipher_text=[0 for i in range(n)]
        key=[0 for i in range(l)]
        for i in range(l):
            key[i] = keyword[i]
        j=0
        while(j<n):
            k=0
            while(k<l):
                for i in range(s):
                    if(vigenere[i][0]==key[k] and j<n):
                        sym=ord(plain_text_message[j])-32
                        cipher_text[j]=vigenere[i][sym]
                k=k+1
                j=j+1
        cipher_text_message = ''.join(cipher_text) 
        return cipher_text_message
    
    #decrypting the given message
    #--------------------------------------------------------------
    def decrypt(self,cipher_text_message,seed):
        keyword =self. keywordFromSeed(seed)
        symbols = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
        #creating unique randomized vigenere table        
        vigenere = self.buildVigenere(symbols,seed)
        l=len(keyword)
        n=len(cipher_text_message)
        s=len(symbols)
        plain_text=[0 for i in range(n)]
        key=[0 for i in range(l)]
        for i in range(l):
            key[i] = keyword[i]
        j=0
        while(j<n):
            k=0
            while(k<l):
                for i in range(s):
                    if vigenere[i][0]==key[k] and j<n:
                        for a in range(s):
                            if(vigenere[i][a]==cipher_text_message[j]):
                                sym=a+32
                                plain_text[j]=chr(sym)
                k=k+1
                j=j+1
        plain_text_message = ''.join(plain_text)
        return plain_text_message
    #this function is creating ramdomized function
    #--------------------------------------------------------------- 
    def buildVigenere(self,symbols,seed):
        tep=self.seedVigenere(seed,symbols)
        n = len(symbols)
        vigenere = [[0 for i in range(n)] for i in range(n)]
        temp=[0 for i in range(n)]
        for i in range(n):
            temp[i] = tep[i]
        col=[0 for i in range(n)]
        for i in range(n):
            col[i]=i
        random.shuffle(col,random.random)
        j=0
        while(j<n):
            for i in range(n):
                vigenere[col[j]][i]=chr((ord(temp[i]) +j)% 95 + 32)
            j=j+1
        return vigenere
    
    #shuffele the symbols 
    def seedVigenere(self,seed,symbols):
        random.seed(seed)
        n=len(symbols)
        temp=[0 for i in range(n)]
        for i in range(n):
            temp[i] = symbols[i]
        random.shuffle(temp)
        #print(temp)
        return temp
        