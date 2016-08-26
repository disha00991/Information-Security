# Implement yourself

#Encryption 
def rotor(plaintext,shift):
    
	alphabet=["a","b","c","d","e","f","g","h","i","j","k","l",
	"m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

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
def rotordecrypt(plaintext, shift):
    

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
print "Plaintext "
plaintext = raw_input()

print "Scaling Factor for rotor 1"
n1=int(raw_input())
print "Scaling Factor for rotor 2"
n2=int(raw_input())
print "Scaling Factor for rotor 3"
n3=int(raw_input())
print "Plaintext:", plaintext
rotor1text=rotor(plaintext, n1)
print "After passing from rotor 1 : ",rotor1text
rotor2text=rotor(rotor1text, n2)
print "After passing from rotor 2 : ",rotor2text
rotor3text=rotor(rotor2text, n3)
print "After passing from rotor 3 [Ciphertext] : ",rotor3text
decrypt1 = rotordecrypt(rotor3text, n3)
print "Retreival string from rotor 3 : ", decrypt1
decrypt2= rotordecrypt(decrypt1, n2)
print "Retreival string from rotor 2 : ", decrypt2
decrypt3 = rotordecrypt(decrypt2, n1)
print "Retreival string from rotor 1 [Original String] : ", decrypt3
# print "Cipertext:",caesar(plaintext,3)
#This will result in:
#Plaintext: the cat sat on the mat
#Cipertext: wkh fdw vdw rq wkh pdw
