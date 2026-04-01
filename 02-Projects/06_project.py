import streamlit as st
import pandas as pd

# ॲपचे शीर्षक
st.title("💪 डेली फिटनेस ट्रॅकर")

# साइडबारमध्ये माहिती घेणे
st.sidebar.header("तुमची माहिती भरा")

with st.sidebar.form("fitness_form"):
    date = st.date_input("तारीख निवडा")
    exercise = st.selectbox("व्यायामाचा प्रकार", ["रनिंग", "जिम", "योगा", "सायकलिंग", "इतर"])
    duration = st.number_input("वेळ (मिनिटांत)", min_value=1, max_value=300, value=30)
    calories = st.number_input("बर्न केलेल्या कॅलरीज", min_value=1, max_value=2000, value=200)
    
    # फॉर्म सबमिट बटण
    submitted = st.form_submit_button("डेटा सेव्ह करा")

# डेटा प्रदर्शित करण्यासाठी एक रिकामी लिस्ट (Example साठी)
if submitted:
    st.success(f"नोंद यशस्वी! तुम्ही {date} रोजी {duration} मिनिटे {exercise} केले.")
    
    # एक साधा डेटाफ्रेम तयार करून टेबल दाखवणे
    data = {
        "तारीख": [date],
        "व्यायाम": [exercise],
        "वेळ (Min)": [duration],
        "कॅलरीज": [calories]
    }
    df = pd.DataFrame(data)
    
    st.subheader("आजची प्रगती")
    st.table(df) # टेबल फॉरमॅटमध्ये डेटा दाखवण्यासाठी

else:
    st.info("तुमचा व्यायाम ट्रॅक करण्यासाठी साइडबारमधील फॉर्म भरा.")

# एक प्रोग्रेस बार दाखवणे (Just for UI)
st.divider()
st.write("तुमचे आठवड्याचे ध्येय (Goal): 70%")
st.progress(70)
