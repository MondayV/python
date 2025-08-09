# gacha_system/utils/chart_generator.py
import matplotlib.pyplot as plt

def create_chart(total_5, total_4_char, total_4_weapon, total_3):
    """生成统计图表"""
    fig = plt.figure(figsize=(12, 6))
    
    # 饼图
    ax1 = fig.add_subplot(121)
    total_4 = total_4_char + total_4_weapon
    ax1.pie([total_5, total_4, total_3],
           labels=[f'5星 ({total_5})', f'4星 ({total_4})', f'3星 ({total_3})'],
           autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    ax1.set_title('星级分布比例')

    # 柱状图
    ax2 = fig.add_subplot(122)
    categories = ['三星武器', '四星武器', '四星角色', '五星角色']
    values = [total_3, total_4_weapon, total_4_char, total_5]
    bars = ax2.bar(categories, values)
    ax2.set_title('详细物品分布')
    ax2.set_ylabel('数量')
    
    # 添加数值标签
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{height}', ha='center', va='bottom')
    
    plt.tight_layout()
    return fig