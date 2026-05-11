import random
def get_camera_data(camera_type):
"""Simulate camera input for testing"""
# this is dummy data for testing
if camera_type == "front":
data = [
(100, 200, 0.92),
(150, 250, 0.85),
(200, 300, 0.78),
(250, 350, 0.65),
(300, 400, 0.55)
]
else: # side camera
data = [
(100, 200, 0.88),
(150, 250, 0.72),
(200, 300, 0.60),
(250, 350, 0.45)
]
print(f"Received {len(data)} points from {camera_type} camera")
return data
