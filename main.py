# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def count_list():
    l = [{'name': 12},
         {'age': 333}]
    x = 0
    for i in l:
        x += 1
    return x


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(count_list())
 
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
