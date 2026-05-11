def combine_keypoints(frontData, sideData):
"""Combine keypoints from front and side camera"""
front_conf = frontData["conf"]
side_conf = sideData["conf"]
if front_conf == 0 and side_conf == 0:
return {"conf": 0}
# giving more weight to front camera as it is usually clearer
fused = (front_conf * 0.6) + (side_conf * 0.4)
# if one camera has very low confidence, use the other one
if front_conf < 0.2:
fused = side_conf
elif side_conf < 0.2:
fused = front_conf
return {"conf": fused}
