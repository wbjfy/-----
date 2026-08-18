# Streamlit是一个开源的Python库，专为数据工程师及机器学习工程师设计，用来快速基于Python代码构建交互式的web网站
# 官方官网：https://streamlit.io

# 1、安装streamlit: pip install streamlit
# 2、再python文件中引入streamlit模块
# 3、基于streamlit中提供的API来构建Web应用
# 4、运行程序:streamlit run xxxx.py
import streamlit as st

# 设置页面配置项
st.set_page_config(
    page_title="Streamlit入门", # 标题
    page_icon="🧊", #图标
    layout="wide", #布局
    initial_sidebar_state="expanded", #侧边栏状态
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


# 大标题
st.title("Streamlit 入门演示")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")

# 段落

st.write('动态漫方向：学ComfyUI搭角色一致性工作流，配合AE做细腻动画小说推文方向：练“黄金3秒”开头，用冲突画面抓眼球')
st.write('Midjourney用cref角色参考 + seed固定')
st.write('或用剪映拉长静止画面配合配音，规避口型问题')

# 图片
# st.image('图片路径')

# 音频
# st.audio('音频路径')

# 视频
# st.video('视频路径')

# Logo
# st.logo('图片路径')   出现在左上角

# 表格
studnet_data = {"姓名":["王林",'2','3','5','4'],
                "学号":['4124','32141','12341','51325','51235']}
st.table(studnet_data)

# 输入框
# 普通输入框
name = st.text_input('请输入姓名')
st.write(name)

# 密码输入框
password = st.text_input("请输入密码",type = "password")
st.write(password)

# 单选按钮
gender = st.radio("请输入您的性别",['男','女','未知'])
st.write(gender)