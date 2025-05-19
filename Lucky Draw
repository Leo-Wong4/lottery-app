import streamlit as st
import random

st.title("Lottery App")

participants = st.text_area("Enter the names of participants (one per line):")
participants_list = list(set(participants.split("\n")))  # Remove duplicates

if 'winners' not in st.session_state:
    st.session_state['winners'] = []

if 'remaining_participants' not in st.session_state:
    st.session_state['remaining_participants'] = participants_list
else:
    st.session_state['remaining_participants'] = list(set(st.session_state['remaining_participants']).intersection(set(participants_list)))

if st.button("Draw a Winner") and st.session_state['remaining_participants']:
    winner = random.choice(st.session_state['remaining_participants'])
    st.session_state['winners'].append(winner)
    st.session_state['remaining_participants'].remove(winner)
    st.success(f"The winner is: {winner}")

if st.session_state['winners']:
    st.write("List of winners:")
    for winner in st.session_state['winners']:
        st.write(winner)

if not st.session_state['remaining_participants']:
    st.warning("All participants have won. The draw is complete.")
