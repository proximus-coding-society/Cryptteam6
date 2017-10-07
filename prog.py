inp=raw_input('Enter your text : ')
k=input("Enter a key between 1-26  : ")
d=input('press 1: For Caesar Cipher\npress 2: For Simple substitution cipher\nPress 3: For Vigenere Cipher')
#Caesar Cipher
#alph='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#len_alpha=len(alpha)
#len_inp=len(inp)
if(d==1):
    size=len(inp)
    out1=[""for x in range(size)]
    for x in range(len(inp)):
        s=inp[x]
        out1[x]=chr(ord(s)+3)
    print '%s' % ''.join(map(str,out1))
    
#Simple Substitution Cipher
let='abcdefghijklmnopqrstuvwxyz'
cyp='KDGFNSLVBWAHEXJMQCPZRTYIUO'
out2=[""for t in range(len(inp))]
if(d==2):
    for x2,t in zip(inp.lower(),range(len(inp))):
        for y2 in let: 
            if(y2==x2):
                c=let.find(y2)
                out2[t]=cyp[c]
    print '%s' % ''.join(map(str,out2))

# Vigenere Cipher : key is school
if(d==3):
    key=['s','c','h','o','o','l']
    #num_key=[""for t in range(len(key))]
    #for x3,t in zip(range(len(key)),range(len(inp))):
     #   num_key[t]=ord(key[x3])
    #for x3 in range
    n = len(inp)
    num_key=n*[16,15,9,14,20,3]
    out3=[""for x3 in range(len(inp))]
    for x3,t in zip(range(len(inp)),range(len(num_key))):
        out3[x3]=chr(ord(inp[x3])-num_key[t])
        #print out3[x]
    print '%s' % ''.join(map(str,out3))

    

#Caesar Decryption
dec=input("Enter your key for decryption : ")
if(dec==k):
    if(d==1):
        dec_out1=[""for x in range(len(out1))]
        for x in range(len(out1)):
            s=out1[x]
            dec_out1[x]=chr(ord(s)-3)
        print '%s' % ''.join(map(str,dec_out1))

#Simple Substitution Decryption
    if(d==2):
        dec_out2=[""for t in range(len(out2))]
        for x2,t in zip(out2,range(len(out2))):
            for y2 in cyp: 
                if(y2==x2):
                    c=cyp.find(y2)
                    dec_out2[t]=let[c]
        print '%s' % ''.join(map(str,dec_out2))

# Vigenere Decryption
    if(d==3):
    #num_key=[""for t in range(len(key))]
    #for x3,t in zip(range(len(key)),range(len(inp))):
     #   num_key[t]=ord(key[x3])
    #for x3 in range
    #n = len(inp)
    #num_key=n*[16,15,9,14,20,3]
        dec_out3=[""for x3 in range(len(out3))]
        for x3,t in zip(range(len(out3)),range(len(num_key))):
            dec_out3[x3]=chr(ord(out3[x3])+num_key[t])
            #print out3[x]
        print '%s' % ''.join(map(str,dec_out3))

else:
    print "Wrong Key provided"


    
