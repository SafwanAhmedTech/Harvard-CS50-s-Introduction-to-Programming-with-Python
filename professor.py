import random


def main():
    level = get_level()
    score = 0
    for n in range(10):
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        answer = num1 + num2
        tries = 0
        while True:
            try:
                user_answer = int(input(f'{num1} + {num2} = '))
            except ValueError:
                tries += 1
                print('EEE')
                if tries == 3:
                    print(answer)
                    break
                continue
            else:
                if user_answer == answer:
                    score += 1
                    tries = 0
                    break
                else:
                    tries += 1
                    print('EEE')
                    if tries == 3:
                        print(answer)
                        break
                    continue

    print(f'Score: {score}')


def get_level():
    while True:
        try:
            level = int(input('level: '))
        except ValueError:
            continue
        else:
            if 1 <= level <= 3:
                return level



def generate_integer(level):
        if level == 1:
            start = 0
        else:
            start = 10**(level - 1)
        end = (10**level) - 1
        num = random.randint(start, end)
        return num





if __name__ == "__main__":
    main()
