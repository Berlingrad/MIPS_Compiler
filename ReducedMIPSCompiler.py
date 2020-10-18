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
    print("""
    Input format: 
       I-type: op rt,rs,imm
       R-type: op rd,rs,rt
       j-type: j addr
    """
          )
    print("""
    Example input:
        lw 0,1,0
        addu 1,2,3
        j 14
    """
          )
    with open('imem.txt', 'w') as outputFile, open('imemHumanReadable.txt', 'w') as outputHFile:
        while True:
            instr = input("Enter a MIPS instruction(Enter 'EXIT' to terminate): ")
            outputHFile.write(instr+os.linesep*4)
            instrComps = instr.split()
            if instrComps[0].lower().strip() == "exit":
                [outputFile.write("11111111"+os.linesep) for i in range(4)]
                break
            elif instrComps[0].lower().strip() == "jump" or instrComps[0].lower().strip() == "j":
                opcode = "000010"
                jAddr = instrComps[1]
                toWrite = opcode + format(int(jAddr), "026b")


            elif instrComps[0].lower().strip() == "addiu":
                toWrite = "001001"+ decipherIType(instrComps[1])
            elif instrComps[0].lower().strip() == "beq":
                toWrite = "000100" + decipherIType(instrComps[1])
            elif instrComps[0].lower().strip() == "lw":
                toWrite = "100011" + decipherIType(instrComps[1])
            elif instrComps[0].lower().strip() == "sw":
                toWrite = "101011" + decipherIType(instrComps[1])
            elif instrComps[0].lower().strip() == "addu":
                toWrite = "000000" + decipherRType(instrComps[1]) + "00000" + "100001"
            elif instrComps[0].lower().strip() == "subu":
                toWrite = "000000" + decipherRType(instrComps[1]) + "00000" + "100011"
            elif instrComps[0].lower().strip() == "and":
                toWrite = "000000" + decipherRType(instrComps[1]) + "00000" + "100100"
            elif instrComps[0].lower().strip() == "or":
                toWrite = "000000" + decipherRType(instrComps[1]) + "00000" + "100101"
            elif instrComps[0].lower().strip() == "nor":
                toWrite = "000000" + decipherRType(instrComps[1]) + "00000" + "100111"
            else:
                raise ValueError("Invalid command")

            print("Binary: " + toWrite)
            if len(toWrite) == 32:
                [outputFile.write(toWrite[i:i+8]+os.linesep) for i in range(0,31,8)]
            else:
                raise ValueError("wrong length")















