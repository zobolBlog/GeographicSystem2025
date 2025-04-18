import streamlit as st
import pandas as pd
import numpy as np
from openai import OpenAI
import folium
from streamlit_folium import st_folium
import requests

#大模型
volcengine_api_key = "aa26b4cf-b087-4659-a937-99b236f9b5e6"
volcengine_client = OpenAI(
        # 此为默认路径，您可根据业务所在地域进行配置
        base_url="https://ark.cn-beijing.volces.com/api/v3",
        # 获取您的 API Key
        api_key=volcengine_api_key,
        )

def volcengine_client_request(user_message):
    completion = volcengine_client.chat.completions.create(
        # 指定您创建的方舟推理接入点 ID
        model="ep-20250328200027-vt64n",
        messages=[
            {"role": "user", "content": user_message}
        ],
    )
    return completion.choices[0].message.content


# 地图模块：天地图地图源的key
tdt_key = "cb06c24e85ad961f9320591bed31e843"

def get_transit_route(orig, dest, style=0):
    """
    调用天地图公交规划 API 获取交通规划路线。
    
    :param orig: 起点坐标（经度,纬度），例如 "114.3432,34.8041"
    :param dest: 终点坐标（经度,纬度），例如 "114.3568,34.7981"
    :param style: 公交类型0：推荐，1：少换乘，2：少步行，3：不坐地铁）
    :return: 交通规划路线的文本描述
    """
    # 构造请求 URL
    url = f"http://api.tianditu.gov.cn/transit?type=busline&postStr={{\"startposition\":\"{orig}\",\"endpositio\":\"{dest}\",\"linetype\":\"{style}\"}}&tk={tdt_key}"

    # 示例 URL
    example_url = f"http://api.tianditu.gov.cn/transit?type=busline&postStr={{\"startposition\":\"116.427562,39.939677\",\"endposition\":\"116.349329,39.939132\",\"linetype\":\"0\"}}&tk={tdt_key}"

    print(example_url)
    # 发送请求
    response = requests.get(example_url)
    
    # 检查响应状态
    if response.status_code == 200:
        data = response.json()
        if data.get("status") == 0:  # 请求成功
            routes = data.get("result", {}).get("routes", [])
            if routes:
                # 提取第一条路线
                return routes[0].get("description", "未找到路线描述")
            else:
                return "未找到合适的公交路线。"
        else:
            return f"请求失败，错误信息：{data.get('msg', '未知错误')}"
    else:
        return f"请求失败，HTTP状态码：{response.status_code}"







# layout: 5:5 双层布局
col1, col2 = st.columns([5, 5])
with col1:
    contaner1 = st.container(border=True,height=800)
with col2:
    contaner2 = st.container(border=True,height=800)

with contaner1:
    options = st.multiselect(
        '基于Doubao-1.5-thinking-pro大模型的新一代旅游计划定制AI，选择你的出行情况',
        ['单人', '家庭', '情侣', '学生','公司团建','穷游', '驾车', '美食', '文化', '购物', '运动', '龙亭区', '祥符区'],
        ['学生', '美食'])

    if st.button("智能制定旅游计划"):
        if 'generated' not in st.session_state:
            st.session_state['generated'] = []
        if 'past' not in st.session_state:
            st.session_state['past'] = []
        user_input = "请制定开封旅游计划,涉及非物质文化遗产非遗盘鼓,400字," + ",".join(options)
        if user_input:
            output=volcengine_client_request(user_input)
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)

        if st.session_state['generated']:
            for i in range(len(st.session_state['generated'])-1, -1, -1):
                #msg = st.chat_message("user", avatar="img/assisant1.jpg")
                #msg.write(st.session_state['past'][i])
                msg2 = st.chat_message("ai", avatar="img/assisant2.jpg")
                msg2.write(st.session_state['generated'][i])


with contaner2:
 # 创建一个 Folium 地图对象，开封为中心
    folium_map = folium.Map(location=[34.8041, 114.3432], zoom_start=13)

    # 添加天地图矢量图层
    tdt_vec_url = f"http://t0.tianditu.gov.cn/DataServer?T=vec_w&x={{x}}&y={{y}}&l={{z}}&tk={tdt_key}"
    folium.TileLayer(
        tiles=tdt_vec_url,
        attr='天地图',
        name='天地图矢量图'
    ).add_to(folium_map)

    # 添加天地图注记图层
    tdt_cva_url = f"http://t0.tianditu.gov.cn/DataServer?T=cva_w&x={{x}}&y={{y}}&l={{z}}&tk={tdt_key}"
    folium.TileLayer(
        tiles=tdt_cva_url,
        attr='天地图',
        name='天地图注记'
    ).add_to(folium_map)

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
                              '<div style="line-height: 12px; font-size: 10px; color: black;">'
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
  

    plugin_click_LatLon = folium.LatLngPopup()
    folium_map.add_child(plugin_click_LatLon)
    
    map_data = st_folium(folium_map, use_container_width=True,height=600)


