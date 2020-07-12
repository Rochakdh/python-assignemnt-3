def interpolation_search(arr, x): 
    lo = 0
    n = len(arr)
    hi = (n - 1) 
    while lo <= hi and x >= arr[lo] and x <= arr[hi]: 
        if lo == hi: 
            if arr[lo] == x:  
                return True; 
            return False;  
        pos  = lo + int(((float(hi - lo) / ( arr[hi] - arr[lo])) * ( x - arr[lo]))) 
  
        if arr[pos] == x: 
            return True 
        if arr[pos] < x: 
            lo = pos + 1; 
        else: 
            hi = pos - 1; 
    return False
  
 
if __name__ == "__main__":
    print(interpolation_search([1,2,3,4,5],3))