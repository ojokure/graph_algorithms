


def merge_sorted_list(l1, l2):

    # have a pointer keep track of the position/elements 
    # in the 2 lists

    p1 = 0
    p2 = 0
    merged = []

    while p1 < len(l1) and p2 < len(l2):
        if l1[p1] < l2[p2]:
            merged.append(l1[p1])
            p1 += 1
        
        else:
            merged.append(l2[p2])
            p2 += 1

    if p1 < len(l1):
        while p1 < len(l1):
            merged.append(l1[p1])
            p1 += 1

    if p2 < len(l2):
        while p2 < len(l2):
            merged.append(l2[p2])
            p2 += 1
         


    return merged


la = [ 2, 4, 6, 7, 10, 12, 15, 18]
lb = [ 2, 5, 9, 11]


print(merge_sorted_list(la, lb))


