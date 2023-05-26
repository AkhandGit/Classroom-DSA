
'''
Given a number n, print 1-n.


def print_numbers(n):
    if n <= 0:
        return
    print_numbers(n-1)
    print(n)

n = int(input("Enter the value of n: "))
print("Numbers are:")
print_numbers(n)

'''


'''
Given a number n, print n-1.


def print_numbers(n):
  if n > 0:
    print(n) 
    print_numbers(n-1)


n = int(input("Enter a number: "))
print_numbers(n)



'''



'''
Given an array print array.

def print_array(arr, i):
    if i == len(arr):
        return
    print(arr[i])
    print_array(arr, i+1)

arr = [1, 2, 3, 4, 5]
print_array(arr, 0)

'''

'''
Print the array in reverse.

def reverse(arr, i):
    if i < 0:
        return
    print(arr[i])
    reverse(arr, i-1)

arr = [1, 2, 3, 4, 5]
reverse(arr, len(arr)-1)


'''

'''

Find the maximum of an array.

def max(arr, i):

    if i == 0:
        return arr[0]

    return max(arr[i], max(arr, i-1))

arr = [5, 9, 3, 7, 2]

max_val = max(arr, len(arr)-1)

print("Maximum Value:", max_val)


'''