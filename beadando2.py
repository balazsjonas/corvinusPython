def is_perfect(n: int) -> bool:
    def get_divisors(n: int) -> list:
        divisors = [1]
        for i in range(2, n):
            if n % i == 0:
                divisors.append(i)
        return divisors
    divisors = get_divisors(n)
    return sum(divisors) == n


assert is_perfect(6)
assert is_perfect(28)
assert is_perfect(496)

for i in range(1,10):
    if is_perfect(i):
        print("{} tökéletes? {}".format(i, is_perfect(i)))
#print("{} tökéletes? {}".format(12, is_perfect(12)))

while True:
    number = int(input("Adj meg egy egész számot:"))
    print("{} tökéletes? {}".format(number, is_perfect(number)))


