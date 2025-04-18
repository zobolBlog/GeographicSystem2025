import streamlit as st 
import folium
from streamlit_folium import st_folium
from openai import OpenAI
import matplotlib.pyplot as plt
import numpy as np
import os

# 0.1 系统：设置环境变量隐藏 Deploy 按钮
st.set_option("client.toolbarMode","viewer")

# 1.0 UI模块：设置页面配置
st.set_page_config(layout="wide", page_title="基于人工智能的开封市非物质文化遗产地理信息智能分析平台")

# 1.1 UI模块：隐藏右上角的Deploy图标
st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
            
        [data-testid="stSidebarNavItems"] {
                padding-top: 2rem;
            } /*顶部内边距*/
            [data-testid="stSidebarUserContent"] {
                    padding: 1rem 1.5rem 3rem;
        } /*侧边栏顶部、左侧&右侧、底部内边距*/
    </style>
            """
   , unsafe_allow_html=True)

st.html(
    """
    <style>
        .stApp {
                background-image: url("https://p1.itc.cn/q_70/images03/20231018/dad56facc84d461586190472dd13ed70.jpeg");
                background-size: cover;
            }
        [data-testid="stVerticalBlockBorderWrapper"] {
                background-color: rgba(255, 255, 255, 0.75);
                padding: 0.5rem;
            }
        [data-testid="stVerticalBlockBorderWrapper"]>div {
                background-color: rgba(255, 255, 255, 1);
            }
</style>
    """
)


# UI：设置标题图片
with st.container():
    st.image("img/title2.jpg",use_container_width="true") 

# Layout:设置导航栏
pages = {
    "开封市非物质文化遗产地理信息智能分析平台": [
        st.Page("page_geoAIAnalysis.py", title="声启遗境：开封非遗AI语音交互信息平台"),
        st.Page("page_geoAIAssisant.py", title="智享非遗：开封非遗AI小助手"),
        st.Page("page_geoAIDataVis.py", title="慧览非遗：开封非遗大数据可视化平台"),
        st.Page("page_geoAIlocation.py", title="寻迹非遗：开封非遗AI旅游推荐系统"),
    ],
     "开封非物质文化遗产档案": [
        st.Page("page_heritage1.py", title="朱仙镇木版年画"),
        st.Page("page_heritage2.py", title="开封盘鼓"),
        st.Page("page_heritage3.py", title="汴京灯笼张"),
        st.Page("page_heritage4.py", title="汴绣"),
        st.Page("page_heritage5.py", title="大相国寺梵乐"),
        st.Page("page_heritage6.py", title="麒麟舞"),
        st.Page("page_heritage7.py", title="二夹弦"),
        st.Page("page_heritage8.py", title="撂石锁"),
        st.Page("page_heritage9.py", title="杞人忧天传说"),
        st.Page("page_heritage10.py", title="马大吹糖人"),
        st.Page("page_heritage11.py", title="马豫兴桶子鸡"),
        st.Page("page_heritage12.py", title="沙家牛肉"),
    ],
}



pg = st.navigation(pages,expanded=True)
pg.run()