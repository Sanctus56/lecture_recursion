
def recursive_nth_fibo(n):
    if n == 0:
        return n
    elif n == 1:
        return 1
    else:
        return recursive_nth_fibo(n - 1) + recursive_nth_fibo(n - 2)



def main():
    pass


if __name__ == "__main__":
    print(recursive_nth_fibo(9))
    main()
