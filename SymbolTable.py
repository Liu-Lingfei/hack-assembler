class SymbolTable:
    def __init__(self, file_name):
        self.file = open(file_name, "r")
        self.name = self.file.name
        self.table = {}
        self.lines = 0

    def record(self, command):
        first = command.find("(")
        second = command.find(")")
        if first == -1 or second == -1:
            return False
        symbol = command[(first + 1):second]
        self.table[symbol] = self.lines
        return True

    def read_newline(self):
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

    def process_line(self):
        command = self.read_newline()
        com_type = self.commandType(command)
        if com_type == "L_COMMAND":
            self.record(command)
            return True
        elif com_type == "A_COMMAND" or com_type == "C_COMMAND":
            self.lines += 1
            return True
        elif com_type == "COMMENT":
            return True
        else:
            return False