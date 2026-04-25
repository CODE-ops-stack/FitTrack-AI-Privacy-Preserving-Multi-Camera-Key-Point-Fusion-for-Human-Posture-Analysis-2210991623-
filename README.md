FitTrack-AI Privacy Preserving Multi Camera Key Point Fusion for Human Posture Analysis

This project is a basic implementation focused on the core idea of privacy-preserving posture analysis. 
It processes only numerical keypoints from front and side views, performs multi-camera fusion, and gives simple feedback.

Note:This is a modular prototype. Real camera integration and advanced posture angle calculation are planned as future work.

 -Current Implementation

- Keypoint filtering
- Confidence-based multi-camera fusion
- Basic posture feedback using fused confidence
- Strong focus on privacy (raw data is cleared immediately)
- Streamlit interface for demonstration

-Repository Structure
...(same as before)
-Limitations

- Currently uses simulated (dummy) keypoints instead of real camera input
- Posture evaluation is based on confidence score only (not actual joint angles)
- Not a complete real-time system yet

-Repository Structure
FitTrack-AI/
├── main.py                 # Main file to run the system
├── Pose_Detection.py       # Filters keypoints
├── fusion_logic.py         # Multi-camera keypoint fusion
├── feedback_logic.py       # Posture feedback logic
├── camera_input.py         # Dummy camera input (simulation)
├── utils.py                # Helper functions
├── constants.py            # Constants used in project
├── app.py                  # Streamlit web interface for demo
└── README.md
-Future Scope

- Integrate MediaPipe for real keypoint extraction
- Calculate actual angles (knee, hip, back, etc.)
- Give specific correction suggestions
- Support different exercises (squat, deadlift, etc.)

-Author
Harsh Raj  
BE-CSE, 8th Semester (Zeta Cluster)  
Chitkara University  
April 2026
