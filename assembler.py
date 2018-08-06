import Parser
import SymbolTable


def write(compute, address, file):
    if compute != '':
        compute = '111' + compute
    if compute != '':
        file.write(compute + '\n')
    elif address != '':
        file.write(address + '\n')
    else:
        pass

if __name__ == '__main__':
    print("start\n")
    asmfile = "Rect.asm"
    hackfile = asmfile[:-4] + ".hack"

    pre_process = SymbolTable.SymbolTable(asmfile)
    while (True):
        if pre_process.process_line():
            pass
        else:
            break

    table = pre_process.table
    pre_process.file.close()

    hack = open(hackfile, "w+")
    file = Parser.Code(asmfile, table)
    more = file.hasMoreCommands()
    while more != '':
        com_type = file.commandType(more)
        compare, destination, jump, address = file.process_type(more, com_type)
        compute = compare + destination + jump
        write(compute, address, hack)
        more = file.hasMoreCommands()
    hack.seek(0, 0)
    print(hack.read())
    hack.close()
    print("end")