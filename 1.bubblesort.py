def bubble(ip_list):
    for i in range(len(ip_list)-1):
        for j in range(len(ip_list)-1-i):
            if ip_list[j]>ip_list[j+1]:
                ip_list[j],ip_list[j+1] = ip_list[j+1],ip_list[j]
    return ip_list

if __name__ == "__main__":
    print(bubble([2,1,9,3,5,6,4,8]))