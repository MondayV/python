# gacha_system/core/controller.py
from .gacha_core import GachaCore
from .analyzer import GachaAnalyzer

class GachaController:
    """协调核心逻辑和界面交互"""
    def __init__(self):
        self.core = GachaCore()
        self.analyzer = GachaAnalyzer()

    def execute_pulls(self, times):
        """执行抽卡操作"""
        self.core.reset()
        return self.core.pull_multi(times)

    def get_statistics(self):
        """获取统计信息"""
        return {
            'total_pulls': len(self.core.history),
            'total_5': self.core.total_5,
            'total_4_char': self.core.total_4_char,
            'total_4_weapon': self.core.total_4_weapon,
            'total_3': self.core.total_3,
            'intervals': self.analyzer.calculate_intervals(self.core.history)
        }