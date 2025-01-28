import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

def configure_styles():
    """配置全局界面样式"""
    # 配置Matplotlib中文字体
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 创建ttk样式对象
    style = ttk.Style()
    
    # 设置主题
    style.theme_use('clam')

    # 主背景色配置
    style.configure('.', 
                   background='#2D2D2D', 
                   foreground='white',
                   font=('Microsoft YaHei', 10))

    # 标签框架样式
    style.configure('Gold.TLabelframe', 
                   background='#3A3A3A', 
                   bordercolor='#555555',
                   relief='groove')
    style.configure('Gold.TLabelframe.Label', 
                   background='#3A3A3A', 
                   foreground='#FFD700',
                   font=('Microsoft YaHei', 12, 'bold'))

    # 金色按钮样式
    style.configure('Golden.TButton', 
                   font=('Microsoft YaHei', 12),
                   foreground='#2D2D2D',
                   background='#FFD700',
                   borderwidth=2,
                   padding=8)
    style.map('Golden.TButton',
             background=[('active', '#FFE55C'), ('!active', '#FFD700')],
             foreground=[('active', '#2D2D2D'), ('!active', '#2D2D2D')])

    # 暗色输入框样式
    style.configure('Dark.TEntry',
                   fieldbackground='#1E1E1E',
                   foreground='white',
                   insertcolor='white',
                   bordercolor='#555555',
                   relief='flat')

    # 文本区域样式
    style.configure('Dark.TText',
                   background='#1E1E1E',
                   foreground='white',
                   insertbackground='white')

    # 配置窗口背景
    style.configure('Tk', background='#2D2D2D')