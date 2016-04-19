def find_median(List_1, List_2):
    l = List_1+List_2
    l.sort()
    if len(l) % 2 == 0:
        return l[len(l)//2-1], sorted(l)
    return l[(len(l)-1)//2], sorted(l)


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
