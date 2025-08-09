# gacha_system/core/analyzer.py
class GachaAnalyzer:
    @staticmethod
    def calculate_intervals(history):
        """计算五星抽卡间隔统计"""
        positions = [i for i, res in enumerate(history) if res == '5_star']
        intervals = [positions[i]-positions[i-1]-1 for i in range(1, len(positions))]
        
        if not positions:
            return None
        
        return {
            'average': sum(intervals)/len(intervals) if intervals else 0,
            'max': max(intervals) if intervals else 0,
            'min': min(intervals) if intervals else 0,
            'count': len(positions)
        }