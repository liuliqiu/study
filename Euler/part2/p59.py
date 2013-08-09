##Each character on a computer is assigned a unique code and the preferred
##standard is ASCII (American Standard Code for Information Interchange). For
##example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
##A modern encryption method is to take a text file, convert the bytes to ASCII,
##then XOR each byte with a given value, taken from a secret key. The advantage
##with the XOR function is that using the same encryption key on the cipher text,
##restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
##For unbreakable encryption, the key is the same length as the plain text message
##, and the key is made up of random bytes. The user would keep the encrypted
##message and the encryption key in different locations, and without both "halves"
##, it is impossible to decrypt the message.
##Unfortunately, this method is impractical for most users, so the modified method
##is to use a password as a key. If the password is shorter than the message,
##which is likely, the key is repeated cyclically throughout the message. The
##balance for this method is using a sufficiently long password key for security,
##but short enough to be memorable.
##Your task has been made easy, as the encryption key consists of three lower
##case characters. Using cipher1.txt (right click and 'Save Link/Target As...'),
##a file containing the encrypted ASCII codes, and the knowledge that the plain
##text must contain common English words, decrypt the message and find the sum of
##the ASCII values in the original text.
def test(nums):
    v=[32]+list(range(65,91))+list(range(97,123))
    z=[[i^j for j in v] for i in nums]
    x=[{},{},{}]
    y=[0,0,0]
    for i in range(len(z)):
        for c in range(3):
            if i%3==c:
                y[c]=y[c]+1
                for j in z[i]:
                    if j in x[c]:
                        x[c][j]=x[c][j]+1
                    else:
                        x[c][j]=1
    re=[]
    for i in range(3):
        a,b=0,0
        for j in range(97,123):
            if x[i][j]>a:
                a,b=x[i][j],j
        re.append(b)
    return re
def fi():
    f=open('txt\\cipher1.txt')
    s=f.read().strip()
    ns=[int(c) for c in s.split(',')]
    z=test(ns)
    s=sum([z[i%3]^ns[i] for i in range(len(ns))])
    print(s)
fi()
