def linear_search(ip_list,n): 
    for i in range(len(ip_list)): 
        if ip_list[i] == n: 
            return True
    return False

if __name__ == "__main__":
    print(linear_search([1,2,3,4,5],3))
    
