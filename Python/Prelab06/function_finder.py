import re, sys, os

def finder(filename):
    r1 = re.compile(r"def\s+(?P<func>[a-zA-Z]\w*)\s*\((?P<args>[\w=\-,\s]+)\)")
    r2 = re.compile(r"\s*,\s*")
    with open(filename, 'r') as myfile:
        content = myfile.readlines()
    for line in content:
        l = r1.match(line)
        if l is not None:
            print(l.group("func"))
            args = l.group("args")
            arg_l = r2.split(args)
            for i in range(len(arg_l)):
                print("Arg"+str(i+1)+": "+arg_l[i])

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if os.access(sys.argv[1], os.R_OK):
            finder(sys.argv[1])
        else:
            print(sys.argv[1] + " is not readable")
    else:
        print("usage: function_finder.py filename")
