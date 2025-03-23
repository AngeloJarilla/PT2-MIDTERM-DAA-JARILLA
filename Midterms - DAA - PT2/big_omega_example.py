def big_omega_example(arr, target):
    if arr[0] == target:
        return True
    for i in range(1, len(arr)):  
        if arr[i] == target:
            return True
    return False
	