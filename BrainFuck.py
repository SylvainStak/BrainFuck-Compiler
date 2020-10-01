class BrainFuck:
    """
    memoryCellBitSize --> Bits that can be stored in a single cell, so it can either be 8, 16 or 32
        8bits = (2^8)-1 --> 255 | 16bits = (2^16)-1 --> 65535 | 32bits = (2^32)-1 --> 4294967295

    memoryLength --> Number of cells available to be used, each of the size specified in memoryCellBitSize
    """
    def __init__(self, memoryCellBitSize, memoryLength, code):
        # Array that stores the memory of the program instance
        self.memory = [0]*memoryLength

        # Maximum value that can be stored in a cell
        self.memoryCellBitSize = 2**memoryCellBitSize-1

        # Position of the main pointer that keeps track of the program execution
        self.memoryPosition = 0
        
        # Position of the analyzed character in the given code as a string
        self.codePosition = 0
        
        # Actual code in brainfuck to compile
        self.code = code

        # Dictionary that matches each valid character with its function
        self.do_action = {
            '+': self.incrementByte,
            '-': self.decrementByte,
            '>': self.incrementPointer,
            '<': self.decrementPointer,
            ',': self.readByte,  
            '.': self.printByte,
            '[': self.jumpNext,
            ']': self.jumpPrevious,
        }

    # +
    def incrementByte(self):
        if(self.getPointerValue() < self.memoryCellBitSize):
            self.updatePointerValue(self.getPointerValue()+1)
        else:
            self.updatePointerValue(0)
    # -
    def decrementByte(self):
        if(self.getPointerValue() > 0):
            self.updatePointerValue(self.getPointerValue()-1)
        else:
            self.updatePointerValue(self.memoryCellBitSize)
    # >
    def incrementPointer(self):
        if(self.memoryPosition < len(self.memory)-1):
            self.memoryPosition += 1
        else:
            self.memoryPosition = 0

    # <
    def decrementPointer(self):
        if(self.memoryPosition > 0):
            self.memoryPosition -= 1
        else:
            self.memoryPosition = len(self.memory)-1

    # ,
    def readByte(self):
        char = input('Insert a value (only the first character will be taken in count): ')
        if(len(char) > 0):
            # save the user input as an ascii value
            self.updatePointerValue(ord(char[0]))
        else:
            # if the user press enter, then store 13
            self.updatePointerValue(13)

    # .
    def printByte(self):
        char = self.getPointerValue()
        result = 'BRAINFUCK COMPILER OUTPUT ---> '
        if(char >= 0 and char <= self.memoryCellBitSize):
            result += chr(char)
        print(result)

    # [
    def jumpNext(self):
        if(self.getPointerValue() == 0):
            while(self.getActualCodeChar() != ']'):
                self.codePosition += 1
            # jump to the character at the right of matching bracket
            self.codePosition += 1


    # ]
    def jumpPrevious(self):
        if(self.getPointerValue() == 0):
            while(self.getActualCodeChar() != '['):
                self.codePosition -= 1
            # jump to the character at the right of matching bracket
            self.codePosition += 1

    # Set new value to actual pointer
    def updatePointerValue(self, value):
        self.memory[self.memoryPosition] = value
    
    # Get the value from the actual pointer
    def getPointerValue(self):
        return self.memory[self.memoryPosition]

    # Get the actual character from the code
    def getActualCodeChar(self):
        return self.code[self.codePosition]

    # Runs the actual brainfuck code
    def run(self):
        while(self.codePosition < len(self.code)):
            self.do_action[self.getActualCodeChar()]()
            self.codePosition += 1

        print('------------------------------------')
        print('PROGRAM EXECUTION ENDED SUCCESSFULLY')
        print('------------------------------------')
        print('MEMORY:')
        print(self.memory)
        
if __name__ == '__main__':
    BF = BrainFuck(8,10,'+>++>+++>++++>')
    BF.run()

