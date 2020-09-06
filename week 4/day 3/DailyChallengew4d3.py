def encrypt (text,num):
    result = ''
    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + num-65) % 26 + 65)    
        else:
            result += chr((ord(char) + num - 97) % 26 + 97)
    return result        
text = "secret code"
num = 13            
print ("Cipher: " + encrypt(text,num))        