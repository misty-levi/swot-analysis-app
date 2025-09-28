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
        border: 1px solid rgba(255, 255, 255, 0.2);
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

    /* 课程卡片中加粗内容的颜色 - 修改为亮青色 */
    .stMarkdown strong {
        color: #00FFFF !important; /* 亮青色 */
        text-shadow: 0 0 5px rgba(0, 255, 255, 0.7);
        font-weight: bold;
    }

    /* 为加粗内容添加轻微的光晕动画效果 */
    @keyframes cyanGlow {
        from {
            text-shadow: 0 0 5px rgba(0, 255, 255, 0.7);
        }
        to {
            text-shadow: 0 0 10px rgba(0, 255, 255, 0.9), 0 0 15px rgba(0, 255, 255, 0.6);
        }
    }

    .stMarkdown strong {
        animation: cyanGlow 2s ease-in-out infinite alternate;
    }

    /* 调整课程推荐标题的字体大小 - 与课程卡片标题保持一致 */
    .course-recommendation-title {
        font-size: 1.5rem !important;
        font-weight: 700;
        color: #00FFFF !important;
        text-shadow: 0 0 5px #00FFFF;
        margin: 1rem 0;
        padding: 0.5rem 0;
        border-bottom: 2px solid rgba(0, 255, 255, 0.3);
    }

    /* 移动端适配 - 新增媒体查询 */
    @media screen and (max-width: 768px) {
        /* 调整全局字体大小 */
        .stApp {
            font-size: 14px;
        }
        
        /* 调整标题大小 */
        h1 {
            font-size: 1.8rem !important;
        }
        
        h2 {
            font-size: 1.5rem !important;
        }
        
        h3 {
            font-size: 1.2rem !important;
        }
        
        /* 调整指标标签大小 */
        [data-testid="stMetricLabel"] {
            font-size: 1.4rem !important;
        }
        
        /* 调整指标值大小 */
        [data-testid="stMetricValue"] {
            font-size: 20px !important;
        }
        
        /* 调整选项卡样式 */
        .stTabs [data-baseweb="tab"] {
            height: 40px;
            padding: 8px 12px;
            font-size: 14px;
        }
        
        /* 调整按钮大小 */
        .stButton > button {
            padding: 0.5rem 1rem;
            font-size: 14px;
        }
        
        /* 调整单选按钮大小 */
        .stRadio > div[role="radiogroup"] label {
            padding: 0.4rem 0.8rem;
            font-size: 14px;
        }
        
        /* 调整卡片内边距 */
        .glass-card {
            padding: 1rem;
        }
        
        /* 调整进度条高度 */
        .stProgress > div > div {
            height: 12px;
        }
        
        /* 调整布局间距 */
        .stColumn {
            margin-bottom: 1rem;
        }
        
        /* 调整测试说明框 */
        .stAlert {
            font-size: 13px;
        }
        
        /* 移动端调整课程标题大小 */
        .course-recommendation-title {
            font-size: 1.3rem !important;
        }
        
        /* 新增：移动端调整课程卡片价格字体大小 */
        .course-price {
            font-size: 18px !important; /* 从原来的25px减小到18px */
        }
        
        /* 确保价格容器在移动端有合适的间距 */
        .course-price-container {
            min-height: 70px !important; /* 稍微减小高度 */
            padding: 6px 10px !important;
        }
        
        /* 新增：移动端调整鼓励话语换行 */
        .stSuccess {
            font-size: 14px !important;
            line-height: 1.4 !important;
            padding: 12px !important;
            white-space: pre-line !important; /* 保留换行符 */
        }
        
        /* 新增：移动端调整鼓励话语中的标题大小 */
        .stSuccess strong {
            font-size: 15px !important;
            display: block;
            margin-bottom: 8px;
            white-space: normal !important;
        }
        
        /* 新增：确保文本在移动端正确换行 */
        .stSuccess .stMarkdown {
            white-space: pre-line !important;
            word-wrap: break-word !important;
            overflow-wrap: break-word !important;
        }
        
        /* 新增：移动端调整鼓励话语容器 */
        div[data-testid="stSuccess"] > div {
            white-space: pre-line !important;
            word-break: break-word !important;
        }
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

def show_results_interface():
    res = st.session_state.scorer.get_results()
    scores, details = res["scores"], res["details"]
    avg = lambda t: scores[t] / len([q for q in questions if q["type"] == t])
    avg_s, avg_w, avg_o, avg_t = avg("S"), avg("W"), avg("O"), avg("T")

    # 1️⃣ 总体分析
    st.header("📊 总体分析")
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("✅ 优势", f"{avg_s:.1f}/5.0", f"{scores['S']}分")
    with c2: st.metric("❌ 劣势", f"{avg_w:.1f}/5.0", f"{scores['W']}分")
    with c3: st.metric("🎯 机会", f"{avg_o:.1f}/5.0", f"{scores['O']}分")
    with c4: st.metric("⚠️ 威胁", f"{avg_t:.1f}/5.0", f"{scores['T']}分")

    st.markdown("---")
    if avg_s + avg_o > avg_w + avg_t:
        st.success("### 🎉 积极前景")
        st.write("你的外部机会与内部优势相结合，专升本成功几率较高！")
    else:
        st.warning("### ⚠️ 需要重点关注")
        st.write("你面临一些挑战，但只要针对性改进，完全有机会实现逆袭！")

    # 2️⃣ SWOT 矩阵 + 雷达图
    st.header("🎯 SWOT 矩阵")
    swot_labels = {
        'S': ["执行力", "组织力", "洞察力", "目标感", "进取心"],
        'W': ["依赖性", "拖延倾向", "信息局限", "考试焦虑", "韧性不足", "决策困难"],
        'O': ["支持系统", "榜样引导", "环境利好", "趋势匹配", "变革机会"],
        'T': ["同伴压力", "环境干扰", "时机紧迫", "竞争激烈"]
    }

    def get_high(t):
        return [swot_labels[t][i] for i, item in enumerate(details[t]) if item["score"] >= 4]

    high_S, high_W, high_O, high_T = get_high("S"), get_high("W"), get_high("O"), get_high("T")

    # 渲染象限
    def render_quadrant(col, label, title, avg_score, items):
        color = {"S": "#28a745", "W": "#dc3545", "O": "#17a2b8", "T": "#ffc107"}[label]
        icon = {"S": "✅", "W": "⚠️", "O": "🚀", "T": "⚡"}[label]
        with col:
            with st.container(border=True):
                st.markdown(f"### {icon} {title} ({label}) <small style='color:{color};'>{avg_score:.1f}/5.0</small>", unsafe_allow_html=True)
                if items:
                    tag_html = " ".join(
                        f'<span style="background:{color};color:white;padding:4px 10px;border-radius:12px;margin:2px;display:inline-block;font-size:14px;">{t}</span>'
                        for t in items
                    )
                    st.markdown(tag_html, unsafe_allow_html=True)
                else:
                    no_hint = {"S": "暂无明显优势", "W": "暂无明显劣势", "O": "暂无明显机会", "T": "暂无明显威胁"}
                    st.caption(no_hint[label])

    # 雷达图 · 科幻霓虹 + 官方发光（修复不可拖动问题）
    r = [avg_s, avg_o, avg_w, avg_t]
    theta = [" 优势(S)",  " 劣势(W)", " 威胁(T)"," 机会(O)"]  # 四角方位

    fig = go.Figure(go.Scatterpolar(
        r=r, theta=theta, mode='lines+markers+text',
        marker=dict(size=12, color="#00f5ff", line=dict(width=2, color="#ffffff")),
        line=dict(width=3, color="#00f5ff"),
        fill='toself', fillcolor="rgba(0, 245, 255, 0.15)",
        name="得分"
    ))

    # 四字发光大字体
    big_label_font = dict(color="white", size=22, shadow="0 0 5px #00f5ff, 0 0 10px #00f5ff")
    # 刻度数字原大
    tick_font = dict(color="white", size=14)

    fig.update_layout(
        polar=dict(
            bgcolor="rgba(0,0,0,0)",
            radialaxis=dict(
                range=[0, 5],
                tickfont=tick_font,          # 刻度数字
                gridcolor="rgba(0, 245, 255, 0.6)", gridwidth=1.5
            ),
            angularaxis=dict(
                rotation=135,
                direction="clockwise",
                tickfont=big_label_font,     # 只放大「优势(S)」等四字
                gridcolor="rgba(0, 245, 255, 0.6)", gridwidth=1.5
            )
        ),
        margin=dict(l=40, r=40, t=40, b=40),
        height=420,
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white"),
        # 添加以下配置禁用交互
        dragmode=False,
        hovermode=False
    )

    # 禁用缩放和旋转交互
    fig.update_layout(
        xaxis=dict(fixedrange=True),
        yaxis=dict(fixedrange=True)
    )

    # 在显示图表时禁用交互模式
    st.plotly_chart(fig, use_container_width=True, config={
        'displayModeBar': False,  # 隐藏模式栏
        'staticPlot': True,       # 静态图表
        'scrollZoom': False,      # 禁用滚动缩放
        'doubleClick': False,     # 禁用双击缩放
        'showTips': False,        # 禁用提示
        'displaylogo': False      # 隐藏logo
    })

    col_left, col_right = st.columns(2)
    render_quadrant(col_left, 'S', "优势", avg_s, high_S)
    render_quadrant(col_left, 'O', "机会", avg_o, high_O)
    render_quadrant(col_right, 'W', "劣势", avg_w, high_W)
    render_quadrant(col_right, 'T', "威胁", avg_t, high_T)

    # 3️⃣ 个性建议 - 修改为更符合学生的版本
    st.header("💡 学习策略建议")

    # 根据得分情况给出不同的学习建议和课程推荐
    if avg_s > 3.5 and avg_o > 3.5:
        st.success("🌟 优势突破型学习策略")
        st.write("""
        **你的优势明显且机会良好，建议采取：**
        - 发挥强项科目，建立信心优势
        - 利用现有资源，快速提升成绩
        - 设定较高目标，冲击重点院校
        - 保持学习节奏，避免骄傲松懈
        """)
        
        # 课程推荐 - 使用适当大小的标题
        st.markdown('<div class="course-recommendation-title">📚 新知教育课程推荐：全程班</div>', unsafe_allow_html=True)
        st.write("""
        适合基础扎实、升本目标明确的你！课程包含：
        - 春秋季周末公共基础+重难强化
        - 寒暑假专业课基础+强化集训
        - 考前全科总复习
        - OK网校全科配套网课
        - 新知题库刷题训练
        """)
        
    elif avg_s > 3.5 and avg_t > 3.5:
        st.warning("🛡️ 稳扎稳打型学习策略")
        st.write("""
        **基础扎实但挑战较多，建议采取：**
        - 巩固优势科目，确保基本盘稳定
        - 重点突破薄弱环节，补齐短板
        - 制定详细计划，按部就班执行
        - 建立学习小组，互相督促进步
        """)
        
        # 课程推荐 - 使用适当大小的标题
        st.markdown('<div class="course-recommendation-title">📚 新知教育课程推荐：VIP班</div>', unsafe_allow_html=True)
        st.write("""
        适合需要系统化指导的你！课程包含：
        - 春秋季周末公共基础+重难强化
        - 寒暑假VIP公共+专业特训营
        - **VIP考前全科冲刺培训营**
        - **VIP考前全科答疑特训**
        - OK网校全科配套网课
        - 新知题库刷题训练
        - **享受专属定向督学服务**
        """)
        
    elif avg_w > 3.5 and avg_o > 3.5:
        st.info("🚀 逆袭赶超型学习策略")
        st.write("""
        **机会很好但基础薄弱，建议采取：**
        - 抓住关键机会，重点投入时间
        - 寻求老师帮助，建立学习基础
        - 从易到难循序渐进，建立信心
        - 利用外部资源，弥补自身不足
        """)
        
        # 课程推荐 - 使用适当大小的标题
        st.markdown('<div class="course-recommendation-title">📚 新知教育课程推荐</div>', unsafe_allow_html=True)
        
        col_rec1, col_rec2 = st.columns(2)
        
        with col_rec1:
            st.markdown("""
            **登科集训营（仅限大三学生）**
            - 春秋季周末公共基础+重学强化
            - **暑期VIP公共+专业特训营**
            - **大三登科特训营**
            - VIP考前全科答疑特训
            - OK网校全科配套网课
            - 新知题库刷题训练
            """)
        
        with col_rec2:
            st.markdown("""
            **超能冲分班（适合各年级学生）**
            - 春秋季周末公共基础+重难强化
            - **暑期VIP公共+专业特训营**
            - **大三登科特训营**
            - **考前冲分急救营**
            - VIP考前全科答疑特训
            - OK网校全科配套网课
            - 新知题库刷题训练
            """)
        
        st.write("""
        **选择建议：**
        - 如果您是**大三学生**，时间紧迫需要快速提升，推荐**登科集训营**
        - 如果您希望系统打好基础，需要**沉浸式冲刺学习**，推荐**超能冲分班**
        """)
        
    else:
        st.error("💪 基础夯实型学习策略")
        st.write("""
        **当前挑战较多，建议采取：**
        - 从头开始打好基础，不贪多求快
        - 小步快跑，每天进步一点点
        - 寻求专业辅导，建立正确方法
        - 保持耐心毅力，相信厚积薄发
        """)
        
        # 课程推荐 - 使用适当大小的标题
        st.markdown('<div class="course-recommendation-title">📚 新知教育课程推荐：巅峰特训营</div>', unsafe_allow_html=True)
        st.write("""
        适合需要长期系统化提升的你！
        课程包含：
        - 春秋季周末公共基础+重难强化
        - **寒暑假VIP公共+专业特训营**
        - **大三登科特训营**
        - **VIP考前全科冲刺密训营**
        - VIP考前全科答疑特训
        - OK网校全科配套网课
        - 新知题库刷题训练
        """)

    # 具体学习建议
    st.subheader("📚 针对性学习建议")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **✅ 优势科目强化：**
        - 每天保持2小时优势科目练习
        - 整理错题本，避免重复错误
        - 尝试教授他人，加深理解
        
        **❌ 薄弱环节改进：**
        - 找出3个最薄弱知识点重点突破
        - 寻求新知教育老师一对一指导
        - 建立专项练习计划
        """)

    with col2:
        st.markdown("""
        **🎯 时间管理建议：**
        - 制定周学习计划表
        - 使用番茄工作法提高效率
        - 早晚各1小时黄金学习时间
        
        **🤝 资源利用建议：**
        - 加入**新知教育**专属学习小组，专业老师全程督学
        - 利用**小星学府**线上题库和网课，随时随地查漏补缺
        - 定期参加新知教育模拟考试，真实体验考场氛围
        - 预约新知教育一对一辅导，针对性解决学习难题
        """)

    # 课程对比表 - 优化后的美观卡片布局
    st.subheader("🏫 新知教育专升本课程体系")

    # 创建课程卡片
    courses = [
        {
            "name": "全程班",
            "icon": "🎯",
            "features": [
                "春秋季周末公共基础+重难强化",
                "寒暑假专业课基础+强化集训", 
                "考前全科总复习",
                "OK网校全科配套网课",
                "新知题库刷题训练"
            ],
            "target": "基础扎实、升本目标明确、需要清晰备考方向指导的考生",
            "price": "¥2980",
            "color": "#00f5ff",
            "note": "不含住宿费及额外200元综合服务费"
        },
        {
            "name": "VIP班",
            "icon": "⭐",
            "features": [
                "春秋季周末公共基础+重难强化",
                "寒暑假VIP公共+专业特训营",
                "**VIP考前全科冲刺培训营**",
                "**VIP考前全科答疑特训**",
                "OK网校全科配套网课",
                "新知题库刷题训练",
                "享受专属定向督学服务"
            ],
            "target": "升本小白0基础、无明确备考方向，需掌握全科系统化指导教学，定向细致化管学的考生",
            "price": "¥7480",
            "color": "#ff00ff",
            "note": "不含住宿费及额外500元综合服务费"
        },
        {
            "name": "登科集训营（仅限大三学生）",
            "icon": "🚀",
            "features": [
                "春秋季周末公共基础+重难强化",
                "**暑期VIP公共+专业特训营**",
                "**大三登科特训营**",
                "VIP考前全科答疑特训",
                "OK网校全科配套网课",
                "新知题库刷题训练",
                "享受专属定向督学服务"
            ],
            "target": "升本小白0基础，考前佛脚党，需要全科系统化指导教学，定向细致化管学的考生",
            "price": "¥7480",
            "color": "#00ffaa",
            "note": "不含住宿费及额外500元综合服务费"
        },
        {
            "name": "超能冲分班",
            "icon": "💪",
            "features": [
                "春秋季周末公共基础+重学强化",
                "**暑期VIP公共+专业特训营**",
                "**大三登科特训营**",
                "**考前冲分急救营**",
                "VIP考前全科答疑特训",
                "OK网校全科配套网课",
                "新知题库刷题训练",
                "享受专属定向督学服务"
            ],
            "target": "升本小白0基础，考前佛脚党，需要全科系统化指导教学，定向细致化管学、冲刺急救，沉浸式学习氛围的考生",
            "original_price": "￥10860",
            "discount_price": "¥9960",
            "has_discount": True,
            "color": "#ffaa00",
            "note": "不含住宿费及额外600元综合服务费"
        },
        {
            "name": "巅峰特训营",
            "icon": "🏆",
            "features": [
                "春秋季周末公共基础+重难强化",
                "**寒暑假VIP公共+专业特训营**",
                "**大三登科特训营**",
                "**VIP考前全科冲刺培训营**",
                "VIP考前全科答疑特训",
                "OK网校全科配套网课",
                "新知题库刷题训练",
                "享受全程专属定向督学服务"
            ],
            "target": "学习基础薄弱，自律性不强，需要超长课时保障，定向细致化督学；大一至大三全程科学化、系统化、高效化多轮递进式全面提升的考生",
            "original_price": "￥15960",
            "discount_price": "¥14460",
            "has_discount": True,
            "color": "#aa00ff",
            "note": "不含住宿费及额外800元综合服务费"
        }
    ]

    # 为每个课程创建美观的卡片
    for i, course in enumerate(courses):
        # 使用Streamlit原生组件创建卡片
        with st.container():
            # 卡片标题区域
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"""
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 24px;">{course['icon']}</span>
                    <h3 style="margin: 0; color: {course['color']}; 
                        text-shadow: 0 0 8px {course['color']};">
                        {course['name']}
                    </h3>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                if course.get('has_discount', False):
                    # 有优惠价的显示方式 - 原价划掉，显示优惠价
                    st.markdown(f"""
                    <div class="course-price-container" style="
                        background: linear-gradient(90deg, {course['color']}, #ff00ff);
                        color: #0f0c29;
                        padding: 8px 12px;
                        border-radius: 20px;
                        font-weight: bold;
                        text-align: center;
                        box-shadow: 0 0 10px {course['color']};
                        min-height: 80px;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                    ">
                        <div style="margin-bottom: 4px;">
                            <del style="font-size: 16px; opacity: 0.7;">{course['original_price']}</del>
                        </div>
                        <div style="display: flex; align-items: center; justify-content: center; gap: 8px; margin-bottom: 4px;">
                            <div class="course-price" style="font-size: 25px;">{course['discount_price']}</div>
                            <div style="font-size: 16px; font-weight: bold; background: rgba(255,255,255,0.5); padding: 2px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.8);">限时优惠</div>
                        </div>
                        <div style="font-size: 12px; opacity: 0.7; line-height: 1.2;">{course['note']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    # 普通价格的显示方式
                    st.markdown(f"""
                    <div class="course-price-container" style="
                        background: linear-gradient(90deg, {course['color']}, #ff00ff);
                        color: #0f0c29;
                        padding: 8px 12px;
                        border-radius: 20px;
                        font-weight: bold;
                        text-align: center;
                        box-shadow: 0 0 10px {course['color']};
                        min-height: 80px;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                    ">
                        <div class="course-price" style="font-size: 25px; margin-bottom: 4px;">{course['price']}</div>
                        <div style="font-size: 12px; opacity: 0.7; line-height: 1.2;">{course['note']}</div>
                    </div>
                    """, unsafe_allow_html=True)
            
            # 适合学员
            st.info(f"**适合学员:** {course['target']}")
            
            # 课程内容 - 使用HTML直接渲染以确保橙色生效
            st.markdown("**课程内容:**")
            for feature in course['features']:
                # 将Markdown加粗转换为HTML加粗并添加亮青色样式
                html_feature = feature.replace("**", "<strong style='color: #00FFFF; text-shadow: 0 0 5px rgba(0, 255, 255, 0.7);'>").replace("**", "</strong>")
                st.markdown(f"• {html_feature}", unsafe_allow_html=True)
            
            # 卡片分隔线
            if i < len(courses) - 1:
                st.markdown("---")

    st.caption("*以上为各个班次大致课程体系内容，具体课程安排以辅导员课表通知为准")

    # 鼓励话语 - 优化移动端换行显示
    st.success("""
    **💫 给亲爱的同学：**
    
    专升本是一场马拉松，不是短跑。
    每天进步一点点，坚持下去，
    你一定能到达理想的彼岸！
    
    新知教育陪你一起冲刺本科梦想！
    """)

    st.markdown("---")
    if st.button("🔄 重新开始测试", use_container_width=True, type="primary"):
        st.session_state.current_question = 0
        st.session_state.answers = [None] * len(questions)
        st.session_state.scorer = SWOTScorer()
        st.session_state.test_complete = False
        st.rerun()

if __name__ == "__main__":
    main()