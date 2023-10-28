import request
import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logging.warn("dasdasdasd")
    a = [1, 2, 3, 4, 5, 6, 7, 9, 8, 0]
    b = len(a)
    d = list(range(b))
    Max = 0
    Min = 0
    for i in list(range(b)):
        for j in list(range(i+1, b)):
            if a[i] < a[j]:
                Max = a[j]
                Min = a[i]
            else:
                Max = a[i]
                Min = a[j]
            e = Max
            a[j] = Min
            a[i] = e
        print(a)
    print(a)






