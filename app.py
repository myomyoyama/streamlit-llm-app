from dotenv import load_dotenv

load_dotenv()

##-----------------------------------------------------------

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

##-----------------------------------------------------------

import streamlit as st

def ai_bot(user_input, selected_item):
    if selected_item == "数学の専門家":
        system_message = "あなたは数学の専門家です。入力されてくる質問に答えてください。"

        messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=user_input)
        ]

        if st.button("送信"):
            if input_message:
                result = llm(messages)
                return result.content
            else:
                st.error("質問するテキストを入力してから「送信」ボタンを押してください。")
    else:
        system_message = "あなたは医療の専門家です。入力されてくる質問に答えてください。ただし、「一般的な情報提供のみ」「診断は行わない」でください。"

        messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=user_input)
        ]

        if st.button("送信"):
            if input_message:
                result = llm(messages)
                return result.content
            else:
                st.error("質問するテキストを入力してから「送信」ボタンを押してください。")

st.title("Q＆A AIチャットボット")

st.write("##### 動作モード1: 数学の専門家")
st.write("入力フォームにテキストを入力し、「送信」ボタンを押すことで数学の専門家に質問ができます。")
st.write("##### 動作モード2: 医療の専門家")
st.write("入力フォームにテキストを入力し、「送信」ボタンを押すことで医療の専門家に質問ができます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["数学の専門家", "医療の専門家"]
)

st.divider()

label_genre = "私は" + selected_item + "です。数学について何でも聞いてください。"
input_message = st.text_input(label=label_genre)

if selected_item == "数学の専門家":
    result = ai_bot(input_message, "数学の専門家")
else:
    result = ai_bot(input_message, "医療の専門家")

if(result):
    st.write(result)
else:
    st.write("質問を入力して「送信」ボタンを押してください。")

