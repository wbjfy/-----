import streamlit as st
import os
from openai import OpenAI

st.set_page_config(
    page_title="AI只能伴侣", # 标题
    page_icon="👽️", #图标
    layout="wide", #布局
    initial_sidebar_state="expanded", #侧边栏状态
    menu_items={}
)

# 大标题
st.title('AI只能伴侣')

client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

# 系统提示词
system_prompt = """
        你叫 %s，现在是用户的真实伴侣，请完全代入伴侣角色。：
        规则：
            1. 每次只回1条消息
            2. 禁止任何场景或状态描述性文字
            3. 匹配用户的语言
            4. 回复简短，像微信聊天一样
            5. 有需要的话可以用❤️🌸等emoji表情
            6. 用符合伴侣性格的方式对话
            7. 回复的内容, 要充分体现伴侣的性格特征
        伴侣性格：
            - %s
        你必须严格遵守上述规则来回复用户。
    """
# 初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages = []

#昵称
if 'nick_name' not in st.session_state:
    st.session_state.nick_name = ''

# 性格
if 'nature' not in st.session_state:
    st.session_state.nature = ''


# 展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message['role']).write(message['content'])
    # if message['role'] == 'user':
    #     st.chat_message('user').write(message['content'])
    # else:
    #     st.chat_message('assistant').write(message['content'])

# 左侧侧边栏
with st.sidebar:
    st.subheader("伴侣信息")
    nick_name = st.text_input('昵称',placeholder="请输入昵称")
    if nick_name:
        st.session_state.nick_name = nick_name
    nature = st.text_area('性格',placeholder="请输入性格")
    if nature:
        st.session_state.nature = nature

# 消息输入框
prompt = st.chat_input("请输入您要问的问题")
if prompt:
    st.chat_message("user").write(prompt)
    print('----------> 调用AI大模型，提示词: ',prompt)
    st.session_state.messages.append({'role':'user','content':prompt})
    # 调用AI大模型
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system","content": system_prompt % (st.session_state.nick_name,st.session_state.nature)},
            *st.session_state.messages
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    # 非流式输出
    # print("<---------------- 大模型返回的结果: " ,response.choices[0].message.content)
    # st.chat_message('assistant').write(response.choices[0].message.content)

    # 流式输出
    response_message = st.empty()  # 创建一个空的组件，用于展示大模型返回的结果
    full_response = ''
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message('assistant').write(full_response)
#     保存大模型返回的结果
#     st.session_state.messages.append({'role':'assistant','content':response.choices[0].message.content})
    st.session_state.messages.append({'role':'assistant','content':full_response})

