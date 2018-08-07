import Parser
import SymbolTable
import Code

class Assembler:
    def __init__(self, command, command_type):
        self.command = command
        self.command_type = command_type


    def process_type(self, command, com_type, parser):
        code_translator = Code.Code()
        if com_type == 'C_COMMAND':
            destination = parser.dest(command)
            dest_code = code_translator.dest(destination)
            compare = parser.comp(command)
            comp_code = code_translator.comp(compare)
            jump = parser.jump(command)
            jump_code = code_translator.jump(jump)
            address = ''
        elif com_type == 'A_COMMAND':
            dest_code = ""
            comp_code = ""
            jump_code = ""
            address = parser.symbol(command)
        else:
            dest_code = ""
            comp_code = ""
            jump_code = ""
            address = ''

        return dest_code, comp_code, jump_code, address

    def write(self, compute, address, file):
        if compute != '':
            compute = '111' + compute
        if compute != '':
            file.write(compute + '\n')
        elif address != '':
            file.write(address + '\n')
        else:
            pass
