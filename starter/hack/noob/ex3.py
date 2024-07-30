def Encryptmessage(str, key1):
    encstring=""
    for i in str:
        if(ord(i))>=65 and (ord(i)<=90):
            tempstr=(ord(i)+key1)
            if tempstr>90:
                tempstr=tempstr%90+64
            encstring=encstring+chr(tempstr)
        elif(ord(i))>97 and (ord(i)<=122):
            tempstr=(ord(i)+key1)
            if tempstr>122:
                tempstr=tempstr%122+96
            encstring=encstring+chr(tempstr)
        else:
            encstring=encstring+chr(ord(i)+key1)
    return encstring
def Decryptmessage(key1):
    ptr=Encryptmessage(str, key1)
    dncstring=""
    for i in ptr:
        if ((ord(i))>=65) and (ord(i))<=90:
            dncstring=dncstring+chr((ord(i)-key1-65)%26+65)
        elif((ord(i))>=97) and (ord(i))<122:
            dncstring=dncstring+chr((ord(i)-key1-97)%26+97)
        else:
            dncstring=dncstring+chr(ord(i)-key1)
    return dncstring
print("Enter the string to Encrypt and decrypt :")
str=input()
print("Enter the key(Eg.11):")
keyp=int(input())
keyp=keyp%26
print("Encrypted string : ",Encryptmessage(str,keyp))
print("Decrypted String : ",Decryptmessage(keyp))