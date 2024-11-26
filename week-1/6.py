"""
A just graduated Software Engineer wants to buy his dream Laptop which costs x DKK. He has y
DKK saved up, but it is not enough to buy the laptop, so he decides to put the money in an
investment. Every lucky week his money is increasing with the basic interest rate which is 5%.
Every unlucky week the interest rate becomes -3%. Every 4th week is an unlucky week. So the
first week he has his savings as a base in the investment, the second week he has the increased
amount as a base in the investment. Write a program which counts how many weeks does he
need to invest his money to get the dream laptop.

Input
The input line contains 2 integers x, y, where x, y > 0 (x: price of the laptop, y: saved money)

Output
The output writes the number of weeks needed in the investment.
"""

def savings(x, y):
    weeks = 0

    while y < x:
        if weeks%4 != 0:
            y += (y*0.05)
        elif weeks%4 == 0 and weeks > 1:
            y += (y*(-0.03))

        if y < x:
            weeks += 1

    return weeks

print(savings(100, 81))
print(savings(1000, 1000))
print(savings(9876, 5432))
print(savings(10000, 9999))
print(savings(18000, 7800))
