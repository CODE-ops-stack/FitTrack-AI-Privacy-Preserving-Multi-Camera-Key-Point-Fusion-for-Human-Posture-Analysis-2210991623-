def get_body_keypoints(points):
"""This function extracts and filters keypoints"""
body_data = []
for p in points:
conf = p[2]
if conf < 0.2:
continue # skipping low confidence points to reduce noise
temp = {}
temp["x"] = p[0]
temp["y"] = p[1]
temp["conf"] = conf
body_data.append(temp)
return body_data
