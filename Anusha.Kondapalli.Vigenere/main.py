#Name:Anusha Kondapalli
#course:Cryptography
#Program:2-Vigenere cipher
#main.py
import argparse
from randomized_vigenere import RandomizedVigenere

parser = argparse.ArgumentParser()
p = RandomizedVigenere()
parser.add_argument("-m", "--mode", dest="mode", default = "encrypt", help="Encrypt or Decrypt")
parser.add_argument("-i", "--inputfile", dest="inputFile", help="Input Name")
parser.add_argument("-o", "--outputfile", dest="outputFile", help="Output Name")
parser.add_argument("-s", "--seed", dest="seed",help="Integer seed")

args = parser.parse_args()
seedVal=args.seed
print(seedVal)
f = open(args.inputFile,'r')
message = f.read()
if(args.mode == 'encrypt'):
    data = p.encrypt(message,int(seedVal))
    o = open(args.outputFile,'w')
    o.write(str(data))
    o.close()
else:
    data = p.decrypt(message,int(seedVal))
    o = open(args.outputFile,'w')
    o.write(str(data))
    o.close()
