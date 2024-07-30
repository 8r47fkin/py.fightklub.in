message=input("What would you like to do? \nEncrypt\nDecrypt\n")
if message=="Encrypt":
    print("Your message will be encrypted\n")
    message=input("Enter your message here:")
    x1=message
    translated=''
    i=len(message)-1
    while i>=0:
        translated=translated+message[i]
        i=i-1
    print(translated)
elif message=="Decrypt":
    print("Your message will be decrypted\n")
    message=input("Enter the encrypted message:")
    y1=message
    translated=''
    i=len(message)-1
    while i >= 0:
        translated=translated+message[i]
        i=i-1
    print(translated)