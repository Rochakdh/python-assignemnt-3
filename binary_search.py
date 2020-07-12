def binary_search(ip_list, x): 
    low = 0
    high = len(ip_list) - 1
    mid = 0
    while low <= high: 
        mid = (high + low) // 2
        if ip_list[mid] < x: 
            low = mid + 1
        elif ip_list[mid] > x: 
            high = mid - 1
        else: 
            return True
    return False
if __name__ == "__main__":
    print(binary_search([1,2,3,4,5],9))