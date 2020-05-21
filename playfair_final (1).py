import sys
import re
import random
def matrix(key):
	matrix=[]
	for e in key.upper():
		if e not in matrix:
			matrix.append(e)
	alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"
	
	for e in alphabet:
		if e not in matrix:
			matrix.append(e)	
	
	#initialize a new list
	matrix_group=[]
	for e in range(5):
		matrix_group.append('')

	#Break it into 5*5
	matrix_group[0]=matrix[0:5]
	matrix_group[1]=matrix[5:10]
	matrix_group[2]=matrix[10:15]
	matrix_group[3]=matrix[15:20]
	matrix_group[4]=matrix[20:25]
	return matrix_group

def message_to_digraphs(message_original):
	#Change it to Array
	message=[]
	for e in message_original:
		message.append(e)

	#Delete space
	for unused in range(len(message)):
		if " " in message:
			message.remove(" ")

	#If both letters are the same, add an "X" after the first letter.
	i=0
	for e in range(len(message)/2):
		if message[i]==message[i+1]:
			message.insert(i+1,'X')
		i=i+2

	#If it is odd digit, add an "X" at the end
	if len(message)%2==1:
		message.append("X")
	#Grouping
	i=0
	new=[]
	for x in xrange(1,len(message)/2+1):
		new.append(message[i:i+2])
		i=i+2
	return new

def find_position(key_matrix,letter):
	x=y=0
	for i in range(5):
		for j in range(5):
			if key_matrix[i][j]==letter:
				x=i
				y=j

	return x,y
def cipher_to_digraphs(cipher):
	i=0
	h=[]
	for x in range(len(cipher)/2):
		h.append(cipher[i:i+2])
		i=i+2
	new = "" 
  
    	for x in h: 
        	new = new + x[0] + x[1]  
  	
	return new

def encrypt(message,key):
	message=message_to_digraphs(message)
	key_matrix=matrix(key)
	cipher=[]
	for e in message:
		p1,q1=find_position(key_matrix,e[0])
		p2,q2=find_position(key_matrix,e[1])
		if p1==p2:
			if q1==4:
				q1=-1
			if q2==4:
				q2=-1
			cipher.append(key_matrix[p1][q1+1])
			cipher.append(key_matrix[p1][q2+1])		
		elif q1==q2:
			if p1==4:
				p1=-1;
			if p2==4:
				p2=-1;
			cipher.append(key_matrix[p1+1][q1])
			cipher.append(key_matrix[p2+1][q2])
		else:
			cipher.append(key_matrix[p1][q2])
			cipher.append(key_matrix[p2][q1])
	new=cipher_to_digraphs(cipher)
	return new

def vernam(key,message):
    message = str(message)
    m = message.upper().replace(" ","") 	# Convert to upper case, remove whitespace
    encrypt = ""
    try:
        key = int(key)           		# if the key value is not a number, then run with key = 0
    except ValueError:
        key = 0
    for i in range(len(m)):
        letter = ord(m[i])-65      		# Letters now range 0-25
        letter = (letter + key)%25 		# Alphanumeric + key mod 25 = 0-25
        letter +=65
        

        encrypt = encrypt + chr(letter) 	# Concatenate message
        
    return encrypt

count = 0


f = open("diary.txt", "r")
string = f.read()
line = re.sub(r"[\n\t\s]*", "", string)
#print line
n = 10
lines = map(''.join, zip(*[iter(line)]*n))
#print(lines)
for l in lines:
	#print(l)
	count=count+1
	keys = []
	key=random.randint(0,99)
	keys.append(key)
	key1="crypto"
	enc=vernam(key,l)
	cp=encrypt(enc,key1)
	print(cp)
