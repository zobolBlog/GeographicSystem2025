"https: // img601.yun300.cn / repository / image / b980f237…53.png?tenantId = 297708 & viewType = 1 & k = 1724381652000"
import streamlit as st
import streamlit.components.v1 as components

# 定义一个简单的 HTML 页面，去除外部资源引用
html_content = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <title>开封市沙家牛肉</title>
    <meta name="keywords" content=",,,开封市沙家牛肉" />
    <meta name="description" content="开封市继中朱仙镇木板年画社创建于明末清初，是 朱仙镇著名的年画老店之一。万同老店年画主要产品有：门神、财神、灶神、神话故事、戏曲年画等，它构图饱满、线条粗犷、色彩艳丽、久不褪色、形象夸张，采用传统手工水色套印，被誉为“中华绝活”，是古版年画中的精品。电话：86-0371-26711980" />
    <meta name="baidu-site-verification" content="qf5YGeha33" />
    <link rel="shortcut icon" type="image/x-icon" href="http://www.zxznianhua.com/ico/favicon.ico?1073435635" />
    <style>
        /* 可以在这里添加一些基本的样式 */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        .head {
            background-color: #000; /* 设置背景颜色为黑色 */
            color: #fff; /* 设置文字颜色为白色 */
            display: flex; /* 使用弹性布局 */
            align-items: center; /* 垂直居中对齐 */
            padding: 10px;
            height: 15px;

            }
        .welcolm {
            padding-left: 30px; /* 让文字向右偏移20px，可按需调整 */
            font-size: 10px;
        }
       .logo img {
            max-width: 100%;
            height: auto;
            padding-left: 0px; /* 让文字向右偏移20px，可按需调整 */
        }
       .topbanner {
            width: 100%;
            overflow: hidden;
        }
       .banner ul {
            list-style-type: none;
            margin: 0;
            padding: 0;
            display: flex;
        }
       .banner li {
            min-width: 100%;
        }
       .banner img {
            width: 100%;
            height: auto;
        }
    </style>
</head>
<body>
    <!-- 公共头部包含 -->
    <div class="head">
        <div id="header">
            <div class="welcolm fl"><p>开封汴绣</p></div>
        </div>
    </div>
    <div id="header">
        <div class="top clearfix">
            <div class="logo">
                <img alt="" src="https: // img601.yun300.cn / repository / image / b980f237…53.png?tenantId = 297708 & viewType = 1 & k = 1724381652000" />
            </div>
            <div class="topLink">
            </div>
        </div>
    </div>
    <!-- 首页banner -->
    <div class="topbanner">
        <div class="banner">
            <ul class="bb">
                <li>
                    <a title="开封木版年画">
                        <img src="https://n.sinaimg.cn/translate/20160919/vFex-fxvyqwe0157191.jpg" alt="开封木版年画" width="1920" height="670" />
                    </a>
                </li>
                <li>
                    <a title="朱仙镇年画">
                        <img src="http://www.zxznianhua.com/data/images/banner/20170315165302_697.jpg" alt="朱仙镇年画" width="1920" height="670" />
                    </a>
                </li>
            </ul>
        </div>
    </div>

</body>
</html>
"""

# 在 Streamlit 应用中嵌入 HTML 页面，增大高度
components.html(html_content, height=700)

# 定义全局 CSS 样式
css = """
<style>
    /* 设置背景颜色为暗红色 */
   .custom-container {
        background-color: #8B0000;
        padding: 20px;
        border-radius: 10px;
        height: 100%; /* 让容器高度占满列 */
        box-sizing: border-box; /* 包含内边距和边框在高度计算内 */
    }
    /* 设置标题居中 */
   .custom-title {
        text-align: center;
        font-size: 24px;
        color: white;
    }
    /* 设置内容字号小于标题 */
   .custom-content {
        font-size: 16px;
        color: white;
    }
    /* 使两列高度一致 */
   .st-col {
        display: flex;
        align-items: stretch;
    }
    /* 让图片容器高度占满列 */
   .stImage {
        height: 100%;
    }
    .stImage img {
        object-fit: cover; /* 图片填充容器 */
        height: 100%;
    }
    /* 修改图片标题颜色为黑色 */
   .stCaption {
        color: black;
    }
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# 创建列布局，两列宽度相等
col1, col2 = st.columns([1, 1])

with col1:
    st.image("https://p8.itc.cn/q_70/images03/20220508/7f325db93e2d40bd9bb1ec1d8d80b09c.jpeg", caption='汴绣',
             use_container_width=True)

with col2:
    # 展示内容并应用样式
    st.markdown(f"""
        <div class="custom-container">
            <h2 class="custom-title">开封汴绣</h2>
                                                          _</p>
            <p class="custom-content">汴绣，流传于河南省开封市的传统美术，国家级非物质文化遗产之一。汴绣也称“宋绣”，是流行于河南开封一带的传统刺绣艺术，因产生于北宋的都城汴京开封而得名。北宋时期汴京刺绣业兴盛，已达到较高的技艺水平，故《东京梦华录》中有“金碧相射，锦绣交辉”之誉。宋钦宗靖康二年（1127年），金兵攻破开封，宋室南迁，后复值兵祸水患，开封城市经济一蹶不振，刺绣业逐渐衰落。新中国建立后，几代汴绣艺人努力发掘整理宋代刺绣技艺，并借鉴苏绣、湘绣等其他绣种的长处，总结出36种汴绣针法，使汴绣工艺日臻完善成熟。汴绣长于绣制花鸟虫鱼、飞禽走兽等传统题材，同时也精于摹绣名画。其绣作形象逼真传神，针法严谨工致，技艺精巧细腻，色彩古朴典雅，是刺绣艺苑中不可多得的珍品。</p>


        </div>
        """, unsafe_allow_html=True)

# 第一组列布局，展示图片
col0, col1, col2, col3, col4, col5 = st.columns([0.5, 1, 1, 1, 1, 0.5])
with col0:
    pass
with col1:
    st.image("https://n.sinaimg.cn/translate/20160919/dcPx-fxvyqvy6696761.jpg",
             caption="配线，是“十指春风”的基础。艺人将手中的蚕丝彩线匹配分发，用心缠绕。", use_container_width=True)
with col2:
    st.image("http://n.sinaimg.cn/translate/20160919/p8fa-fxvyqwa3439571.jpg",
             caption='汴绣在继承传统工艺基础上，又创新了散针、乱针、滚针、水纹蒙针等几十种针法，多种针法的交替使用', use_container_width=True)
with col3:
    st.image("http://n.sinaimg.cn/translate/20160919/XRiE-fxvyqvy6696763.jpg",
             caption='一针一线的纯手工绣制，代表着汴绣艺人的“执著”，经过时间滋养的绣品充满温度', use_container_width=True)
with col4:
    st.image("http://n.sinaimg.cn/translate/20160919/GGS6-fxvyzus2035381.jpg",
             caption='汴绣代表作《韩熙载夜宴图》', use_container_width=True)
