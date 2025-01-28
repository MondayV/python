# interface.py
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from core import GachaCore
from styles import configure_styles  # 导入样式配置

class GachaGUI:
    def __init__(self, master):
        self.master = master
        self.core = GachaCore()
        
        # 应用全局样式
        configure_styles()
        self.setup_ui()

    def setup_ui(self):
        """初始化界面组件"""
        self.master.title("抽卡模拟分析器")
        self.master.geometry("900x700")
        self.master.configure(bg='#2D2D2D')  # 直接设置窗口背景

        # 主容器（使用styles.py中定义的样式）
        main_frame = ttk.Frame(self.master, style='Gold.TLabelframe')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # 输入区
        input_frame = ttk.LabelFrame(
            main_frame, 
            text=" 抽卡设置 ",
            style='Gold.TLabelframe'
        )
        input_frame.pack(fill=tk.X, pady=10, padx=10)

        # 输入组件
        ttk.Label(
            input_frame, 
            text="请输入抽卡次数（1-1000）：",
            style='Gold.TLabelframe.Label'
        ).pack(side=tk.LEFT, padx=5)
        
        self.entry_times = ttk.Entry(
            input_frame, 
            width=10, 
            style='Dark.TEntry'
        )
        self.entry_times.pack(side=tk.LEFT, padx=5)
        
        # 功能按钮
        btn_start = ttk.Button(
            input_frame, 
            text="开始抽卡！", 
            style='Golden.TButton',
            command=self.start_gacha
        )
        btn_start.pack(side=tk.LEFT, padx=5)
        
        btn_chart = ttk.Button(
            input_frame, 
            text="显示图表", 
            style='Golden.TButton',
            command=self.show_charts
        )
        btn_chart.pack(side=tk.LEFT, padx=5)

        # 结果展示区
        self.result_text = tk.Text(
            main_frame, 
            bg='#1E1E1E', 
            fg='white',
            insertbackground='white',
            font=('Microsoft YaHei', 10)
        )
        self.result_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # ----------- 功能方法------------
    def validate_input(self):
        """验证输入有效性"""
        try:
            times = int(self.entry_times.get())
            if 1 <= times <= 1000:
                return times
            messagebox.showerror("错误", "抽卡次数需在1-1000之间！")
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字！")
        return None

    def start_gacha(self):
        """执行抽卡操作"""
        times = self.validate_input()
        if not times:
            return
        
        self.core.reset()
        self.core.pull_multi(times)
        self.show_report()

    def show_report(self):
        """显示统计报告"""
        report = [
            "抽卡统计报告",
            f"总抽卡次数：{len(self.core.history)}",
            "\n【★ 五星角色】",
            f"→ 总数量：{self.core.total_5}",
            self._get_interval_stats(),
            "\n【★ 四星物品】",
            f"→ 角色数量：{self.core.total_4_char}",
            f"→ 武器数量：{self.core.total_4_weapon}",
            "\n【★ 三星武器】",
            f"→ 总数量：{self.core.total_3}"
        ]
        
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "\n".join(report))
        self.result_text.config(state=tk.DISABLED)

    def _get_interval_stats(self):
        """获取五星间隔统计"""
        positions = [i for i, res in enumerate(self.core.history) if res == '5_star']
        intervals = [positions[i]-positions[i-1]-1 for i in range(1, len(positions))]
        
        if not positions:
            return "→ 尚未抽到五星角色"
        
        avg = sum(intervals)/len(intervals) if intervals else 0
        return (f"→ 平均出货间隔：{avg:.1f}抽\n"
                f"→ 最大间隔：{max(intervals) if intervals else 0}抽\n"
                f"→ 最小间隔：{min(intervals) if intervals else 0}抽")

    def show_charts(self):
        """显示图表窗口"""
        if not self.core.history:
            messagebox.showwarning("警告", "请先执行抽卡操作！")
            return

        try:
            chart_window = tk.Toplevel(self.master)
            chart_window.title("抽卡统计图表")
            
            fig = self._create_figure()
            canvas = FigureCanvasTkAgg(fig, master=chart_window)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
        except Exception as e:
            messagebox.showerror("图表错误", f"生成图表失败：{str(e)}")

    def _create_figure(self):
        """创建matplotlib图表"""
        fig = plt.figure(figsize=(12, 6))
        
        # 饼图
        ax1 = fig.add_subplot(121)
        total_4 = self.core.total_4_char + self.core.total_4_weapon
        labels = [f'5星 ({self.core.total_5})', 
                 f'4星 ({total_4})', 
                 f'3星 ({self.core.total_3})']
        sizes = [self.core.total_5, total_4, self.core.total_3]
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        ax1.set_title('星级分布比例')

        # 柱状图
        ax2 = fig.add_subplot(122)
        categories = ['三星武器', '四星武器', '四星角色', '五星角色']
        values = [self.core.total_3, 
                 self.core.total_4_weapon,
                 self.core.total_4_char,
                 self.core.total_5]
        bars = ax2.bar(categories, values)
        ax2.set_title('详细物品分布')
        ax2.set_ylabel('数量')
        
        for bar in bars:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}', ha='center', va='bottom')
        
        plt.tight_layout()
        return fig

if __name__ == "__main__":
    root = tk.Tk()
    app = GachaGUI(root)
    root.mainloop()