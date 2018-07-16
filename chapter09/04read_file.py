# create by 'yang' in 2018/7/12 
__author__ = 'yang'


# 读取一个500G的文件
# f.read(4096) # 代表一次读取4096字节的数据

def myreadlines(f, newline):
    buf = ''
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]
        chunk = f.read(20)
        if not chunk:
            yield buf
            break
        buf += chunk


with open('input.txt') as f:
    for line in myreadlines(f, "{|}"):
        print(line)
