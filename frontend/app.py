import streamlit as st
import requests

st.set_page_config(page_title="Adaptive Learning System", layout="wide")

st.title("Adaptive Learning Recommendation System")

# ---------------- INPUT SECTION ---------------- #

st.subheader("📋 Enter Student Details")

col1, col2 = st.columns(2)

with col1:
    study_hours = st.slider("Study Hours (per day)", 0, 10)
    attendance = st.slider("Attendance (%)", 0, 100)
    resources = st.slider("Study Resources Usage", 0, 10)

    extra_option = st.selectbox(
        "Extracurricular Activity",
        ["None", "Low", "Medium", "High"]
    )
    extra_map = {"None": 0, "Low": 1, "Medium": 3, "High": 5}
    extracurricular = extra_map[extra_option]

    motivation = st.slider("Motivation Level", 0, 10)

    internet_option = st.selectbox("Internet Access", ["No", "Yes"])
    internet = 1 if internet_option == "Yes" else 0


with col2:
    age = st.slider("Age", 15, 30)

    style_option = st.selectbox(
        "Learning Style",
        ["Visual", "Auditory", "Kinesthetic"]
    )
    style_map = {
        "Visual": 0,
        "Auditory": 1,
        "Kinesthetic": 2
    }
    learning_style = style_map[style_option]

    online_courses = st.slider("Online Courses Taken", 0, 10)
    discussions = st.slider("Participation in Discussions", 0, 10)
    assignment = st.slider("Assignment Completion", 0, 10)
    edutech = st.slider("EduTech Usage", 0, 10)
    stress = st.slider("Stress Level", 0, 10)

# ---------------- PREDICT BUTTON ---------------- #

st.markdown("###")
predict_btn = st.button("🚀 Predict")

# ---------------- PREDICTION ---------------- #

if predict_btn:

    data = {
        "StudyHours": study_hours,
        "Attendance": attendance,
        "Resources": resources,
        "Extracurricular": extracurricular,
        "Motivation": motivation,
        "Internet": internet,
        "Age": age,
        "LearningStyle": learning_style,
        "OnlineCourses": online_courses,
        "Discussions": discussions,
        "AssignmentCompletion": assignment,
        "EduTech": edutech,
        "StressLevel": stress
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=data)

        if response.status_code != 200:
            st.error(f"API Error: {response.status_code}")
            st.stop()

        res_json = response.json()

        # 🔥 DEBUG (DON'T REMOVE UNTIL STABLE)
        st.write("RAW RESPONSE:", res_json)

        if "prediction" not in res_json:
            st.error(f"Unexpected response format: {res_json}")
            st.stop()

        raw_pred = res_json["prediction"]

        # 🔥 HANDLE ALL CASES (no assumptions)
        if isinstance(raw_pred, list):
            prediction = int(raw_pred[0])
        elif isinstance(raw_pred, (int, float)):
            prediction = int(raw_pred)
        elif isinstance(raw_pred, str):
            # map string outputs
            string_map = {
                "Low": 0,
                "Medium": 1,
                "High": 2
            }
            prediction = string_map.get(raw_pred, -1)
        else:
            prediction = -1

        label_map = {
            0: "Low Performance",
            1: "Medium Performance",
            2: "High Performance"
        }

        result = label_map.get(prediction, "Unknown")

        st.markdown("---")

        # -------- RESULT DISPLAY -------- #
        if prediction == 0:
            st.error(f"📉 Prediction: {result}")
        elif prediction == 1:
            st.warning(f"📊 Prediction: {result}")
        elif prediction == 2:
            st.success(f"📈 Prediction: {result}")
        else:
            st.error(f"Prediction could not be interpreted → {raw_pred}")

        # -------- RECOMMENDATIONS -------- #
        st.subheader("🎯 Personalized Recommendations")

        if study_hours < 3:
            st.info("Increase daily study hours")

        if attendance < 75:
            st.info("Improve attendance")

        if stress > 7:
            st.info("Reduce stress levels")

        if motivation < 4:
            st.info("Work on motivation")

        if learning_style == 0:
            st.write("🧠 Visual learner → use diagrams & charts")
        elif learning_style == 1:
            st.write("🧠 Auditory learner → use lectures & discussions")
        else:
            st.write("🧠 Kinesthetic learner → practice hands-on")

    except requests.exceptions.ConnectionError:
        st.error("🚫 Backend server not running")
    except Exception as e:
        st.error(f"Unexpected Error: {e}")

# ---------------- METRICS ---------------- #

st.markdown("---")
st.subheader("📊 Model Monitoring")

try:
    metrics = requests.get("http://127.0.0.1:8000/metrics")

    if metrics.status_code == 200:
        data = metrics.json()

        st.write("RAW METRICS:", data)

        if "total_samples" in data:
            st.write(f"Feedback Samples: {data['total_samples']}")
        else:
            st.write(data.get("message", "No data available"))

    else:
        st.warning("Metrics not available")

except requests.exceptions.ConnectionError:
    st.warning("Backend not running")
except Exception as e:
    st.warning(f"Error fetching metrics: {e}")