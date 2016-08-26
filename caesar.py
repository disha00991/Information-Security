#Encryption
def caesar(plaintext,shift):

	alphabet=["a","b","c","d","e","f","g","h","i","j","k","l",
	"m","n","o","p","q","r","s","t","u","v","w","x","y","z",]

	#Create our substitution dictionary
	dic={}
	for i in range(0,len(alphabet)):
		dic[alphabet[i]]=alphabet[(i+shift)%len(alphabet)]

	#Convert each letter of plaintext to the corrsponding
	#encrypted letter in our dictionary creating the cryptext
	ciphertext=""
	for l in plaintext.lower():
		if l in dic:
			l=dic[l]
		ciphertext+=l

	return ciphertext

#Decryption
def caesardecrypt(plaintext, shift):
    

    alphabet1=["a","b","c","d","e","f","g","h","i","j","k","l",
	"m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

	#Create our substitution dictionary
    dic1={}
    for i in range(0,len(alphabet1)):
		dic1[alphabet1[i]]=alphabet1[(i-shift)%len(alphabet1)]
    
    #Convert each letter of plaintext to the corrsponding
	#encrypted letter in our dictionary creating the cryptext
    Decryptedciphertext=""
    for l in plaintext.lower():
        if l in dic1:
            l=dic1[l]
        Decryptedciphertext+=l

    return Decryptedciphertext

#Example useage
# plaintext="the cat sat on the mat"
print "Plaintext"
plaintext = raw_input()
print "Number"
n=int(raw_input())
print "Plaintext : ", plaintext
cipher=caesar(plaintext,n)
print "Cipertext : ",cipher
print "Decrypted text : ",caesardecrypt(cipher, n)
#This will result in:
#Plaintext: the cat sat on the mat
#Cipertext: wkh fdw vdw rq wkh pdw
