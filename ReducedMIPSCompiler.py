import os

def decipherIType(trailer):
    trailerComps = trailer.split(',')
    result = format(int(trailerComps[0]), "05b") + format(int(trailerComps[1]), "05b") + format(int(trailerComps[2]), "016b")
    return result
def decipherRType(trailer):
    trailerComps = trailer.split(',')
    result = format(int(trailerComps[1]), "05b") + format(int(trailerComps[2]), "05b") + format(int(trailerComps[0]), "05b")
    return result



if __name__ == '__main__':
    print("Input format: ")
    print("   I-type: op rd,rs,imm")
    print("   R-type: op rd,rs,rt")
    print("   j-type: j addr")

    print("Example input: ")
    print("    lw 0,1,0")
    print("    addu 1,2,3")
    print("    j 14")
    with open('imem.txt', 'w') as outputFile, open('imemHumanReadable.txt', 'w') as outputHFile:
        while True:
            instr = input("Enter a MIPS instruction(Enter 'EXIT' to terminate): ")
            outputHFile.write(instr)
            instrComps = instr.split()
            if instrComps[0].lower() == "exit":
                [outputFile.write("11111111"+os.linesep) for i in range(4)]
                break
            elif instrComps[0].lower() == "jump" or instrComps[0].lower() == "j":
                opcode = "000010"
                jAddr = instrComps[1]
                toWrite = opcode + format(int(jAddr), "026b")


            elif instrComps[0].lower() == "addiu":
                toWrite = "001001"+ decipherIType(instrComps[1])
            elif instrComps[0].lower() == "beq":
                toWrite = "000100" + decipherIType(instrComps[1])
            elif instrComps[0].lower() == "lw":
                toWrite = "100011" + decipherIType(instrComps[1])
            elif instrComps[0].lower() == "sw":
                toWrite = "101011" + decipherIType(instrComps[1])
            elif instrComps[0].lower() == "addu":
                toWrite = "000000" + decipherRType(instrComps[1]) + "00000" + "100001"
            elif instrComps[0].lower() == "subu":
                toWrite = "000000" + decipherRType(instrComps[1]) + "00000" + "100011"
            elif instrComps[0].lower() == "and":
                toWrite = "000000" + decipherRType(instrComps[1]) + "00000" + "100100"
            elif instrComps[0].lower() == "or":
                toWrite = "000000" + decipherRType(instrComps[1]) + "00000" + "100101"
            elif instrComps[0].lower() == "nor":
                toWrite = "000000" + decipherRType(instrComps[1]) + "00000" + "100111"
            else:
                raise ValueError("Invalid command")

            print("Binary: " + toWrite)
            if len(toWrite) == 32:
                [outputFile.write(toWrite[i:i+8]+os.linesep) for i in range(0,31,8)]
            else:
                raise ValueError("wrong length")















