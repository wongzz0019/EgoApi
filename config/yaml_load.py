# 读取yaml文件

import yaml


# 封装
def load_yaml(filename):
    # 打开要读取的文件  r可读取
    stream = open(filename, 'r')
    # 读取文件数据
    data = yaml.load(stream, yaml.FullLoader)
    return data
