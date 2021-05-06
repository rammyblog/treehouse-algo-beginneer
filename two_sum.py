def find_sum(arr, target):
    for num in arr:
        diff = abs(target-num)
        if diff in arr and arr.count(diff)>1:
            return num, diff
    else:
        return None


print(find_sum([1,2,3,4,5], 10))
