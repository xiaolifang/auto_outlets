import yaml
import os

from APP import BASE_PROJECT


def get_file_data(file_name):
    with open(BASE_PROJECT + os.sep + "data" + os.sep + file_name, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    return data

    # print("成功能够;;;;;;",suc_list)
    #     # print("失败能够;;;;;;",fai_list)

# get_data()
