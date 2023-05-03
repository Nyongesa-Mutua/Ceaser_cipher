print("Hello, cryptanalytic nefarious arts fans. I kept a diary when I was younger.")
print("Since my diary had all my dark secrets, I was constantly worried that someone would read it in my absence.")
print("I did not want nobody snooping around my shit.")
print("Therefore, I did what was logical and looked into how to encrypt text before I wrote it in my diary.") 
print("Using the Caesar Cipher was one method I discovered.")
print("Simply type or paste the phrase you want to be encrypted, and the program will take care of the rest.")

symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.?,:;'1234567890abcdefghijklmnopqrstuvwxyz"
total = len(symbols)
try:
    import pyperclip # pyperclip copies text to the clipboard.
except ImportError:
    pass

translated = ''
text = str(input("Enter the message in concern."))

while True:
    mode = str(input('Do you want to encrypt(e), decrypt(d) or quit(q)')).lower()
    if mode.startswith("e"):
        mode == "encrypt"
        break
    elif mode.startswith("d"):
        mode == "decrypt"
        break
    elif mode.startswith("q"):
        break
    else:
        print("Invalid input please try again.")
        continue
    
    
while True:
    somet = int(input("Enter a key you want to use for encryption"))
    if somet>total:
        key = somet-len(symbols)
        break
    elif somet<0:
        key= somet+len(symbols)
        break
    else:
        key = somet
        break   
    
for symbol in text:
    if symbol in symbols:
 # Get the encrypted (or decrypted) number for this symbol.
        num = symbols.find(symbol) # Get the number of the symbol.
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num-key
# symbols or less than 0:
        if num >= len(symbols):
            num = num - len(symbols)
        elif num < 0:
            num = num + len(symbols)
 # Add encrypted/decrypted number's symbol to translated:
        translated = translated + symbols[num]
    else:
 # Just add the symbol without encrypting/decrypting:
        translated = translated + symbol


try:
    pyperclip.copy(translated)
    print(translated)
except:
    pass # Do nothing if pyperclip wasn't installed.
    
    

    
    

    



    
    