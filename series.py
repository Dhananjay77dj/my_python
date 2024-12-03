def fs(n):
    if n ==1  :
        return 0
    elif n == 2:
        return 1
    
    elif n >2:
        return fs(n -1) + fs(n-2) # this line iss very important to understand
    # example you take 4 now this will be like that -- fs(5-1) + fs(5-2)
    #                                               -- fs(4) + fs(3)
    #                                     now here is fs(4) so it will implies the fs function
    #                                                 -- fs(4-1) + fs(4-2)
    #                                                 -- fs(3)  + fs(2)
    #                                             here it will implies fs(3) = fs(3-1) + fs(3-2)
    #                                                  -- fs(2) + fs(1) + fs(2)
c = fs(5)
print(c)
