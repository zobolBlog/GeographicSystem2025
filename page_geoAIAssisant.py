import streamlit as st
from openai import OpenAI

from streamlit_chat import message

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

st.markdown("#### 我是开封市非物质文化遗产地理信息智能分析平台的AI助手，请问有什么可以帮助您的吗？")


# layout: 3:7 布局
col1, col2 = st.columns([3, 7])
with col1:
    contaner_first = st.container(border=True,height=800)
with col2:
    contaner_second = st.container(border=True,height=800)


with contaner_first:    
    st.image("img/Assisant_Logo.png",use_container_width="true") 
    st.subheader('',divider='rainbow')
    AVAILABLE_MODELS = [
        "Doubao-1.5-lite-32k",
        "Doubao-1.5-pro-32k",
        "DeepSeek-R1",
        "DeepSeek-R1-Distill-Qwen-32B",
        "Mistral-7B",
        "Moonshot-v1-8k",
    ]
    llm = st.selectbox('选择您的模型', AVAILABLE_MODELS, index=4)
    st.info("本助手基于火山方舟平台提供的大模型API，结合开封市非物质文化遗产地理信息数据组成的专属知识库，提供专属版的智能问答服务。")


with contaner_second:
    
    if 'generated' not in st.session_state:
        st.session_state['generated'] = []
    if 'past' not in st.session_state:
        st.session_state['past'] = []
    user_input=st.text_input("请输入您的问题:",key='input')
    if user_input:
        output=volcengine_client_request(user_input+",80字以内")
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)

    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            msg = st.chat_message("user", avatar="img/assisant1.jpg")
            msg.write(st.session_state['past'][i])
            msg2 = st.chat_message("ai", avatar="img/assisant2.jpg")
            msg2.write(st.session_state['generated'][i])
            #message(st.session_state['past'][i], 
            #        is_user=True, 
            #        key=str(i)+'_user',avatar_style=="img/assisant1.jpg")
            #message(st.session_state["generated"][i], key=str(i),logo=":img/assisant2.jpg")
            

