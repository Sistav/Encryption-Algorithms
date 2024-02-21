# Created by Georgios Dialynas-Vatsis
import random
class Message:
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    def __init__(self,message = ""):
        self.message = message.upper()

    def getText(self):
        return self.message
    
    def setText(self):
        self.message = plaintextMsg.upper()

class plaintextMsg(Message):
    def __init__(self, message=""):
        super().__init__(message)
    
    def substitutionCipher(self,substitutions = []):
    # Make 2 copies of the alphabet, one to modify
    # I could've made it a dictionary, but I prefer to work with lists
        normalAlpha = Message.alpha.copy()
        ciperAlpha = Message.alpha.copy()

        # Go through all the substitution pairs
        for i in range(len(substitutions)):
            # Get the 2 positions
            position1 = substitutions[i][0]
            position2 = substitutions[i][1]

            # Swap
            temp = ciperAlpha[position1%len(ciperAlpha)]
            ciperAlpha[position1%len(ciperAlpha)] = ciperAlpha[position2%len(ciperAlpha)]
            ciperAlpha[position2%len(ciperAlpha)] = temp



            
        encryptedString = ""
        for i in self.message:
            # If the character is a letter, swap it for it's replacement
            if i.isalpha():
                encryptedString += ciperAlpha[normalAlpha.index(i)]
            else:
                # Add the non-letter character to the string
                encryptedString += i
        return ciphertextMsg(encryptedString)
        
    def playfairCipher(self,key=""):
        playfairAlpha =['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        playfairAlphaCopy = playfairAlpha.copy()
        # Get unique letters in the key
        uniqueString = ""
        key = key.upper()
        for i in key:
            if i.isalpha():
                if i == "J":
                    i == "I"
                if not i in uniqueString:
                    
                    uniqueString += i
        
        # Make the matrix
        matrixSize = 5
        matrix = []
        for i in range(matrixSize):
            currentArray = []
            for j in range(matrixSize):
                # Check to see if there are any letters left in the key
                if len(uniqueString) > 0:
                    # If so, add it first, then remove it 
                    # from the list of remaining letters
                    currentLetter = uniqueString[0]
                    uniqueString = uniqueString[1:]
                    playfairAlpha.remove(currentLetter)
                else:
                    # Otherwise, get the first letter 
                    # in the list of remaining lettters
                    currentLetter = playfairAlpha.pop(0)
                # Add the letter to the temp array
                currentArray.append(currentLetter)
            # add the temp array to the matrix
            matrix.append(currentArray)
        
        # Convert the plaintext to an uppercase string without I's
        plainText = ""
        for i in self.message:
            if i.isalpha():
                if i == "J" or i == 'j':
                    plainText += "I"
                else:
                    plainText += i.upper()
        
        # Creating the letter splits
        spiltLetters = []
        # Check if we have any letters left
        while len(plainText) >= 1:
            # if the letter is the last one left or we have a double letter
            if len(plainText) == 1 or plainText[0] == plainText[1]:
                # Generate a random letter that isn't the same as the first letter
                random_letter = plainText[0]
                while(random_letter == plainText[0]):
                    random_letter = random.choice(playfairAlphaCopy)
                # Add it to the list of splits
                spiltLetters.append((plainText[0],random_letter))
                # Remove it from the text
                plainText = plainText[1:]
            else:
                # If the letters aren't the same, then add them to the split
                spiltLetters.append((plainText[0],plainText[1]))
                plainText = plainText[2:]

        i = 0
        cipherString = ""
        while len(spiltLetters) >= 1:
            # Get the first 2 letters
            currentLetters = spiltLetters.pop(0)
            firstLetter,secondLetter = currentLetters[0],currentLetters[1]

            # Get the rows and cols of the letters
            firstCol, firstRow = indexMatrix(matrix,firstLetter)
            secondCol, secondRow = indexMatrix(matrix,secondLetter)

            # If the cols are the same
            if firstCol == secondCol:
                cipherString += matrix[firstCol][(firstRow + 1) % matrixSize]
                cipherString += matrix[firstCol][(secondRow + 1) % matrixSize]
            
            # if the rows are the same
            elif firstRow == secondRow:
                cipherString += matrix[(firstCol + 1) % matrixSize][firstRow]
                cipherString += matrix[(secondCol + 1) % matrixSize][firstRow]
                
            # if neither of the above are true, then we swap the letters
            # with the letters on the other side of the square 
            else:
                cipherString += matrix[firstCol][secondRow]
                cipherString += matrix[secondCol][firstRow]
                

        return ciphertextMsg(cipherString)

    def caesarCipher(self,shift=0):
        # Get a copy of the alphabet
        normalAlpha = Message.alpha.copy()
        encryptedString = ""
        # Loop the the string
        for i in self.message:
            # if it's a letter, add the shift to the string,
            #  and we modulo it by the len of the alphabet
            # So it wraps around to the front
            if i.isalpha():
                encryptedString += normalAlpha[(normalAlpha.index(i) + shift) % len(normalAlpha)]
            else:
                # If it's not a letter, add the char to the string
                encryptedString += i
        return ciphertextMsg(encryptedString)
    
    def transposition(self,columnSize):
        words = []
        transposition = ""
        # Make an array of (the length of the string) / columsizes
        # Add the letters according to that array
        for i in range(0,len(self.message),columnSize):
            words.append(self.message[i:i+columnSize])
        
        # Loop through the array and,
        # add each row as the strings column,
        # and vice versa
        for i in range(columnSize):
            string = ""
            for j in range(len(words)):
                try:
                    string += words[j][i]
                except IndexError:
                    # If we run out of letters,
                    # add a string
                    string += " "
            transposition += (string)
        return ciphertextMsg(transposition)

class ciphertextMsg(Message):
    def __init__(self, message=""):
        super().__init__(message)
    
    def substitutionCipher(self,substitutions = []):
        normalAlpha = Message.alpha.copy()
        ciperAlpha = Message.alpha.copy()
        # Loop through all substitutions
        for i in range(len(substitutions)):
            # Get the 2 positions
            position1 = substitutions[i][0]
            position2 = substitutions[i][1]

            # Swap
            temp = ciperAlpha[position1%len(ciperAlpha)]
            ciperAlpha[position1%len(ciperAlpha)] = ciperAlpha[position2%len(ciperAlpha)]
            ciperAlpha[position2%len(ciperAlpha)] = temp
        deryptedString = ""
        for i in self.message:
            if i.isalpha():
                deryptedString += normalAlpha[ciperAlpha.index(i)]
            else:
                deryptedString += i
        return plaintextMsg(deryptedString)
        
    def playfairCipher(self,key=""):
        playfairAlpha =['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        playfairAlphaCopy = playfairAlpha.copy()
        
        # Get unique letters in the key
        uniqueString = ""
        key = key.upper()
        for i in key:
            if i.isalpha():
                if i == "J":
                    i == "I"
                if not i in uniqueString:
                    
                    uniqueString += i
        
        # Make the matrix
        matrixSize = 5
        matrix = []
        for i in range(matrixSize):
            currentArray = []
            # Check to see if there are any letters left in the key
            for j in range(matrixSize):
                if len(uniqueString) > 0:
                    # If so, add it first, then remove it 
                    # from the list of remaining letters
                    currentLetter = uniqueString[0]
                    uniqueString = uniqueString[1:]
                    playfairAlpha.remove(currentLetter)
                else:
                    # Otherwise, get the first letter 
                    # in the list of remaining lettters
                    currentLetter = playfairAlpha.pop(0)
                # Add the letter to the temp array
                currentArray.append(currentLetter)
            # add the temp array to the matrix
            matrix.append(currentArray)
        
        cipherText = self.message
        spiltLetters = []
        while len(cipherText) >= 1:
            # if the letter is the last one left or we have a double letter
            if len(cipherText) == 1 or cipherText[0] == cipherText[1]:
                # Generate a random letter that isn't the same as the first letter
                random_letter = cipherText[0]
                while(random_letter == cipherText[0]):
                    random_letter = random.choice(playfairAlphaCopy)
                # Add it to the list of splits
                spiltLetters.append((cipherText[0],random_letter))
                # Remove it from the text
                cipherText = cipherText[1:]
            else:
                # If the letters aren't the same, then add them to the split
                spiltLetters.append((cipherText[0],cipherText[1]))
                cipherText = cipherText[2:]

        i = 0
        plainString = ""
        while len(spiltLetters) >= 1:
            # Get the first 2 letters
            currentLetters = spiltLetters.pop(0)
            # Get the rows and cols of the letters
            firstLetter,secondLetter = currentLetters[0],currentLetters[1]
            firstCol, firstRow = indexMatrix(matrix,firstLetter)
            secondCol, secondRow = indexMatrix(matrix,secondLetter)

            # If the cols are the same
            if firstCol == secondCol:
                plainString += matrix[firstCol][(firstRow - 1) % matrixSize]
                plainString += matrix[firstCol][(secondRow - 1) % matrixSize]
            # if the rows are the same
            elif firstRow == secondRow:
                plainString += matrix[(firstCol - 1) % matrixSize][firstRow]
                plainString += matrix[(secondCol - 1) % matrixSize][firstRow]
                
            # if neither of the above are true, then we swap the letters
            # with the letters on the other side of the square 
            else:
                plainString += matrix[firstCol][secondRow]
                plainString += matrix[secondCol][firstRow]
                

        return plaintextMsg(plainString)

    def caesarCipher(self,shift=0):
        normalAlpha = Message.alpha.copy()
        decryptedString = ""
        # Loop through all the letters
        for i in self.message:
            if i.isalpha():
                # we go the opposite direction of the shift
                # We use modulo to loop back to the end
                decryptedString += normalAlpha[(normalAlpha.index(i) - shift) % len(normalAlpha)]
            else:
                # Otherwise, add the letter
                decryptedString += i
        return plaintextMsg(decryptedString)

    def transposition(self,columnSize):
        loops = int((len(self.message) + columnSize - 1) / columnSize  )
        # Loop through the string, and get each row of the string,
        # and set it as the column
        decrypt = ""
        for i in range(loops):
            for j in range(columnSize):
                decrypt += self.message[i + (j * loops)]
                
        return plaintextMsg(decrypt)

def indexMatrix(matrix, object):
    # Loop through the lists
    for i, x in enumerate(matrix):
        # check if the object is in the current list
        if object in x:
            return i, x.index(object)
    # If not, we send back an error
    return -1

if __name__ == "__main__":


    # Set random keys
    swapsForSub = [(random.randint(0,26),random.randint(0,26)) for _ in range(random.randint(0,100))]
    playfairKey = "THISWORKS"
    caesarShift = random.randint(1,100)
    transCol = random.randint(2,5)
    
    substitutions = []
    caesars = []
    playfairs = []
    transpositions = []

    listOfInputs = []

    # Get inputs
    while True:
        userInput = input("Please Enter the message you would Like to encrypt (type 'Stop' to end the program):\n")
        if userInput.upper() == "STOP":
            break
        
        listOfInputs.append(userInput)
    
    # Output inputs
    print("You entered:")
    for i in range(len(listOfInputs)):
        listOfInputs[i] = plaintextMsg(listOfInputs[i])
        print(listOfInputs[i].getText())

        # Encrypt inputs
        substitutions.append(listOfInputs[i].substitutionCipher(swapsForSub))
        caesars.append(listOfInputs[i].caesarCipher(caesarShift))
        playfairs.append(listOfInputs[i].playfairCipher(playfairKey))
        transpositions.append(listOfInputs[i].transposition(transCol))

    # Print encryption
    for i in range(len(listOfInputs)):
        print("\n" + listOfInputs[i].getText() + " encrypted in:\n")
        print('Substitution Cipher: ' + substitutions[i].getText())
        print("Caesar Cipher: " + caesars[i].getText())
        print("Playfair Cipher: " + playfairs[i].getText())
        print("Transposition: " + transpositions[i].getText())

    # Print decryption
    for i in range(len(listOfInputs)):
        print("\n" + listOfInputs[i].getText() + " decrypted in:\n")
        print('Substitution Cipher: ' + substitutions[i].substitutionCipher(swapsForSub).getText())
        print("Caesar Cipher: " + caesars[i].caesarCipher(caesarShift).getText())
        print("Playfair Cipher: " + playfairs[i].playfairCipher(playfairKey).getText())
        print("Transposition: " + transpositions[i].transposition(transCol).getText())
       
