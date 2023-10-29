import threading
import time


def haha(num, put_list: list):
    time.sleep(num / 1000)
    print(num)
    put_list.append(num)


if __name__ == '__main__':
    in_list = [1, 122, 32, 444, 41, 312, 44, 98]
    out_list = []
    for x in in_list:
        t = threading.Thread(target=haha, args=(x, out_list))
        t.start()
    time.sleep(3)
    print(out_list)