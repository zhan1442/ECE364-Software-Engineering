from HardwareTasks import *

def verilog2vhdl(line):
    try:
        elements = list(processLine(line))
        s = elements[1]+": "+elements[0]+" PORT MAP("
        con = list(elements[2])
        for i in con:
            wn, cn = i
            s += wn+"=>"+cn+", "
        return s[0:-2] + ');'
    except ValueError:
        return "Error: Bad Line."

def convertNetlist(src,des):
    with open(src, 'r') as myfile:
        content = myfile.readlines()
    s = ""
    for line in content:
        s += verilog2vhdl(line) + "\n"
    s = s[0:-1]
    with open(des, 'w') as myfile:
        myfile.write(s)




