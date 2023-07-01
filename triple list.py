number=list(map(int,input('Enter a list :').split()))
def triple(x):
    return 3*x
triple_list=map(triple,number)
print('Triple list is :',list(triple_list))

# output
#
# Enter a list :1 2 3 4 5 6 7
# Triple list is : [3, 6, 9, 12, 15, 18, 21]
