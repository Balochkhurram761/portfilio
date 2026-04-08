# with open('data.txt', 'r') as file:
#    content = file.read()
#    print(content)

# loggeddata= "hello my name is khurram\n"
# with open('data.txt', 'a') as file:
#    file.write(loggeddata)
#    print(file)
# with open('data.txt', 'r') as file:
#     for line in file:
#         print(line.strip())

# lines = ["First line\n", "Second line\n", "Third line\n"]
# with open('data.txt', 'w') as file:  # Overwrite mode
#     file.writelines(lines)
# with open('data.txt', 'r') as file:
#     lines = file.readlines()  # Returns list of lines
#     print(lines)
# import os

# if os.path.exists('data.txt'):
#     with open('data.txt', 'r') as file:
#         print(file.read())
# else:
#     print("File does not exist.")

# def add_task(task):
#     with open('tasks.txt', 'a') as file:
#         file.write(task + '\n')

# def view_tasks():
#     with open('tasks.txt', 'r') as file:
#         tasks = file.readlines()
#     for idx, task in enumerate(tasks, start=1):
#         print(f"{idx}. {task.strip()}")

# # Usage
# add_task("Finish Python project")
# add_task("Prepare for interview")
# view_tasks()


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)

print(acc.get_balance())