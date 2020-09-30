class BrainFuck:
    """
    memoryCellBitSize --> Bits that can be stored in a single cell, so it can either be 8, 16 or 32
        8bits = 255-MAX_VALUE / 16bits = 65536-MAX_VALUE / 32bits = 4294967296-MAX_VALUE

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
        }

    # +
    def incrementByte(self):
        if(self.memory[self.memoryPosition] < self.memoryCellBitSize):
            self.memory[self.memoryPosition] += 1
        else:
            self.memory[self.memoryPosition] = 0
    # -
    def decrementByte(self):
        if(self.memory[self.memoryPosition] > 0):
            self.memory[self.memoryPosition] -= 1
        else:
            self.memory[self.memoryPosition] = self.memoryCellBitSize
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
            self.memory[self.memoryPosition] = ord(char[0])
        else:
            # if the user press enter, then store 13
            self.memory[self.memoryPosition] = 13

    # .
    def printByte(self):
        char = self.memory[self.memoryPosition]
        result = 'BRAINFUCK COMPILER OUTPUT ---> '
        if(char >= 0 and char <= self.memoryCellBitSize):
            result += chr(char)
        print(result)
    
    # Runs the actual brainfuck code
    def run(self):
        while(self.codePosition < len(self.code)):
            self.do_action[self.code[self.codePosition]]()
            self.codePosition += 1

        print('------------------------------------')
        print('PROGRAM EXECUTION ENDED SUCCESSFULLY')
        print('------------------------------------')
        print('MEMORY:')
        print(self.memory)
        
if __name__ == '__main__':
    BF = BrainFuck(8,10,'>>,.')
    BF.run()

