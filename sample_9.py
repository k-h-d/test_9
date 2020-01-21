def binary_search(lis,s_item):
    #lis.sort()
    low=0
    high=len(lis)-1
    while low <= high:
        mid=(low+high)//2
        if lis[mid]==s_item:
            print("{0}({1}番目)".format(s_item,mid))
            return
        elif lis[mid]<s_item:
            low=mid+1
        else:
            high=mid-1
    return


if __name__ == '__main__':
    heart_cards = [1, 2, 4, 5, 6, 8, 9, 10, 12, 13]
    heart_eight = 12
    binary_search(heart_cards, heart_eight)
