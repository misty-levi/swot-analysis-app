import streamlit as st

# 全局暗黑主题 + 字体 + 圆角
st.set_page_config(
    page_title="专升本学员SWOT智能分析系统",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    /* 全局底色 & 字体 */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #e0e0e0;
        font-family: 'SF Pro Display', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }

    /* 标题发光文字 */
    h1, h2, h3 {
        color: #00f5ff !important;
        text-shadow: 0 0 8px #00f5ff;
    }

    /* 卡片/容器：毛玻璃 + 霓虹边框 */
    .glass-card {
        background: rgba(255, 255, 255, 0.06);
        border-radius: 16px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        margin-bottom: 1rem;
        padding: 1.5rem;
    }

    /* 进度条：赛博霓虹 */
    .stProgress > div > div {
        background: linear-gradient(90deg, #00f5ff, #ff00ff);
        border-radius: 10px;
    }

    /* 按钮：霓虹发光 */
    .stButton > button {
        border: none;
        color: #0f0c29;
        background: linear-gradient(90deg, #00f5ff, #ff00ff);
        padding: 0.75rem 1.5rem;
        border-radius: 999px;
        font-weight: 600;
        box-shadow: 0 0 10px #00f5ff, 0 0 20px #ff00ff;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 0 15px #00f5ff, 0 0 30px #ff00ff;
    }

    /* 选项单选：悬浮霓虹 */
    .stRadio > div[role="radiogroup"] label {
        background: rgba(255, 255, 255, 0.07);
        border-radius: 12px;
        padding: 0.5rem 1rem;
        margin-bottom: 0.5rem;
        transition: all 0.3s;
        color: #ffffff !important;
    }
    .stRadio > div[role="radiogroup"] label:hover {
        background: rgba(0, 245, 255, 0.2);
        box-shadow: 0 0 8px #00f5ff;
    }

    /* 指标卡：透明底 + 霓虹字 */
    div[data-testid="metric-container"] {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 1rem;
        border: 1px solid rgba(0, 245, 255, 0.3);
        box-shadow: 0 0 10px rgba(0, 245, 255, 0.4);
    }
    
    /* 指标值 - 保持原样 */
    [data-testid="stMetricValue"] {
        color: #ff00ff;
        font-weight: 700;
        font-size: 24px;
    }
    
    /* 指标标签 - 增大SWOT标签字体并添加霓虹效果 */
    [data-testid="stMetricLabel"] {
        font-size: 1.8rem !important;
        font-weight: 700;
        color: #e0e0e0 !important;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 5px #00f5ff, 0 0 10px #00f5ff, 0 0 15px #00f5ff;
        animation: neonGlow 1.5s infinite alternate;
    }
    
    /* 霓虹光效动画 */
    @keyframes neonGlow {
        from {
            text-shadow: 0 0 5px #00f5ff, 0 0 10px #00f5ff, 0 0 15px #00f5ff;
        }
        to {
            text-shadow: 0 0 10px #00f5ff, 0 0 20px #00f5ff, 0 0 30px #00f5ff, 0 0 40px #00f5ff;
        }
    }
    
    /* 指标变化 - 保持原样 */
    [data-testid="stMetricDelta"] {
        font-weight: 600;
    }

    /* 侧边栏：半透明 */
    .css-1d391kg {
        background: rgba(0, 0, 0, 0.25) !important;
    }
    
    /* 强制所有radio选项文字为白色 */
    .stRadio label {
        color: white !important;
    }
    
    /* 更具体的选择器确保文字颜色 */
    div[data-testid="stRadio"] label,
    div[data-testid="stRadio"] label span,
    .st-bx label,
    .st-bx label span {
        color: white !important;
    }
    
    /* 针对Streamlit新版本的radio按钮样式 */
    .st-cc label,
    .st-cc label span,
    .st-cd label,
    .st-cd label span,
    .st-ce label,
    .st-ce label span {
        color: white !important;
    }
    
    /* 确保所有文本元素在暗色背景下可见 */
    .stRadio > label,
    .stRadio > div > label,
    .stRadio > div > div > label {
        color: white !important;
    }
    
    /* 针对选项文字的特殊处理 */
    .st-ae, .st-af, .st-ag, .st-ah, .st-ai {
        color: white !important;
    }
    
    /* 选项卡按钮样式 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 10px 20px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(0, 245, 255, 0.2);
        border: 1px solid #00f5ff;
        box-shadow: 0 0 10px rgba(0, 245, 255, 0.5);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, #00f5ff, #ff00ff);
        color: #0f0c29 !important;
        font-weight: bold;
        box-shadow: 0 0 15px #00f5ff, 0 0 25px #ff00ff;
        border: none;
    }
    
    /* 选项卡内容区域 */
    [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1rem;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True,
)


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time

# 设置页面配置
st.set_page_config(
    page_title="专升本学员SWOT智能分析系统",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 定义测试题库（与之前相同）
questions = [
    # 优势 (Strengths)
    {"text": "对我来说，一旦制定了计划，我通常都能坚持下去。", "type": "S", "reverse": False},
    {"text": "我书桌或学习区域的东西总是井井有条。", "type": "S", "reverse": False},
    {"text": "我总能注意到一些别人没留意的政策或消息变化。", "type": "S", "reverse": False},
    {"text": "我认为自己比多数同龄人更清楚未来的方向。", "type": "S", "reverse": False},
    {"text": "我乐于接受有挑战性的任务，并享受克服困难的过程。", "type": "S", "reverse": False},
    
    # 劣势 (Weaknesses)
    {"text": "如果遇到一道难题，我的第一反应是去查阅答案或请教别人。", "type": "W", "reverse": True},
    {"text": "我经常觉得，如果时间再多一点，我能把事情做得更好。", "type": "W", "reverse": True},
    {"text": "我认为我获取关键信息的渠道比较有限。", "type": "W", "reverse": True},
    {"text": "考试前，即使准备充分，我依然会感到紧张。", "type": "W", "reverse": True},
    {"text": "如果一次努力没有看到结果，我很容易感到气馁。", "type": "W", "reverse": True},
    {"text": "我常常担心\"选择\"本身会带来错误的结果。", "type": "W", "reverse": True},
    
    # 机会 (Opportunities)
    {"text": "当我做出一个重要决定时，我能获得足够的支持。", "type": "O", "reverse": False},
    {"text": "我认识一些优秀的学长学姐，他们的经历对我很有启发。", "type": "O", "reverse": False},
    {"text": "在我看来，未来的趋势对我们这一代人比较有利。", "type": "O", "reverse": False},
    {"text": "我擅长的领域，似乎正变得越来越受欢迎。", "type": "O", "reverse": False},
    {"text": "一些新的变革（如新技术、新政策）总让我觉得是种机遇。", "type": "O", "reverse": False},
    
    # 威胁 (Threats)
    {"text": "我身边有些朋友，他们的选择常常让我感到压力。", "type": "T", "reverse": False},
    {"text": "我常常需要为一些家庭或生活琐事分心。", "type": "T", "reverse": False},
    {"text": "我认为，重要的机会窗口正在慢慢变窄。", "type": "T", "reverse": False},
    {"text": "我感觉，无论做什么，好像都有很多竞争对手。", "type": "T", "reverse": False}
]

options = {
    "A": {"text": "非常符合", "score": 5},
    "B": {"text": "比较符合", "score": 4},
    "C": {"text": "一般/不确定", "score": 3},
    "D": {"text": "不太符合", "score": 2},
    "E": {"text": "非常不符合", "score": 1}
}

class SWOTScorer:
    def __init__(self):
        self.scores = {"S": 0, "W": 0, "O": 0, "T": 0}
        self.details = {"S": [], "W": [], "O": [], "T": []}
        self.total_questions = len(questions)
        self.answered = 0
        
    def add_score(self, question_idx, answer_key):
        question = questions[question_idx]
        option = options[answer_key.upper()]
        score = option["score"]
        
        if question["reverse"]:
            score = 6 - score
        
        self.scores[question["type"]] += score
        
        self.details[question["type"]].append({
            "text": question["text"],
            "score": score,
            "answer": option["text"]
        })
        
        self.answered += 1
    
    def get_results(self):
        return {
            "scores": self.scores,
            "details": self.details
        }

# 初始化session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = [None] * len(questions)
if 'scorer' not in st.session_state:
    st.session_state.scorer = SWOTScorer()
if 'test_complete' not in st.session_state:
    st.session_state.test_complete = False

def main():
    # 页面标题
    st.title("🎓 专升本学员SWOT智能分析系统")
    st.markdown("---")
    
    if not st.session_state.test_complete:
        # 测试界面
        show_test_interface()
    else:
        # 结果展示界面
        show_results_interface()

def show_test_interface():
    col1, col2 = st.columns([3, 1])
    
    with col1:
        current_idx = st.session_state.current_question
        question = questions[current_idx]
        
        # 显示进度条
        progress = (current_idx + 1) / len(questions)
        st.progress(progress)
        st.caption(f"进度: {current_idx + 1}/{len(questions)}")
        
        # 显示当前问题
        st.subheader(f"第 {current_idx + 1} 题")
        st.markdown(f"### {question['text']}")
        
        # 答案选项
        answer_options = ["A. 非常符合", "B. 比较符合", "C. 一般", "D. 不太符合", "E. 非常不符合"]
        selected = st.radio("请选择最符合的选项:", answer_options, key=f"q{current_idx}")
        
        col_btn1, col_btn2 = st.columns(2)
        
        with col_btn1:
            if current_idx > 0:
                if st.button("上一题", use_container_width=True):
                    st.session_state.current_question -= 1
                    st.rerun()
        
        with col_btn2:
            if selected:
                if st.button("下一题" if current_idx < len(questions) - 1 else "完成测试", 
                           type="primary", use_container_width=True):
                    # 保存答案
                    answer_key = selected[0]  # 获取A/B/C/D/E
                    st.session_state.scorer.add_score(current_idx, answer_key)
                    st.session_state.answers[current_idx] = answer_key
                    
                    if current_idx < len(questions) - 1:
                        st.session_state.current_question += 1
                        st.rerun()
                    else:
                        st.session_state.test_complete = True
                        st.rerun()
    
    with col2:
        st.info("""
        ### 📝 测试说明
        - 共有20道题目
        - 请根据第一感觉选择
        - 真实作答效果最佳
        - 完成后生成详细分析报告
        """)
        
        # 移除了"当前维度"的显示部分
        # 只保留测试说明，不再显示当前问题的SWOT类型

def show_results_interface():
    results = st.session_state.scorer.get_results()
    scores = results["scores"]
    details = results["details"]
    
    # 计算平均分
    avg_s = scores["S"] / len([q for q in questions if q["type"] == "S"])
    avg_w = scores["W"] / len([q for q in questions if q["type"] == "W"])
    avg_o = scores["O"] / len([q for q in questions if q["type"] == "O"])
    avg_t = scores["T"] / len([q for q in questions if q["type"] == "T"])
    
    # 创建选项卡界面
    tab1, tab2, tab3 = st.tabs(["📊 总体分析", "🎯 SWOT矩阵", "💡 个性建议"])
    
    with tab1:
        st.header("总体分析报告")
        
        # 分数卡片
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("✅ 优势", f"{avg_s:.1f}/5.0", f"{scores['S']}分")
        with col2:
            st.metric("❌ 劣势", f"{avg_w:.1f}/5.0", f"{scores['W']}分")
        with col3:
            st.metric("🎯 机会", f"{avg_o:.1f}/5.0", f"{scores['O']}分")
        with col4:
            st.metric("⚠️ 威胁", f"{avg_t:.1f}/5.0", f"{scores['T']}分")
        
        # 总体评估
        st.markdown("---")
        if avg_s + avg_o > avg_w + avg_t:
            st.success("### 🎉 积极前景")
            st.markdown("""
            **总体评估**: 你的外部机会与内部优势相结合，专升本成功几率较高！
            
            **核心优势**:
            - 具有良好的执行力和目标感
            - 能够把握外部机会
            - 整体积极因素多于消极因素
            
            **建议**: 保持当前节奏，继续发挥优势，积极备考！
            """)
        else:
            st.warning("### ⚠️ 需要重点关注")
            st.markdown("""
            **总体评估**: 你面临一些挑战，但只要针对性改进，完全有机会实现逆袭！
            
            **重点关注**:
            - 需要改进某些方面的表现
            - 建议寻求外部帮助和支持
            - 制定详细的学习计划
            
            **建议**: 不要放弃，针对性改进后成功率会大幅提升！
            """)
    
    with tab2:
        st.header("SWOT分析矩阵")

        # 1. 映射表
        swot_labels = {
            'S': ["执行力", "组织力", "洞察力", "目标感", "进取心"],
            'W': ["依赖性", "拖延倾向", "信息局限", "考试焦虑", "韧性不足", "决策困难"],
            'O': ["支持系统", "榜样引导", "环境利好", "趋势匹配", "变革机会"],
            'T': ["同伴压力", "环境干扰", "时机紧迫", "竞争激烈"]
        }

        # 2. 计算平均分
        avg_s = scores["S"] / len([q for q in questions if q["type"] == "S"])
        avg_w = scores["W"] / len([q for q in questions if q["type"] == "W"])
        avg_o = scores["O"] / len([q for q in questions if q["type"] == "O"])
        avg_t = scores["T"] / len([q for q in questions if q["type"] == "T"])

        # 3. 提取高分项
        def get_high_score_items(swot_type):
            high = []
            for idx, item in enumerate(details[swot_type]):
                if item["score"] >= 4 and idx < len(swot_labels[swot_type]):
                    high.append(swot_labels[swot_type][idx])
            return high

        high_S = get_high_score_items('S')
        high_W = get_high_score_items('W')
        high_O = get_high_score_items('O')
        high_T = get_high_score_items('T')

        # 4. 颜色及图标配置
        swot_style = {
            'S': {'color': '#28a745', 'icon': '✅'},
            'W': {'color': '#dc3545', 'icon': '⚠️'},
            'O': {'color': '#17a2b8', 'icon': '🚀'},
            'T': {'color': '#ffc107', 'icon': '⚡'}
        }

        # 5. 2×2 网格
        col_left, col_right = st.columns(2)

        # 通用渲染函数
        def render_quadrant(col, label, title, avg_score, items):
            """静态展示象限"""
            color = swot_style[label]['color']
            icon  = swot_style[label]['icon']

            with col:
                with st.container(border=True):
                    st.markdown(
                        f"### {icon} {title} ({label})  "
                        f"<small style='color:{color};'>{avg_score:.1f}/5.0</small>",
                        unsafe_allow_html=True
                    )

                    if items:
                        # 一行行彩色标签
                        tag_html = " ".join(
                            f'<span style="background:{color};color:white;padding:4px 10px;border-radius:12px;'
                            f'margin:2px;display:inline-block;font-size:14px;">{t}</span>'
                            for t in items
                        )
                        st.markdown(tag_html, unsafe_allow_html=True)
                    else:
                        no_item_hint = {
                            'S': '暂无明显优势',
                            'W': '暂无明显劣势',
                            'O': '暂无明显机会',
                            'T': '暂无明显威胁'
                        }
                        st.caption(no_item_hint[label])

        # 6. 渲染四个象限
        with col_left:
            render_quadrant(col_left, 'S', "优势", avg_s, high_S)
            render_quadrant(col_left, 'O', "机会", avg_o, high_O)

        with col_right:
            render_quadrant(col_right, 'W', "劣势", avg_w, high_W)
            render_quadrant(col_right, 'T', "威胁", avg_t, high_T)
    
    with tab3:
        st.header("个性化建议")
        
        # 基于分数的策略建议
        st.subheader("🎯 总体备考策略")
        
        if avg_s > 3.5 and avg_o > 3.5:
            st.success("🚀 进攻型战略")
            st.markdown("""
            **策略重点**: 充分发挥优势，大胆把握机会
            
            **具体行动**:
            - 瞄准一流院校，设定较高目标
            - 利用现有优势加速学习进度
            - 积极抓住政策利好和外部机会
            - 保持自信，但避免过度冒进
            
            **预期效果**: 成功率较高，有望进入理想院校
            """)
        elif avg_s > 3.5 and avg_t > 3.5:
            st.warning("⚖️ 多元化战略")
            st.markdown("""
            **策略重点**: 利用优势应对威胁，分散风险
            
            **具体行动**:
            - 准备2-3个备选院校方案
            - 发挥长处规避外部威胁
            - 建立风险应对机制
            - 保持灵活调整的策略
            
            **预期效果**: 稳健备考，多重保障
            """)
        elif avg_w > 3.5 and avg_o > 3.5:
            st.info("🔄 扭转型战略")
            st.markdown("""
            **策略重点**: 全力改进劣势，把握机会实现逆袭
            
            **具体行动**:
            - 重点补足薄弱环节
            - 寻求老师和同学的帮助
            - 抓住外部机遇弥补不足
            - 需要付出加倍努力
            
            **预期效果**: 通过努力可以实现较大提升
            """)
        else:
            st.error("🛡️ 防御型战略")
            st.markdown("""
            **策略重点**: 稳扎稳打，克服劣势，规避威胁
            
            **具体行动**:
            - 从基础知识开始扎实学习
            - 优先确保基础题得分
            - 逐步提升，不求快但求稳
            - 建立良好的学习习惯
            
            **预期效果**: 稳步提升，先求稳再求进
            """)
        
        # 具体行动建议
        st.subheader("💡 具体行动建议")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **📅 立即行动清单**:
            1. 制定详细的周学习计划
            2. 整理专属学习空间
            3. 关注目标院校招生信息
            4. 加入学习小组互相监督
            5. 建立每日学习习惯
            """)
        
        with col2:
            st.markdown("""
            **🛠️ 实用工具推荐**:
            - 番茄TODO - 时间管理
            - Forest - 专注学习  
            - Notion - 知识整理
            - Xmind - 思维导图
            - 百度网盘 - 资料存储
            """)
        
        # 鼓励话语
        st.markdown("---")
        if avg_s + avg_o > avg_w + avg_t:
            st.success("🌈 你的基础很好，继续保持信心，坚持就是胜利！")
        else:
            st.info("🌟 每一个进步都值得庆祝，从现在开始行动，你一定能成功！")
    
    # 重新测试按钮
    st.markdown("---")
    if st.button("🔄 重新开始测试", use_container_width=True, type="primary"):
        st.session_state.current_question = 0
        st.session_state.answers = [None] * len(questions)
        st.session_state.scorer = SWOTScorer()
        st.session_state.test_complete = False
        st.rerun()

if __name__ == "__main__":
    main()