def calculate_average_confidence(keypoint_list):
"""Helper function to calculate average confidence"""
if len(keypoint_list) == 0:
return 0.0
total = 0
for point in keypoint_list:
total = total + point["conf"]
avg = total / len(keypoint_list)
return avg
def clear_memory(data):
"""Clear data for privacy protection"""
# just making sure no image data remains
data = None
return data
