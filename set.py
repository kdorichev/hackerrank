''' Print second last unique number  '''
if __name__ == '__main__':
    #n = int(input())       number of input numbers is not actually required
    arr = map(int, input().split())
    myset  = set(arr)        # set removed duplicate values
    uniquelist = list(myset) # back to list to sort
    uniquelist.sort()
    print(uniquelist[-2])    # 2nd last
