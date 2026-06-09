import streamlit as st
import openai

def generate_article(api_key, topic, stance, tone, length):
    client = openai.OpenAI(api_key=api_key)
    prompt = f"""
    请撰写一篇关于以下主题的深度观点短文：
    主题: {topic}
    立场/观点: {stance}
    语气/风格: {tone}
    目标字数: 约{length}字
    要求：观点明确，逻辑严密，具有深度。
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"错误: {str(e)}"

st.title("深度观点短文创作器")
api_key = st.sidebar.text_input("OpenAI API Key", type="password")
topic = st.text_input("讨论主题")
stance = st.text_area("核心立场")
tone = st.selectbox("风格", ["客观理性", "犀利批判"])
length = st.selectbox("字数", ["500", "1000"])

if st.button("生成"):
    if api_key and topic and stance:
        st.write(generate_article(api_key, topic, stance, tone, length))
    else:
        st.error("请填写完整信息")
