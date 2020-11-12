import string
import random

def get_str(length, with_chinese=False, container_weight=0, reverse_weight: list=None):
    '''
    获取指定长度正则表达式
    :param length:              正则长度
    :param with_chinese:        是否使用中文
    :param container_weight:    容器比重（目前只添加了3种），0即不使用容器，可用于生成大文本文件
    :param reverse_weight:      保留位，可通过传入list加重某些字符的权重
    :return:                    随机生成的正则表达式
    '''
    single_chars = list(string.printable)  # 大小写字母 + 数字 + 常用符号 + 空白符

    if with_chinese:
        chinese_chars = [chr(val) for val in range(0x4e00, 0x9fbf)]
    else:
        chinese_chars = []

    containers = ['[]', '()', '{}'] * container_weight

    all_chars = single_chars + chinese_chars + containers

    if reverse_weight and isinstance(reverse_weight, list):
        all_chars += reverse_weight

    ret_str = str()
    for i in range(length):
        r_int = random.randint(0, len(all_chars) - 1)
        select_char = all_chars[r_int]
        # 容器符号随机选择起始位置插入
        if select_char in containers:
            # print('select_char:', select_char)
            # print('before:', ret_str)
            cur_len = len(ret_str)
            s_index = random.randint(0, cur_len)
            e_index = random.randint(s_index, cur_len)
            ret_str = ret_str[:s_index] + select_char[0] + \
                      ret_str[s_index:e_index] + select_char[1] + \
                      ret_str[e_index:]

            # print('after:', ret_str)
        else:
            ret_str += select_char
    return ret_str

for j in range(20):
    print(get_str(20, with_chinese=False, container_weight=10, reverse_weight=2))
    print('================================================')