
def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Sides must be positive")

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle")

    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"




def course_result(coursework, final, attendance):
    if not (0 <= coursework <= 40):
        raise ValueError("Invalid coursework")

    if not (0 <= final <= 60):
        raise ValueError("Invalid final")

    if not (0 <= attendance <= 100):
        raise ValueError("Invalid attendance")

    if attendance < 75:
        return "barred"
    elif final < 18:
        return "fail"
    elif coursework + final < 60:
        return "fail"
    else:
        return "pass"




def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))

    return result




def is_prime(n):
    if n < 2:
        return False

    divisor = 2

    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1

    return True




def primes_below(n):
    result = []

    for i in range(2, n):
        if is_prime(i):
            result.append(i)

    return result




def first_repeated(values):
    for i in range(len(values)):
        for j in range(i):
            if values[i] == values[j]:
                return values[i]

    return None




def count_pairs(n):
    return n * (n - 1) // 2




def calculator(command):
    parts = command.split()

    try:
        match parts:
            case ["add", a, b]:
                return int(a) + int(b)

            case ["mul", a, b]:
                return int(a) * int(b)

            case ["neg", a]:
                return -int(a)

            case ["sum", *numbers] if len(numbers) >= 1:
                total = 0
                for number in numbers:
                    total += int(number)
                return total

            case _:
                raise ValueError("Invalid command")

    except ValueError:
        raise ValueError("Invalid command")




def parse_int(text, default=None):
    try:
        return int(text)
    except ValueError:
        return default




def stats(*numbers):
    if len(numbers) == 0:
        raise ValueError("At least one number is required")

    smallest = numbers[0]
    largest = numbers[0]
    total = 0

    for number in numbers:
        if number < smallest:
            smallest = number

        if number > largest:
            largest = number

        total += number

    mean = total / len(numbers)

    return smallest, largest, mean




def append_to(item, target=None):
    if target is None:
        target = []

    target.append(item)
    return target




def make_multiplier(k):
    def multiply(x):
        return x * k

    return multiply




def apply_n(f, x, n):
    result = x

    for i in range(n):
        result = f(result)

    return result
