def insertion(ip_list):
    for i in range(1,len(ip_list)):
        for j in range(i-1,-1,-1):
            if ip_list[j]>ip_list[i]:
                ip_list[j],ip_list[j+1] = ip_list[j+1],ip_list[j]
#or # if ip_list[0]>ip_list[1]:
    #     ip_list[0],ip_list[1]=ip_list[1],ip_list[0]
    return ip_list

if __name__ == "__main__":
    print(insertion([1,2,9,3,5,6,4,8]))