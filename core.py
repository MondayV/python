import random

class GachaCore:
    """抽卡系统核心逻辑"""
    def __init__(self):
        self.reset()
        
    def reset(self):
        """重置所有计数器"""
        self.pity_5 = 0      # 五星保底计数器
        self.pity_4 = 0      # 四星保底计数器
        self.total_5 = 0     # 五星总数量
        self.total_4_char = 0  # 四星角色数量
        self.total_4_weapon = 0  # 四星武器数量
        self.total_3 = 0     # 三星武器数量
        self.history = []    # 抽卡结果记录

    def pull_multi(self, times):
        """执行多次抽卡"""
        return [self.pull_once() for _ in range(times)]

    def pull_once(self):
        """执行单次抽卡"""
        result = None
        
        # 处理五星保底和概率
        if self.pity_5 >= 89:
            result = self._handle_5star()
        else:
            if random.random() < 0.006:  # 0.6%基础概率
                result = self._handle_5star()
        
        # 未获得五星时处理四星和三星
        if not result:
            if self.pity_4 >= 9:  # 四星保底
                result = self._handle_4star_guarantee()
            else:
                if random.random() < 0.051:  # 5.1%四星概率
                    result = self._handle_4star()
                else:  # 三星
                    result = self._handle_3star()
        
        self.history.append(result)
        return result

    def _handle_5star(self):
        self.total_5 += 1
        self.pity_5 = 0
        self.pity_4 = 0
        return '5_star'

    def _handle_4star(self):
        if random.random() < 0.5:
            self.total_4_char += 1
            res = '4_char'
        else:
            self.total_4_weapon += 1
            res = '4_weapon'
        self.pity_4 = 0
        self.pity_5 += 1
        return res

    def _handle_3star(self):
        self.total_3 += 1
        self.pity_4 += 1
        self.pity_5 += 1
        return '3_weapon'

    def _handle_4star_guarantee(self):
        if random.random() < 0.006:  # 0.6%概率获得五星
            return self._handle_5star()
        else:
            return self._handle_4star()