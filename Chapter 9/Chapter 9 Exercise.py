# imports
import random
import string

def encrypt():
    # encrypt takes a file, reads its contents, and encrypts it all in a new
    
    # create the key
    key = {'a': 's', 'b': 'O', 'c': 'Y', 'd': 'p', 'e': 'd', 'f': 'v', 'g': 'S', 'h': 'E', 'i': 'K', 'j': 'Q', 'k': 'k', 'l': 'w', 'm': 'f', 'n': 'V', 'o': 'A', 'p': 'e', 'q': 'a', 'r': 'q', 's': 'G', 't': 'y', 'u': 'l', 'v': 'I', 'w': 'n', 'x': 'i', 'y': 'H', 'z': 'u', 'A': 'c', 'B': 'r', 'C': 'h', 'D': 't', 'E': 'W', 'F': 'b', 'G': 'Z', 'H': 'j', 'I': 'T', 'J': 'P', 'K': 'g', 'L': 'R', 'M': 'J', 'N': 'L', 'O': 'z', 'P': 'C', 'Q': 'o', 'R': 'B', 'S': 'F', 'T': 'U', 'U': 'm', 'V': 'N', 'W': 'M', 'X': 'D', 'Y': 'X', 'Z': 'x', " ": " ", "\n" : "\n"}
    file = open("storage_file.txt", "r")
    encoded_file = open("encoded_file.txt", "w")
    
    # encode the file
    for line in file:
        encoded_line = ""
        
        for letter in line:
            encoded_line += key[letter]
        
        encoded_file.write(encoded_line)

def decrypt():
    # decrypt takes a file, reads it contents, and decrypts it in a new file
    
    # create the key
    key = {'a': 's', 'b': 'O', 'c': 'Y', 'd': 'p', 'e': 'd', 'f': 'v', 'g': 'S', 'h': 'E', 'i': 'K', 'j': 'Q', 'k': 'k', 'l': 'w', 'm': 'f', 'n': 'V', 'o': 'A', 'p': 'e', 'q': 'a', 'r': 'q', 's': 'G', 't': 'y', 'u': 'l', 'v': 'I', 'w': 'n', 'x': 'i', 'y': 'H', 'z': 'u', 'A': 'c', 'B': 'r', 'C': 'h', 'D': 't', 'E': 'W', 'F': 'b', 'G': 'Z', 'H': 'j', 'I': 'T', 'J': 'P', 'K': 'g', 'L': 'R', 'M': 'J', 'N': 'L', 'O': 'z', 'P': 'C', 'Q': 'o', 'R': 'B', 'S': 'F', 'T': 'U', 'U': 'm', 'V': 'N', 'W': 'M', 'X': 'D', 'Y': 'X', 'Z': 'x', " ": " ", "\n" : "\n"}
    decoded_file = open("decoded_file.txt", "w")
    encoded_file = open("encoded_file.txt", "r")
    reversed_key = {}
    
    # create reversed key
    for item in key:
        temp_item = key[item]
        
        reversed_key[temp_item] = item
    
    # decode the file
    for line in encoded_file:
        decoded_line = ""
        
        for letter in line:
            decoded_line += reversed_key[letter]
        
        decoded_file.write(decoded_line)