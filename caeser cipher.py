print("ENCRYPTION AND DECRYPTION TOOL")
pwd = input("Enter the password: ")

if pwd == "r34Godzilla" or pwd == "7150":
    
    print("||ACCESS GRANTED||")
    choice = int(input("Enter 1 to encrypt or 0 to decrypt: "))
    key = int(input("Enter the key of this cipher: "))

    if choice == 1: 
        inp = input("Enter something to be encoded: ")
        encrypt = ' '
        for i in inp:
            encrypt = encrypt +  chr(ord(i)+ int(key))
        
        print("The encrypted statement is: " + str(encrypt))

    elif choice == 0:
        inp = input("Enter the encrypted code: ")
        decrypt = ' '
        for i in inp:
            decrypt = decrypt +  chr(ord(i)-int(key))
        
        print("The decrypted code is "+ str(decrypt))

    else:
        print("Enter only 0 or 1 for your desired output.")


else: 
    print("----ACCESS DENIED----")

print()
print("            Author --> ACE")
