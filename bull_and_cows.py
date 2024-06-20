import random


def get_bulls_and_cows(secret: str, guess: str):
    if len(secret) != len(guess):
        raise ValueError("diffeent lenghts")

    cows = 0
    bulls = 0

    secret_without_bulls = []
    guess_without_bulls = []
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1
        else:
            secret_without_bulls.append(secret[i])
            guess_without_bulls.append(guess[i])

    for char in guess_without_bulls:
        if char in secret_without_bulls:
            cows += 1
            secret_without_bulls.remove(char)

    return {'bulls': bulls, "cows": cows}


def generate_random_number(length):
    result = ""
    for _ in range(5):
        n = random.randint(0, 9)
        result += str(n)
    return result


if __name__ == '__main__':
    print(generate_random_number(5))
