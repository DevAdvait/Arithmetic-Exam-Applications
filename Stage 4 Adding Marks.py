#import random module
import random

#function to ask level
def ask_level():
    while True:
        user_input = input("Which level do you want? Enter a number:\n"
                           "1 - simple operations with numbers 2-9\n"
                           "2 - integral squares 11-29\n")
        if user_input in ('1', '2'):
            return user_input
        else:
            print('Incorrect format.')
            continue

#function to generate a equation
def random_task():
    operands = ['+', '-', '*']
    operand = random.choice(operands)
    x = random.randint(2, 9)
    y = random.randint(2, 9)
    return [x, operand, y]

#function to get user's answer for the equation
def get_user_answer():
    while True:
        try:
            return int(input())
        except ValueError:
            print("Incorrect format.")

#func to calculate the answer
def answer(x, operand, y):
    if operand == '+':
        return x + y
    elif operand == '-':
        return x - y
    elif operand == '*':
        return x * y

#func to check correct answer to user answer
def check_answer(ans, res):
    global correct_answers
    if ans == res:
        print('Right!')
        correct_answers += 1
    else:
        print('Wrong')

#func to save results
def save_results():
    name = input('What is your name?\n')
    file = open('results.txt', 'a')
    file.write(f'{name}: {correct_answers}/5 in level {level} ({levels[level]}).\n')
    file.close()
    print('The results are saved in "results.txt".')

#Initial Display
levels = {'1': 'simple operations with numbers 2-9',
          '2': 'integral squares 11-29'}
level = ask_level()

correct_answers = 0

#driver code depending on user's choice
if level == '1':
    for _ in range(5):
        task = random_task()
        print(*task)
        user_answer = get_user_answer()
        check_answer(user_answer, answer(*task))

if level == '2':
    for _ in range(5):
        task = random.randint(11, 29)
        print(task)
        user_answer = get_user_answer()
        check_answer(user_answer, task * task)

save_choice = input(f"Your mark is {correct_answers}/5. Would you like to save the result? Enter yes or no.\n")

#Save file if yes
if save_choice in ('yes', 'YES', 'y', 'Yes'):
    save_results()