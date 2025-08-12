# 外星人入侵游戏

> 基于 Pygame 的太空射击游戏

## 游戏功能
- 玩家控制飞船移动和射击
- 自动生成外星人舰队
- 碰撞检测系统
- 分数统计和等级系统
- 生命值管理

## 游戏控制
- ← → 方向键：移动飞船
- 空格键：发射子弹
- Q 键：退出游戏

## 项目结构
├── alien_invasion.py    # 主游戏逻辑
├── settings.py          # 游戏配置
├── ship.py              # 飞船
├── bullet.py            # 子弹
├── alien.py             # 外星人
├── game_stats.py        # 游戏统计
├── scoreboard.py        # 记分器
└── README.md            # 项目说明

## 运行要求
- Python 3.7+
- Pygame 2.0+
```bash
pip install pygame