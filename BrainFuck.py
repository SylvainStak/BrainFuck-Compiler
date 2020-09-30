class BrainFuck:
    """
    memoryCellBitSize --> Bits that can be stored in a single cell, so it can either be 8, 16 or 32
        8bits = 255-MAX_VALUE / 16bits = 65536-MAX_VALUE / 32bits = 4294967296-MAX_VALUE

    memoryLength --> Number of cells available to be used, each of the size specified in memoryCellBitSize
    """
    def __init__(self, memoryCellBitSize, memoryLength, code):
        # Array that stores the memory of the program instance
        self.memory = [0]*memoryLength

        # Size of each cell
        self.memoryCellBitSize = memoryCellBitSize

        # Position of the main pointer that keeps track of the program execution
        self.memoryPosition = 0
        
        # Position of the analyzed character in the given code as a string
        self.codePosition = 0
        
        # actual code in brainfuck to compile
        self.code = code

        # dictionary that matches each valid character with its function
        self.do_action = {
            '+': self.incrementByte,
            '-': self.decrementByte,
            '>': self.incrementPointer,
            '<': self.decrementPointer,
        }

    # +
    def incrementByte(self):
        # (2**self.memoryCellBitSize)-1 --> Max value that can be stored in a cell
        if(self.memory[self.memoryPosition] < (2**self.memoryCellBitSize)-1):
            self.memory[self.memoryPosition] += 1
        else:
            self.memory[self.memoryPosition] = 0
    # -
    def decrementByte(self):
        # (2**self.memoryCellBitSize)-1 --> Max value that can be stored in a cell
        if(self.memory[self.memoryPosition] > 0):
            self.memory[self.memoryPosition] -= 1
        else:
            self.memory[self.memoryPosition] = (2**self.memoryCellBitSize)-1
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

    def run(self):
        while(self.codePosition < len(self.code)):
            self.do_action[self.code[self.codePosition]]()
            self.codePosition += 1
        
        print('codePosition --> ' + str(self.codePosition))
        print('memory --> ' + str(self.memory))
        print('memoryPosition --> ' + str(self.memoryPosition))

