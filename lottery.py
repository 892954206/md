import random

def simple_lottery(participants, num_winners=1):
    """
    简单抽奖函数
    :param participants: 参与者列表
    :param num_winners: 获奖人数（默认为1）
    :return: 获奖者列表
    """
    if num_winners > len(participants):
        raise ValueError("获奖人数不能超过参与者人数！")
    winners = random.sample(participants, num_winners)
    return winners

# 示例用法
participants = ["张三", "李四", "王五", "赵六", "小明", "小红"]
winners = simple_lottery(participants, num_winners=2)
print("获奖者是：", winners)