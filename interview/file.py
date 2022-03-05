import os


def walk():
    a = input("请输入想要查找的磁盘：") + ':/'
    b = input("请输入想要查找的文件名和后缀：")
    for root, dirs, files in os.walk(a):
        if b in files:
            print("找到了")
            print("root: " + root)
            print("dirs: " + str(dirs))
            print("files:" + str(files))
            break
        else:
            pass


if __name__ == '__main__':
    walk()
