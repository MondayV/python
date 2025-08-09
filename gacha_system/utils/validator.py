# gacha_system/utils/validator.py
def validate_input(input_str):
    """验证用户输入有效性"""
    try:
        times = int(input_str)
        if 1 <= times <= 1000:
            return (True, times)
        return (False, "抽卡次数需在1-1000之间！")
    except ValueError:
        return (False, "请输入有效的数字！")