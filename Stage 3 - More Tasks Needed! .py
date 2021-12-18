import random

def random_task():
    operands = ['+', '-', '*']
    operand = random.choice(operands)
    x = random.randint(2, 9)
    y = random.randint(2, 9)
    return [x, operand, y]


def get_user_answer():
    while True:
        try:
            return int(input())
        except ValueError:
            print("Incorrect format.")


def answer(x, operand, y):
    if operand == '+':
        return x + y
    elif operand == '-':
        return x - y
    elif operand == '*':
        return x * y


def check_answer(ans, res):
    global correct_answers

    if ans == res:
        print('Right!')
        correct_answers += 1

    else:
        print('Wrong')

correct_answers = 0
for _ in range(5):
    task = random_task()
    print(*task)
    user_answer = get_user_answer()
    check_answer(user_answer, answer(*task))


print(f"Your mark is {correct_answers}/5.")