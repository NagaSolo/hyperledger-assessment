"""
Question 1b

"""
def factorial(n):
    # check if the number is negative
    if num < 0:
        print('error')
    elif num == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    num = 100

    # SUM is built-in
    # res = sum(int(i) for i in str(factorial(num)))
    # print(res)

    res = 0
    for i in str(factorial(num)):
        res += int(i)
    print(res)