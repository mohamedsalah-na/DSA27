def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60

    return f"{hours}:{minutes:02d}:{remaining_seconds:02d}"




def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return round(fahrenheit, 1)




def split_evenly(total, people):
    share = total // people
    left_over = total % people

    return share, left_over




def initials(full_name):
    words = full_name.split()
    result = ""
    i = 0

    while i < len(words):
        result += words[i][0].upper() + "."
        i += 1

    return result




def is_palindrome_word(word):
    word = word.strip().lower()
    return word == word[::-1]




def mask_email(email):
    at = email.index("@")
    name = email[:at]
    domain = email[at:]

    if len(name) <= 2:
        return email

    return name[0] + "*" * (len(name) - 2) + name[-1] + domain




def middle(values):
    n = len(values)
    return values[(n - 1) // 2:(n + 2) // 2]




def rotate_left(values, k):
    if len(values) == 0:
        return []

    k = k % len(values)

    return values[k:] + values[:k]




def fib_list(n):
    result = []
    a = 0
    b = 1
    i = 0

    while i < n:
        result.append(a)
        a, b = b, a + b
        i += 1

    return result




def collatz_steps(n):
    steps = 0

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        steps += 1

    return steps