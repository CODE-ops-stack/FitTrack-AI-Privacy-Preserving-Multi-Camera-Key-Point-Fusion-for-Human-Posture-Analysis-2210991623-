from fusion_logic import combine_keypoints
from Pose_Detection import get_body_keypoints
from feedback_logic import check_posture
from camera_input import get_camera_data
def run_system():
# getting data from both cameras
print("Starting FitTrack AI system...")
front_points = get_camera_data("front")
side_points = get_camera_data("side")
# extract keypoints
front_list = get_body_keypoints(front_points)
side_list = get_body_keypoints(side_points)
# calculating average confidence
# I used average because it gives better result than simple count
front_avg = 0
if len(front_list) > 0:
total = 0
for p in front_list:
total = total + p["conf"]
front_avg = total / len(front_list)
side_avg = 0
if len(side_list) > 0:
total = 0
for p in side_list:
total = total + p["conf"]
side_avg = total / len(side_list)
front_info = {"conf": front_avg}
side_info = {"conf": side_avg}
# fuse both cameras
final_data = combine_keypoints(front_info, side_info)
# clear raw data for privacy
front_points = None
side_points = None
# get final feedback
result = check_posture(final_data["conf"])
print("System completed.")
return result
if __name__ == "__main__":
# this is for testing only
output = run_system()
print("Final Result:", output)
