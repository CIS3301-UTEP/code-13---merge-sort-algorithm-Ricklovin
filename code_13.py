
def merge(half_left,half_right):
    i = 0
    j = 0
    merged_list = []
    while i < len(half_left) and j < len(half_right):
        if half_left[i] < half_right[j]:
            merged_list.append(half_left[i])
            i += 1
        else:merged_list.append(half_right[j])
        
        j += 1
        while i < len(half_left):merged_list.append(half_left[i])
        i += 1
        
        while j < len(half_right):merged_list.append(half_right[j])
        j += 1
        
        return merged_list



def get_merge_sorted_list(unsorted_list):

    if len(unsorted_list) == 1:    
        return unsorted_list
    
    mid = int((len(unsorted_list))//2)

    f_half = unsorted_list[:mid]
    s_half = unsorted_list[mid:]

    half_left = get_merge_sorted_list(f_half)
    half_right = get_merge_sorted_list(s_half)

    return merge(half_left,half_right)

if __name__ == "__main__":

    unsorted_list = [1,2,44,1,2,3,4,7,8,92,34,12,3,4,56,8,89,42,24,5,3]


    print(merge(get_merge_sorted_list(unsorted_list)))