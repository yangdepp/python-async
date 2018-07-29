# 事件循环和协程：从生成器到协程
def child():
    r = '这是子程序'
    yield r

def main(c):
    res = c.send(None)
    print(res)

c = child()
main(c)