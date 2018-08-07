class Code:
    def __init__(self):
        pass

    def dest(self, destination):
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

    def comp(self, compare):
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

    def jump(self, jump):
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