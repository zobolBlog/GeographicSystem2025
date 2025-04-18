import streamlit as st
import pandas as pd
import numpy as np
from st_wordcloud import st_wordcloud


# layout: 5:5 双层布局
import streamlit as st
import pandas as pd
import numpy as np
from st_wordcloud import st_wordcloud
import plotly.express as px

# layout: 5:5 双层布局
col0,col1, col2 = st.columns([1,100,1])
with col1:
    contaner1_first = st.container(border=True,height=600)

with col1:
    contaner2_first = st.container(border=True,height=600)

with contaner1_first:
    # 假设这是开封非遗十大受欢迎项目的数据，你可以根据实际情况修改
    data = {
        '非遗项目': ['开封汴绣', '朱仙镇木版年画', '开封盘鼓', '马豫兴桶子鸡', '开封夜市饮食文化',
                     '汴京灯笼张', '摞石锁', '尉氏杨家拳', '通许麒麟舞', '杞县肘歌'],
        '受欢迎程度': [9.2, 9.0, 8.8, 8.5, 8.2, 8.0, 7.8, 7.5, 7.2, 7.0]
    }

    chart_data = pd.DataFrame(data)

    with st.container() as contaner1_first:
        st.markdown("<font size=5> 开封非遗十大受欢迎项目 </font>", unsafe_allow_html=True)
        fig = px.line(chart_data, x='非遗项目', y='受欢迎程度', text='受欢迎程度')
        fig.update_xaxes(tickangle=0)  # 设置 x 轴文字水平
        st.plotly_chart(fig)

    
with contaner2_first:
    data = {
        '级别': ['国家级', '省级', '市级'],
        '数量': [9, 44, 218]
    }
    chart_data = pd.DataFrame(data)

    with st.container() as contaner2_first:
        st.markdown("<font size=5> 开封市非物质文化遗产名录级别 </font>", unsafe_allow_html=True)
        # 绘制饼状图
        fig = px.pie(chart_data, names='级别', values='数量', hole=0.3)
        st.plotly_chart(fig)




import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

# 地图模块：天地图地图源的key
tdt_key = "cb06c24e85ad961f9320591bed31e843"

folium_map = folium.Map(
         location=[34.8041, 114.3432],
         zoom_start=16
    )
     # 渲染地图并获取交互数据（关键：要保存返回的 map_data）

    # 添加天地图矢量图层
tdt_vec_url = f"http://t0.tianditu.gov.cn/DataServer?T=img_w&x={{x}}&y={{y}}&l={{z}}&tk={tdt_key}"
folium.TileLayer(
        tiles=tdt_vec_url,
        attr='天地图',
        name='天地图矢量图'
    ).add_to(folium_map)

    # 添加天地图注记图层
tdt_cva_url = f"http://t0.tianditu.gov.cn/DataServer?T=cia_w&x={{x}}&y={{y}}&l={{z}}&tk={tdt_key}"
folium.TileLayer(
        tiles=tdt_cva_url,
        attr='天地图',
        name='天地图注记'
    ).add_to(folium_map)

# 创建一个坐标点的数据集
heritage_locations = [
        [34.6164, 114.2611,3],#朱仙镇木板年画
        [34.8100, 114.3360,3],#开封盘鼓
        [34.7981, 114.3568,3],#汴京灯笼张
        [34.7905, 114.3434,3],#汴绣
        [34.7922, 114.3488,3],#大相国寺梵乐
        [34.8296, 114.8138,3],#兰考麒麟舞
        [34.7891, 114.3728,3],#二夹弦
        [34.8091, 114.3467,3],#撂石锁
        [34.5473, 114.7798,2],#杞人忧天传说
        [34.8398, 114.8209,2],#卧拐秧歌
        [34.4155, 114.1901,2],#罗卷戏
        [34.8053, 114.8159,2],#仪封三弦书
        [34.7983, 114.3091,2],#北宋官瓷烧制技艺
        [34.7943, 114.3228,2],#开封义兴牌匾制作技艺
        [34.8057, 114.2985,2],#开封第一楼小笼灌汤包子
        [34.7924, 114.3087,2],#开封马豫兴桶子鸡
        [34.8123, 114.3390,2],#开封又一新糖醋软熘鲤鱼焙面
        [34.8261, 114.7911,2],#秋油腐乳
        [34.3991, 114.1713,2],#洧川豆腐 
        [34.8212, 114.2906,2],#针灸铜人
        [34.6071, 114.2563,2],#朱仙镇五香豆腐干
        [34.8007, 114.4235,2],#刘陈铺齐氏骨科
        [34.8239, 114.3279,2],#黄派查拳
        [34.8196, 114.3147,2],#吹糖人
        [34.8310, 114.3529,2],#滕派蝶画
        [34.8160, 114.3763,2],#许氏屋兽与砖雕
        [34.8046, 114.3474,2],#渔鼓道情 
    ]
 
# 创建一个 HeatMap 对象
heatmap = HeatMap(heritage_locations,radius=35)
 
# 将 HeatMap 对象添加到地图上
heatmap.add_to(folium_map)



# 使用HTML设置字体大小为30px
html = f'<p style="font-size: 30px;">开封市热力图</p>'
st.write(html, unsafe_allow_html=True)

map_data = st_folium(
         folium_map,
         use_container_width=True,
         height=1000
     )