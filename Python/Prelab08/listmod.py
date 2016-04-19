from lists import *

if __name__ == '__main__':
    fir = map(int, input("Enter the first list of numbers: ").split())
    sec = map(int, input("Enter the first list of numbers: ").split())
    fl = list(fir)
    sl = list(sec)
    print("First list: ", fl)
    print("Second list: ", sl)
    (Median, Sorted_List) = find_median(fl, sl)
    print("Merged list: ", Sorted_List)
    print("Median: ", Median)