
def merged(half_left,half_right):
    a = 0
    b = 0
    merged_list = []

    for i in range(len(half_left) + len(half_right)):
        if a >= len(half_left):
            merged_list.append(half_right[b])
            b += 1
        elif b >= len(half_right):
            merged_list.append(half_left[a])
            a += 1
        elif half_left[a] < half_right[b]:
            merged_list.append(half_left[a])
            a += 1
        else:
            merged_list.append(half_right[b])
            b += 1
    
    return merged_list

def get_merge_sorted_list(unsorted_list):

    if len(unsorted_list) == 1:    
        return unsorted_list
    
    mid = int((len(unsorted_list))//2)

    f_half = unsorted_list[:mid]
    s_half = unsorted_list[mid:]

    half_left = get_merge_sorted_list(f_half)
    half_right = get_merge_sorted_list(s_half)

    return merged(half_left,half_right)

if __name__ == "__main__":

    unsorted_list = [1,2,1,2,3,7,8,9,1]


    print(get_merge_sorted_list(unsorted_list))