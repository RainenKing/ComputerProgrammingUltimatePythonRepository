def make_abc():
    result = ["a", "b", "c"]
    return result

print("make the abc:")
print(make_abc())



def equal_edges(items):
    first = items[0]
    last = items [-1]
    
    if first == last:
        return True
    else:
        return False

print(equal_edges([9, 6, 7, 5, 9]))
print(equal_edges([9, 6, 7, 5, 4]))



def common_edge(list1, list2):
    first1 = list1[0]
    first2 = list2[0]
    last1 = list1[2]
    last2 = list2[2]

    if first1 or last1 == first2 or last2:
        return True
    else:
        return False
    


def all_the_same(list1):
    first = list1[0]
    middle = list1[1]
    last = list1[2]

    if first == middle and first == last:
        return True
    else:
        return False


print(all_the_same([9, 9, 9]))
print(all_the_same([4, 7, 4]))



def all_unique(list1):
    first = list1[0]
    middle = list1[1]
    last = list1[2]





