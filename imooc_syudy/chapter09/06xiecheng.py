# create by 'yang' in 2018/7/13 
__author__ = 'yang'

final_result = {}


def sales_sum(pro_name):
    total = 0
    nums = []
    while True:
        x = yield
        print(pro_name + '销量：', x)
        if not x:
            break
        total += x
        nums.append(x)
    return total, nums


def middle(key):
    while True:
        final_result[key] = yield from sales_sum(key)
        print(key + '销售统计完成！。')


def main():
    data_sets = {
        'yang牌面膜': [1200, 1500, 3000],
        'yang牌手机': [28, 55, 98, 108],
        'yang牌电脑': [280, 560, 778, 70]
    }
    for key, data_sets in data_sets.items():
        print('start key:', key)
        m = middle(key)
        m.send(None)
        for value in data_sets:
            m.send(value)
        m.send(None)
    print('final_result', final_result)


if __name__ == '__main__':
    main()
