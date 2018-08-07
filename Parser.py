class Parser():
    def __init__(self, file_name, table):
        self.file = open(file_name, "r")
        self.name = self.file.name
        self.table = {"SP": 0, "LCL":1 , "ARG": 2, "THIS": 3, "THAT": 4,
                      "R0": 0, "R1": 1, "R2": 2, "R3": 3, "R4": 4, "R5": 5, "R6": 6, "R7": 7,
                      "R8": 8, "R9": 9, "R10": 10, "R11": 11, "R12": 12, "R13": 13, "R14": 14, "R15": 15,
                      "SCREEN": 16384, "KBD": 24576}
        self.othertable = table
        self.num = 16

    def hasMoreCommands(self):
        command = self.file.readline()
        if command != '' and command.strip() == '':
            return '...'
        command = command.strip()
        index = command.find("//")
        if index == -1:
            pass
        elif index != 0:
            command = command[:index]
        command = command.strip()
        return command

    def commandType(self, command):
        if command == '':
            return False
        elif command[0] == "@":
            return "A_COMMAND"
        elif command[0] == "(":
            return "L_COMMAND"
        elif command[0].isupper() or command[0] == '0' or command[0] == '1' or command[0] == '-1':
            return "C_COMMAND"
        else:
            return "COMMENT"

    def symbol(self, command):
        command = command.strip("@")
        if command.isdigit():
            digit = int(command)
            binary = bin(digit)
        elif command in self.table:
            digit = self.table[command]
            binary = bin(digit)
        elif command in self.othertable:
            digit = self.othertable[command]
            binary = bin(digit)
        else:
            binary = bin(self.num)
            self.othertable[command] = self.num
            self.num += 1
        result = (binary[2:]).zfill(16)
        return result

    def dest(self, command):
        index = command.find("=")
        if index == -1:
            return ''
        destination = command[: index]

        return destination

    def comp(self, command):
        index_equ = command.find("=")
        index_col = command.find(";")
        if index_col == -1:
            compare = command[(index_equ + 1):]
        else:
            compare = command[(index_equ + 1): index_col]

        return compare


    def jump(self, command):
        index = command.find(";")
        if index == -1:
            jump = ''
        else:
            jump = command[(index + 1):]

        return jump
