import Parser
import SymbolTable
import Assembler
import sys

def run():
    print("start", sys.argv[0], "\n")
    asmfile = sys.argv[1]
    if not asmfile.find(".asm"):
        asmfile = asmfile + ".asm"
    hackfile = asmfile[:-4] + ".hack"

    pre_process = SymbolTable.SymbolTable(asmfile)
    while (True):
        if pre_process.process_line():
            pass
        else:
            break

    table = pre_process.table
    print(table)
    pre_process.file.close()

    hack = open(hackfile, "w+")
    file = Parser.Parser(asmfile, table)
    more = file.hasMoreCommands()
    while more != '':
        com_type = file.commandType(more)
        assembler = Assembler.Assembler(more, com_type)
        destination, compare, jump, address = \
            assembler.process_type(more, com_type, file)
        compute = compare + destination + jump
        assembler.write(compute, address, hack)
        more = file.hasMoreCommands()
    hack.seek(0, 0)
    print(hack.read())
    hack.close()
    print("end")


if __name__ == "__main__":
    run()