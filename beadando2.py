def is_perfect(n: int) -> bool:
    def factor(n: int) -> list:
        factors = [1]
        rem  = n
        for i in range(2,n+1):
            if rem % i == 0:
                rem = rem / i
                factors.append(i)
        return factors
    factors = factor(n)
    return sum(factors) == n


for i in range(1,10):
    if is_perfect(i):
        print("{} tökéletes? {}".format(i, is_perfect(i)))
#print("{} tökéletes? {}".format(12, is_perfect(12)))

while True:
    number = int(input("Adj meg egy egész számot:"))
    print("{} tökéletes? {}".format(number, is_perfect(number)))


