import streamlit as st
import streamlit.components.v1 as components

# 定义一个简单的 HTML 页面，去除外部资源引用
html_content = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <title>开封市继中朱仙镇木板年画社</title>
    <meta name="keywords" content=",,,开封市继中朱仙镇木版年画社" />
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
            <div class="welcolm fl"><p>欢迎进入开封朱仙镇木版年画</p></div>
        </div>
    </div>
    <div id="header">
        <div class="top clearfix">
            <div class="logo">
                <img alt="" src="http://www.zxznianhua.com/data/images/other/20170315164321_917.png" />
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
                        <img src="http://www.zxznianhua.com/data/images/banner/20170315165253_662.jpg" alt="开封木版年画" width="1920" height="670" />
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
    st.image("http://www.zxznianhua.com/data/upload/image/20170315/1489569129572494.png", caption='木版年画', use_container_width=True)

with col2:
    # 展示内容并应用样式
    st.markdown(f"""
        <div class="custom-container">
            <h2 class="custom-title">朱仙镇万同老店年画作坊</h2>
            <p>_</p>
            <p>                                                                _</p>
            <p class="custom-content">朱仙镇木版年画源于汉唐壁画艺术，由“桃符”演变而来，历史悠久，源远流长。明清鼎盛时期，朱仙镇木版年画作坊达三百多家，年产销几千万张，畅销全国各地，大有独占市场之势。万同老店年画作坊创建于明末清初，是 朱仙镇著名的年画老店之一，兴盛时期木版千余块，印工上百人。万同老店现位于朱仙镇运粮河西岸中段，面阔六间，占地450平方米。万同老店年画主要产品有：门神、财神、灶神、神话故事、戏曲年画等，它构图饱满、线条粗犷、色彩艳丽、久不褪色、形象夸张，采用传统手工水色套印，被誉为“中华绝活”，是古版年画中的精品。</p>
            <p>_</p>
            <p>_</p>
            
        </div>
        """, unsafe_allow_html=True)


# 第一组列布局，展示图片
col0, col1, col2, col3, col4, col5 = st.columns([0.5, 1, 1, 1, 1, 0.5])
with col0:
    pass
with col1:
    st.image("http://www.zxznianhua.com/data/images/banner/20170315172039_305.png", caption="万同老店现有国家级工艺美术大师三人，河南省民间艺术家五人，高级印工五人", use_container_width=True)
with col2:
    st.image("http://www.zxznianhua.com/data/images/banner/20170315172123_724.png", caption='万同老店在民间文化遗产抢救过程中，尤其在朱仙镇木版年画频危之际', use_container_width=True)
with col3:
    st.image("http://www.zxznianhua.com/data/images/banner/20170315172150_263.png", caption='朱仙镇木版年画有一千多年的迷人历史,历来被国内外民俗专家尊崇', use_container_width=True)
with col4:
    st.image("http://www.zxznianhua.com/data/images/banner/20170315172207_983.png", caption='采用传统手工水色套印，被誉为“中华绝活”，是古版年画中的精品', use_container_width=True)
