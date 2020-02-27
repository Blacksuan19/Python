class Caesar():
    """cypher and decypher caeser's cipher """

    alphabets = 26 # number of alphabets so we wont go above it

    def docipher(self, message, shiftAmount, operation):
        """cypher a given message with agiven amount of shift vlue

        message: the message to cypher
        shiftAmount: a value to shift by (will be % number of alphabets)
        operation: 1 for cypher and 0 for decypher
        """

        results = ""
        for char in message:
            asciirep = ord(char) # get ascii represenation
            if operation == 1: # cypher
                if char.isupper():
                    asciirep = (asciirep + shiftAmount - 65) % self.alphabets + 65
                else:
                    asciirep = (asciirep + shiftAmount - 97) % self.alphabets + 97
            else: # decypher
                if char.isupper():
                    asciirep = (asciirep - shiftAmount - 65) % self.alphabets + 65
                else:
                    asciirep = (asciirep - shiftAmount - 97) % self.alphabets + 97

            results += chr(asciirep) # back to char and add to results
        return results

if __name__ == "__main__":
    caeser = Caesar() # instanciate the class
    string = input("Enter string: ")
    shift = int(input("Enter shift amount: "))
    operation = int(input("Enter Operation to perform(1 = cypher, 0 = decypher): "))
    if type(operation) != int:
        raise TypeError("operation has to 1 or 0")
    print("String: ", string)
    print("Shift Amount: ", shift)
    print("Operation: " + "Cypher" if(operation == 1) else "Decypher")
    print("Result: ", caeser.docipher(string, shift, operation))
