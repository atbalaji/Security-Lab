import random

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi

def computeGCD( eValue, phiValue):

    while phiValue != 0:
        eValue , phiValue = phiValue , eValue % phiValue
    
    return eValue




inputPrimeNumberOne = input("Enter a Prime Number : ")

inputPrimeNumberTwo = input("Enter another Prime Number : ")

nValue = inputPrimeNumberOne * inputPrimeNumberTwo

phiValue = (inputPrimeNumberOne-1)*(inputPrimeNumberTwo-1)

eValue = random.randrange(1,phiValue)

gcdValue = computeGCD( eValue,phiValue )

while gcdValue != 1:
    eValue = random.randrange(1,phiValue)
    gcdValue = computeGCD( eValue,phiValue )

dValue = multiplicative_inverse( eValue , phiValue)

print "Public Key ======>   n = " + str(nValue) + " e = " + str(eValue)
print "\n"
print "Private Key ========> n = " + str(nValue) + " d = " + str(dValue)

print "\n"

inputMessage = raw_input("Enter message to be passed : ")

counter = 0

encryptedCipherList = []
print 'encrypted'
while counter < len(inputMessage):
    value = ((ord(inputMessage[counter])-97) ** eValue) % nValue
    print str(value) + '\t'
    encryptedCipherList.append(value)
    counter = counter + 1
print 'over'
encryptedString = ""
counter = 0

while counter < len(encryptedCipherList):
    encryptedString = encryptedString + str(encryptedCipherList[counter])
    counter = counter + 1
print encryptedString

decryptedString = ""

counter = 0

while counter < len(encryptedCipherList):

    value = chr((encryptedCipherList[counter] ** dValue ) % nValue )
    decryptedString = decryptedString + value
    counter = counter + 1

print decryptedString

print "\n Intruding phase"

S = []

counter = 0

while counter < 26:
    value = pow(counter, eValue);
    value = value % nValue
    S.append(value)
    counter= counter + 1
   
    

counter =0 

while counter < len(encryptedCipherList):
    value = encryptedCipherList[counter]
    second_counter = 0
    while (second_counter<26  and S[second_counter]!=value) :
       second_counter= second_counter + 1
    print (chr(97+second_counter))  
    counter+=1


