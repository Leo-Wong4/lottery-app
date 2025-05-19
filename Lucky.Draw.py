import streamlit as st
import random

st.title("Lottery App")

# 輸入參加者
participants = st.text_area("Enter the names of participants (one per line):")
participants_list = list(set(participants.split("\n")))  # 去除重複

# 初始化 session_state
if 'winners' not in st.session_state:
    st.session_state['winners'] = []

if 'remaining_participants' not in st.session_state:
    st.session_state['remaining_participants'] = participants_list
else:
    # 若使用者有更新名單，重新同步剩餘參加者
    st.session_state['remaining_participants'] = list(
        set(st.session_state['remaining_participants']).intersection(set(participants_list))
    )

# 抽獎按鈕
if st.button("Draw a Winner") and st.session_state['remaining_participants']:
    winner = random.choice(st.session_state['remaining_participants'])
    st.session_state['winners'].append(winner)
    st.session_state['remaining_participants'].remove(winner)
    st.success(f"The winner is: {winner}")

# 顯示中獎名單
if st.session_state['winners']:
    st.write("List of winners:")
    for winner in st.session_state['winners']:
        st.write(winner)

# 所有人都中獎後提示
if not st.session_state['remaining_participants']:
    st.warning("All participants have won. The draw is complete.")
