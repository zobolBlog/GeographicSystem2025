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
components.html(html_content, height=1000)