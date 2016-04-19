import sys

if __name__ == '__main__':
    try:
        with open(sys.argv[1], 'r') as myfile:
            content = myfile.readlines()
        print(content[0], end="")
        for i in range(1,len(content)):
            l = content[i].split()
            tot = 0
            c = 0
            note = ""
            for num in l:
                try:
                    tot += int(num)
                    c += 1
                except ValueError:
                    note += " "+num
            avg = tot/c
            print("{:.3f}".format(avg)+note)

    except IOError as e:
        print(sys.argv[1], "is not a readable file.")
    except IndexError:
        print("Usage: parse.py [filename]")

