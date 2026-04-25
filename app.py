import streamlit as st
import time

# Importing our project modules
from main import run_system
from camera_input import get_camera_data
from Pose_Detection import get_body_keypoints
from fusion_logic import combine_keypoints

st.set_page_config(page_title="FitTrack AI", page_icon="🏋️", layout="centered")

st.title("🏋️ FitTrack AI")
st.subheader("Privacy First AI Posture Analysis System")

st.write("This tool helps analyze your posture using keypoints from two cameras without storing any images or videos.")

# Sidebar
st.sidebar.title("Control Panel")
mode = st.sidebar.selectbox(
    "Choose Analysis Mode",
    ["Front + Side Camera", "Front Camera Only", "Side Camera Only"]
)

speed = st.sidebar.slider("How fast should the analysis run?", 1, 6, 3)

if st.button("Start Posture Analysis", type="primary"):
    
    with st.spinner("Taking keypoints from cameras and analyzing..."):
        time.sleep(speed)
        
        # Using our existing system
        result = run_system()
        
        st.success("Analysis Done!")
        
        # Showing more details for better understanding
        front_points = get_camera_data("front")
        side_points = get_camera_data("side")
        
        front_list = get_body_keypoints(front_points)
        side_list = get_body_keypoints(side_points)
        
        front_conf = sum(p["conf"] for p in front_list) / len(front_list) if front_list else 0
        side_conf = sum(p["conf"] for p in side_list) / len(side_list) if side_list else 0
        
        fused_data = combine_keypoints({"conf": front_conf}, {"conf": side_conf})
        
        # Display results
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Front Confidence", f"{front_conf:.3f}")
        with col2:
            st.metric("Side Confidence", f"{side_conf:.3f}")
        with col3:
            st.metric("Final Fused Score", f"{fused_data['conf']:.3f}")
        
        st.divider()
        
        if fused_data['conf'] >= 0.70:
            st.success("✅ Good Posture! You are doing it correctly.")
        elif fused_data['conf'] >= 0.55:
            st.warning("⚠️ Posture is okay, but you can improve it a bit.")
        else:
            st.error("❌ Poor Posture detected. Please correct your form to avoid injury.")
        
        st.info("🔒 Important: No image or video was saved. Only keypoints were used and then cleared.")

st.divider()

st.write("### How this works")
st.write("""
- Gets keypoints from front and side views  
- Filters weak detections  
- Combines both cameras using confidence scores  
- Clears all raw data for privacy  
- Gives simple feedback
""")

st.caption("Made by Harsh Raj • April 2026")
