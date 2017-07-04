# morse code translator

###To edit: deal with punctuation and special symbols
###Also keep the original case of letter.

DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
while True:
    EorD = raw_input("Enter E to encrypt a message and D to decrypt a message (Q to exit): ")
    #Encryption
    if EorD.capitalize() == 'E':
        mesg = raw_input("Enter your secret message: ")
        encoded = []

        for i in mesg:
            if i == " ":
                encoded.append("  ")
            else:
                encoded.append(DICT.get(i.capitalize()))

        result = " ".join(encoded)
        print "The corresponding code is: " + result

    #Decryption
    elif (EorD.capitalize()== 'D'):
        code = raw_input("Enter the code: ") + ' '
        decoded = []
        cipher = ''
        for i in code:
            if (i != ' '):
                count = 0
                cipher += i
            else:
                count += 1
                if count == 2:
                    decoded.append(" ")
                else:
                    for k,v in DICT.iteritems():
                        if v == cipher:
                            decoded.append(k)
                            cipher = '' 
        print ''.join(decoded)

    #Quit the program
    elif (EorD.capitalize()== 'Q'):
        print "Bye Bye."
        break
    
    else:
        print "Please enter a valid input." 
                    
