import streamlit as st
import streamlit.components.v1 as components

# 定义一个简单的 HTML 页面，去除外部资源引用
html_content = """

"""

# 在 Streamlit 应用中嵌入 HTML 页面，增大高度
components.html(html_content, height=1000)