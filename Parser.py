class Code():
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
            return '000'
        destination = command[: index]
        if destination == '' or destination == "null":
            value = "000"
        elif destination == "M":
            value = "001"
        elif destination == "D":
            value = "010"
        elif destination == "MD":
            value = "011"
        elif destination == "A":
            value = "100"
        elif destination == "AM":
            value = "101"
        elif destination == "AD":
            value = "110"
        elif destination == "AMD":
            value = "111"
        else:
            value = "shit"

        return value

    def comp(self, command):
        index_equ = command.find("=")
        index_col = command.find(";")
        if index_col == -1:
            compare = command[(index_equ + 1):]
        else:
            compare = command[(index_equ + 1): index_col]

        if compare == "0":
            value = "0101010"
        elif compare == "1":
            value = "0111111"
        elif compare == "-1":
            value = "0111010"
        elif compare == "D":
            value = "0001100"
        elif compare == "A":
            value = "0110000"
        elif compare == "!D":
            value = "0001101"
        elif compare == "!A":
            value = "0110001"
        elif compare == "-D":
            value = "0001111"
        elif compare == "-A":
            value = "0110011"
        elif compare == "D+1":
            value = "0011111"
        elif compare == "A+1":
            value = "0110111"
        elif compare == "D-1":
            value = "0001110"
        elif compare == "A-1":
            value = "0110010"
        elif compare == "D+A" or compare == "A+D":
            value = "0000010"
        elif compare == "D-A":
            value = "0010011"
        elif compare == "A-D":
            value = "0000111"
        elif compare == "D&A" or compare == "A&D":
            value = "0000000"
        elif compare == "D|A" or compare == "A|D":
            value = "0010101"

        elif compare == "M":
            value = "1110000"
        elif compare == "!M":
            value = "1110001"
        elif compare == "-M":
            value = "1110011"
        elif compare == "M+1":
            value = "1110111"
        elif compare == "M-1":
            value = "1110010"
        elif compare == "D+M" or compare == "M+D":
            value = "1000010"
        elif compare == "D-M":
            value = "1010011"
        elif compare == "M-D":
            value = "1000111"
        elif compare == "D&M" or compare == "M&D":
            value = "1000000"
        elif compare == "D|M" or compare == "M|D":
            value = "1010101"
        else:
            value = "fuck"
        return value

    def jump(self, command):
        index = command.find(";")
        if index == -1:
            jump = ''
        else:
            jump = command[(index + 1):]

        if jump == '' or jump == "null":
            value = '000'
        elif jump == "JGT":
            value = "001"
        elif jump == "JEQ":
            value = "010"
        elif jump == "JGE":
            value = "011"
        elif jump == "JLT":
            value = "100"
        elif jump == "JNE":
            value = "101"
        elif jump == "JLE":
            value = "110"
        elif jump == "JMP":
            value = "111"
        else:
            value = "shit"
        return value

    def process_type(self, command, com_type):
        if com_type == 'C_COMMAND':
            compare = self.comp(command)
            destination = self.dest(command)
            jump = self.jump(command)
            address = ''
        elif com_type == 'A_COMMAND':
            compare = ''
            destination = ''
            jump = ''
            address = self.symbol(command)
        else:
            compare = ''
            destination = ''
            jump = ''
            address = ''
        return compare, destination, jump, address