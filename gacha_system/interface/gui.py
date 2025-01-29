# gacha_system/interface/gui.py
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ..core.controller import GachaController
from .widgets import configure_styles
from ..utils.validator import validate_input
from ..utils.chart_generator import create_chart

class GachaGUI:
    """抽卡系统图形界面"""
    def __init__(self, master):
        self.master = master
        self.controller = GachaController()
        configure_styles()
        self.setup_ui()
        self.chart_window = None  # 新增窗口跟踪属性
        self.chart_canvas = None

    def setup_ui(self):
        """初始化界面组件"""
        self.master.title("抽卡模拟分析器")
        self.master.geometry("900x700")

        main_frame = ttk.Frame(self.master, style='Gold.TLabelframe')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # 输入面板
        input_panel = ttk.LabelFrame(main_frame, text=" 抽卡设置 ", style='Gold.TLabelframe')
        input_panel.pack(fill=tk.X, pady=10, padx=10)

        ttk.Label(input_panel, text="请输入抽卡次数（1-1000）：", 
                style='Gold.TLabelframe.Label').pack(side=tk.LEFT, padx=5)
        
        self.entry_times = ttk.Entry(input_panel, width=10, style='Dark.TEntry')
        self.entry_times.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(input_panel, text="开始抽卡！", style='Golden.TButton',
                 command=self.start_gacha).pack(side=tk.LEFT, padx=5)
        ttk.Button(input_panel, text="显示图表", style='Golden.TButton',
                 command=self.show_chart).pack(side=tk.LEFT, padx=5)

        # 结果展示区
        self.result_display = tk.Text(main_frame, bg='#1E1E1E', fg='white',
                                    insertbackground='white', font=('Microsoft YaHei', 10))
        self.result_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def start_gacha(self):
        """处理抽卡操作"""
        self._close_chart_window()  # 关闭图表窗口
        input_value = self.entry_times.get()
        valid, result = validate_input(input_value)
        if not valid:
            messagebox.showerror("错误", result)
            return
        
        self.controller.execute_pulls(result)
        self.update_display()

    def update_display(self):
        """更新统计信息显示"""
        stats = self.controller.get_statistics()
        report = self._format_report(stats)
        
        self.result_display.config(state=tk.NORMAL)
        self.result_display.delete(1.0, tk.END)
        self.result_display.insert(tk.END, report)
        self.result_display.config(state=tk.DISABLED)

    def _format_report(self, stats):
        """格式化统计报告"""
        interval_info = ("→ 尚未抽到五星角色" if not stats['intervals'] else
                       f"→ 平均出货间隔：{stats['intervals']['average']:.1f}抽\n"
                       f"→ 最大间隔：{stats['intervals']['max']}抽\n"
                       f"→ 最小间隔：{stats['intervals']['min']}抽")
        
        return "\n".join([
            "抽卡统计报告",
            f"总抽卡次数：{stats['total_pulls']}",
            "\n【★ 五星角色】",
            f"→ 总数量：{stats['total_5']}",
            interval_info,
            "\n【★ 四星物品】",
            f"→ 角色数量：{stats['total_4_char']}",
            f"→ 武器数量：{stats['total_4_weapon']}",
            "\n【★ 三星武器】",
            f"→ 总数量：{stats['total_3']}"
        ])

    def show_chart(self):
        """显示统计图表"""
        self._close_chart_window()  # 关闭已有窗口

        if not self.controller.core.history:
            messagebox.showwarning("警告", "请先执行抽卡操作！")
            return

        try:
            self.chart_window = tk.Toplevel(self.master)
            self.chart_window.title("抽卡统计图表")
            self.chart_window.protocol("WM_DELETE_WINDOW", self._on_chart_close)

            stats = self.controller.get_statistics()
            fig = create_chart(
                stats['total_5'],
                stats['total_4_char'],
                stats['total_4_weapon'],
                stats['total_3']
            )
            
            self.chart_canvas = FigureCanvasTkAgg(fig, master=self.chart_window)
            self.chart_canvas.draw()
            self.chart_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
        except Exception as e:
            messagebox.showerror("图表错误", f"生成图表失败：{str(e)}")
            self._on_chart_close()
            
    def _on_chart_close(self):
            """处理图表窗口关闭事件"""
            if self.chart_canvas:
                self.chart_canvas.get_tk_widget().destroy()
                self.chart_canvas = None
            if self.chart_window:
                self.chart_window.destroy()
                self.chart_window = None
    def _close_chart_window(self):
        """主动关闭图表窗口"""
        if self.chart_window and self.chart_window.winfo_exists():
            self._on_chart_close()