#  How to create a def t0 find the average os n numbers
def avg(*numbers):
    total = sum(numbers)
    average = total / len(numbers)
    print(average)
avg(2,3,4)
#  here the operator * playes a significant role. Iss star ko lagane se ham function "avg" ko ye baata rahe hai ki ham numbers 
# ko ek ya ek se jaada bhi input kara sakte hain .

# def ap(*no):
#     a = no[0]
#     d= no[1] - no[0]
#     n = len(no)
#     S_n = (n/2)  * [2*a + (n-1)*d]    in this the brackets are problem
#     print(S_n)
# ap(1,2,3,4,5,6,7,8,9)
def ap(*no):
    a = no[0]
    d = no[1] - no[0]
    n = len(no)
    S_n = (n / 2) * (2 * a + (n - 1) * d)
    print(S_n)

ap(1, 2, 3, 4, 5, 6, 7, 8, 9)
