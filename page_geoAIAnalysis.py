import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
import geopandas as gpd
from st_audiorec import st_audiorec
from audio_recorder_streamlit import audio_recorder
from streamlit_mic_recorder import mic_recorder, speech_to_text
from aip import AipSpeech
import soundfile as sf
import io
import numpy as np
import wave

#
APP_ID = '118446067'
API_KEY = 'RQuDdCQY2R4fNSPLFKfE8kRG'
SECRET_KEY = 'qKOKgBAHBhF5Ac9iJyspD5uzijj6o1KW'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 地图模块：天地图地图源的key
tdt_key = "cb06c24e85ad961f9320591bed31e843"

# UI模块：设置col的边框
st.markdown(
    """
    <style>
    .stColumn {
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 10px;
    }
    /* 选择 Streamlit 的列容器 --------- 4.11新加的功能*/
    .stHorizontalBlock > div {
        padding: 0;
        margin: 0;
        border: none; /* 去除边框 */
        box-shadow: none; /* 去除阴影 */
    }
    /* 去掉列之间的间距 */
    .stHorizontalBlock {
        gap: 0;
    }
    /* 去除 [data-testid="stVerticalBlockBorderWrapper"] 的背景颜色和内边距 */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: transparent;
        padding: 2px;
    }
    
    /* --------- 4.11新加的功能 */
    </style>
    """,unsafe_allow_html=True
)

# UI模块：设置页面布局，分为左、中
col1, col2 ,col3= st.columns([8, 6,1.5])

# UI模块：左为地图栏，右为图表栏
with col1:
         # 创建一个 Folium 地图对象，开封为中心
    #folium_map = folium.Map(location=[34.8041, 114.3432], zoom_start=13)
     # 初始化 session_state（确保首次运行时有默认值）
    if "map_center" not in st.session_state:
        st.session_state.map_center = [34.8041, 114.3432]  # 开封初始中心坐标
    if "map_key" not in st.session_state:
        st.session_state.map_key = 0  # 动态 Key 计数器
     # 创建 Folium 地图对象（基于 session_state 的当前中心）
    folium_map = folium.Map(
         location=st.session_state.map_center,
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

    plugin_click_LatLon = folium.LatLngPopup()
    folium_map.add_child(plugin_click_LatLon)


    #添加非遗点位
    heritage_locations = [
        [34.6164, 114.2611],#朱仙镇木板年画
        [34.8100, 114.3360],#开封盘鼓
        [34.7981, 114.3568],#汴京灯笼张
        [34.7905, 114.3434],#汴绣
        [34.7922, 114.3488],#大相国寺梵乐
        [34.8296, 114.8138],#兰考麒麟舞
        [34.7891, 114.3728],#二夹弦
        [34.8091, 114.3467],#撂石锁
        [34.5473, 114.7798],#杞人忧天传说
        [34.8398, 114.8209],#卧拐秧歌
        [34.4155, 114.1901],#罗卷戏
        [34.8053, 114.8159],#仪封三弦书
        [34.7983, 114.3091],#北宋官瓷烧制技艺
        [34.7943, 114.3228],#开封义兴牌匾制作技艺
        [34.8057, 114.2985],#开封第一楼小笼灌汤包子
        [34.7924, 114.3087],#开封马豫兴桶子鸡
        [34.8123, 114.3390],#开封又一新糖醋软熘鲤鱼焙面
        [34.8261, 114.7911],#秋油腐乳
        [34.3991, 114.1713],#洧川豆腐 
        [34.8212, 114.2906],#针灸铜人
        [34.6071, 114.2563],#朱仙镇五香豆腐干
        [34.8007, 114.4235],#刘陈铺齐氏骨科
        [34.8239, 114.3279],#黄派查拳
        [34.8196, 114.3147],#吹糖人
        [34.8310, 114.3529],#滕派蝶画
        [34.8160, 114.3763],#许氏屋兽与砖雕
        [34.8046, 114.3474],#渔鼓道情 
    ]

    heritage_texts = [
    "朱仙镇木板年画",
    "开封盘鼓",
    "汴京灯笼张",
    "汴绣",
    "大相国寺梵乐",
    "麒麟舞",
    "二夹弦",
    "撂石锁",
    "杞人忧天传说",
    "卧拐秧歌",
    "罗卷戏",
    "仪封三弦书",
    "北宋官瓷烧制技艺",
    "开封义兴牌匾制作技艺",
    "开封第一楼小笼灌汤包子",
    "开封马豫兴桶子鸡",
    "开封又一新糖醋软熘鲤鱼焙面",
    "秋油腐乳",
    "洧川豆腐",
    "针灸铜人",
    "朱仙镇五香豆腐干",
    "刘陈铺齐氏骨科",
    "黄派查拳",
    "吹糖人",
    "滕派蝶画",
    "许氏屋兽与砖雕",
    "渔鼓道情",
    ]
    heritage_texts_contents = [
        "朱仙镇木板年画是中国四大年画之一，具有鲜明的地方特色和浓厚的民俗文化气息。",
        "开封盘鼓是河南省开封市的传统民间艺术，具有悠久的历史和独特的艺术风格。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
        "汴京灯笼张是开封市的传统手工艺品，以其精美的工艺和丰富的文化内涵而闻名。",
    ]



    heritage_imgs_urls =[
        "https://www.ihchina.cn/r4/cd/i/2018/01/10/e5c7016481e04ada9b54423ea4ee7525.jpg",
        "https://www.kaifeng.gov.cn/kfsrmzfwz/gjjfy/1765600892434583552/UcCntrSo.jpg",
        "https://so1.360tres.com/t01b2d7f1ab54d79ed6.jpg",
        "http://www.wenhua666.com/resource/images/0f96747d838946e29fd02461f65c0e2f_9.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.kaifeng.gov.cn/kfsrmzfwz/gjjfy/1765600892434583552/UcCntrSo.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.kaifeng.gov.cn/kfsrmzfwz/gjjfy/1765600892434583552/UcCntrSo.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.kaifeng.gov.cn/kfsrmzfwz/gjjfy/1765600892434583552/UcCntrSo.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.kaifeng.gov.cn/kfsrmzfwz/gjjfy/1765600892434583552/UcCntrSo.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
        "https://www.ihchina.cn/niansu/images/zhangDengJieCai/bjdlz6.jpg",
    ]   
          
    
    index=0
    while index < len(heritage_locations): 
        folium.Marker(location=heritage_locations[index], 
                      popup=heritage_texts[index], 
                      tooltip=heritage_texts[index],
                      icon=folium.DivIcon(
                          html=(
                              '<div style="line-height: 12px; font-size: 10px; color: white;">'
                              + heritage_texts[index] +
                              '</div>'
                          )
                      )).add_to(folium_map)
        
        html = f'''
                <h3>{heritage_texts[index]}</h3>
                <p>
                    {heritage_texts_contents[index]}
                </p>
                <p>
                <img src="{heritage_imgs_urls[index]}"  style="width:100%;">
                </p>
                '''      
        folium.Marker(location=heritage_locations[index],  
                      popup = folium.Popup(html=folium.IFrame(html=html, width=200, height=200), max_width=250),
                      tooltip=heritage_texts[index]).add_to(folium_map)             
        index +=1
  
    map_data = st_folium(
         folium_map,
         key=f"map_{st.session_state.map_key}",  # 动态 Key,  # 必须指定唯一 key 用于状态追踪
         use_container_width=True,
         height=800
     )


    # 目标位置
    target_location1 = [34.8095, 114.3357]#开封盘鼓
    target_location2 = [34.6164, 114.2611]#木板年画
    target_location3 = [34.7905, 114.3434]#汴绣


    
    #map_data = st_folium(folium_map, use_container_width=True,height=600)
        

heritage_html_contents = {
    "朱仙镇木板年画": "朱仙镇木版年画是中国古老的传统工艺品之一。作为中国木版年画的鼻祖， [1]主要分布于河南省开封、朱仙镇及其周边地区。朱仙镇木版年画构图饱满，线条粗犷简炼，造型古朴夸张，色彩新鲜艳丽。",
    "开封盘鼓": "开封盘鼓原名“大鼓”，是开封市特有的一种民间广场鼓舞乐，它与宋代至明代四百年间流传于开封的迓鼓乐密切相关。开封盘鼓一般在集市、祭祀或节庆活动中表演，清代曾广泛用于抗旱求雨等民俗仪式。开封盘鼓有十几人至几百人的表演队伍，表演者在令旗手指挥下，或击打挎在身前的大鼓，或击打大镲、马锣等铜器，在行进中边击边舞。",
    "汴京灯笼张": "灯彩（汴京灯笼张），河南省开封市传统美术，国家级非物质文化遗产之一。汴京灯笼张是艺人张金汉的祖传技艺，其造型和扎糊技艺源于开封民间的彩灯制作传统。据《开封县志》记载，汴京灯笼张始传于清末，其彩灯作品既有宫廷花灯的古雅、庄重与华贵，又有民间艺术的活泼以及浓郁的生活气息，主要品种有“龙凤呈祥灯”“莲生贵子灯”“牡丹富贵灯”“吉祥高照灯”等。",
    "汴绣": "汴绣也称“宋绣”，是流行于河南开封一带的传统刺绣艺术，因产生于北宋的都城汴京开封而得名。北宋时期汴京刺绣业兴盛，已达到较高的技艺水平，故《东京梦华录》中有“金碧相射，锦绣交辉”之誉。宋钦宗靖康二年（1127年），金兵攻破开封，宋室南迁，后复值兵祸水患，开封城市经济一蹶不振，刺绣业逐渐衰落。新中国建立后，几代汴绣艺人努力发掘整理宋代刺绣技艺,并借鉴苏绣、湘绣等其他绣种的长处,总结出36种汴绣针法,使汴绣工艺日臻完善成熟。"
}

heritage_html_img = {
    "朱仙镇木板年画": "https://www.ihchina.cn/r4/cd/i/2018/01/10/e5c7016481e04ada9b54423ea4ee7525.jpg",
    "开封盘鼓": "https://www.kaifeng.gov.cn/kfsrmzfwz/gjjfy/1765600892434583552/UcCntrSo.jpg",
    "汴京灯笼张": "https://so1.360tres.com/t01b2d7f1ab54d79ed6.jpg",
    "汴绣": "http://www.wenhua666.com/resource/images/0f96747d838946e29fd02461f65c0e2f_9.jpg"
}
with col2:
    upper, lower = st.container(border=True,height=500), st.container(border=True,height=250)

with col3:
    import base64
    import streamlit.components.v1 as components

    # 引入 Tailwind CSS
    st.markdown("""
    <script src="https://cdn.tailwindcss.com"></script>
    """, unsafe_allow_html=True)

    # 获取 GIF 文件的路径
    gif_path = "img1/2025-04-11T03_48_08.178Z-586045.gif"

    # 将 GIF 文件转换为 Base64 编码
    with open(gif_path, "rb") as gif_file:
        encoded_gif = base64.b64encode(gif_file.read()).decode()
    gif_url = f"data:image/gif;base64,{encoded_gif}"

    # 使用 Tailwind CSS 样式包裹 GIF 图
    html_code = f"""
    <style>
        .custom-gif-size {{
            width: 100px; /* 设置图片宽度为 300px */
            height: auto; /* 保持图片的原始纵横比 */
            margin-top: 460px;  /* 高度 */
        }}
        </style>
    <div class='bg-gray-100 p-4 rounded-md'>
        <img src="{gif_url}" alt="GIF 动图" class='custom-gif-size'>
    </div>
    """

    # 使用 st.components.v1.html 嵌入 HTML 代码
    components.html(html_code, height=800)


def convert_to_mono(audio_bytes):
    """
    使用 numpy 将双声道音频数据转换为单声道。
    
    :param audio_bytes: 原始音频数据（字节流）
    :return: 单声道音频数据（字节流）
    """
    # 将字节流转换为 numpy 数组
    audio_array = np.frombuffer(audio_bytes, dtype=np.int16)
    
    # 检查是否为双声道
    if len(audio_array.shape) == 1 and len(audio_array) % 2 == 0:
        # 将双声道数据转换为单声道（取左右声道平均值）
        mono_audio = audio_array.reshape(-1, 2).mean(axis=1).astype(np.int16)
    else:
        # 如果已经是单声道，直接返回
        mono_audio = audio_array
    
    # 返回单声道音频数据
    return mono_audio.tobytes()

with lower:
      # 语音转文本


    audio_bytes = audio_recorder(text="基于百度-短语音识别大模型的交互助手：",sample_rate=8000)
    if audio_bytes:

        mono_audio_bytes = convert_to_mono(audio_bytes)
        st.audio(mono_audio_bytes, format="audio/wav")
        result = client.asr(mono_audio_bytes, 'wav', 8000, {'dev_pid': 1537,})

        #4.11添加内容


        # 构建 HTML 字符串来设置文本颜色
        html_string = f'<p style="color: red;">识别结果2：{result["result"][0]}</p>'


        if result['err_no'] == 0:

            # 使用 st.write 并设置 unsafe_allow_html=True 来渲染 HTML
            st.write(html_string, unsafe_allow_html=True)






            if "开封盘鼓" in str(result["result"][0]):
                with upper:
                    st.title("开封盘鼓")
                    st.markdown(heritage_html_contents["开封盘鼓"], unsafe_allow_html=True)
                    st.image("https://www.kaifeng.gov.cn/kfsrmzfwz/gjjfy/1765600892434583552/UcCntrSo.jpg",use_container_width="true")
                #target_location = [34.8095, 114.3357]
                st.session_state.map_center = target_location1
                st.session_state.map_key = 1  # 修改 Key 值3
                st.rerun()
            if "朱仙镇木版年画" in str(result["result"][0]):
                with upper:
                    st.title("朱仙镇木版年画")
                    st.markdown(heritage_html_contents["朱仙镇木板年画"], unsafe_allow_html=True)
                    st.image("https://www.ihchina.cn/r4/cd/i/2018/01/10/e5c7016481e04ada9b54423ea4ee7525.jpg",use_container_width="true")
                target_location = [34.8095, 114.3357]
                st.session_state.map_center = target_location2
                st.session_state.map_key = 1  # 修改 Key 值3
                st.rerun()
            if "汴绣" in str(result["result"][0]):
                with upper:
                    st.title("汴绣")
                    st.markdown(heritage_html_contents["汴绣"], unsafe_allow_html=True)
                    st.image("http://www.wenhua666.com/resource/images/0f96747d838946e29fd02461f65c0e2f_9.jpg",use_container_width="true")
                target_location = [34.8095, 114.3357]
                st.session_state.map_center = target_location3
                st.session_state.map_key = 1  # 修改 Key 值3
                st.rerun()  
         
         





        else:
            print("识别错误：", result['err_msg'])


    
    
  

    


               
# 检测地图点击事件
if map_data and 'last_object_clicked' in map_data:
    clicked_marker_name = map_data['last_object_clicked_tooltip']

    if clicked_marker_name == "朱仙镇木板年画":
        
            with upper:
                st.title(clicked_marker_name)
                st.markdown(heritage_html_contents[clicked_marker_name], unsafe_allow_html=True)
                st.image("https://www.ihchina.cn/r4/cd/i/2018/01/10/e5c7016481e04ada9b54423ea4ee7525.jpg",use_container_width="true")

            #with lower:
                   # st.write("这是下半部分的内容")

    if clicked_marker_name == "开封盘鼓":
        with col2:
           
            with upper:
                st.title(clicked_marker_name)
                st.markdown(heritage_html_contents[clicked_marker_name], unsafe_allow_html=True)
                st.image("https://www.kaifeng.gov.cn/kfsrmzfwz/gjjfy/1765600892434583552/UcCntrSo.jpg",use_container_width="true")

           


    if clicked_marker_name == "汴京灯笼张":
            with col2:
                
                with upper:
                    st.title(clicked_marker_name)
                    st.markdown(heritage_html_contents[clicked_marker_name], unsafe_allow_html=True)
                    st.image("https://so1.360tres.com/t01b2d7f1ab54d79ed6.jpg",use_container_width="true")

                #with lower:
                    #wav_audio_data = st_audiorec()
                    #if wav_audio_data is not None:
                    #    st.audio(wav_audio_data, format='audio/wav')

    if clicked_marker_name == "汴绣":
        with col2:
            with upper:
                st.title(clicked_marker_name)
                st.markdown(heritage_html_contents[clicked_marker_name], unsafe_allow_html=True)
                st.image("http://www.wenhua666.com/resource/images/0f96747d838946e29fd02461f65c0e2f_9.jpg",use_container_width="true")
