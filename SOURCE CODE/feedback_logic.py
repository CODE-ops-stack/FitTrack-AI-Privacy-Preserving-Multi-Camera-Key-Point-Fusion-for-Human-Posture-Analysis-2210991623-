def check_posture(confidence):
"""Give simple feedback based on confidence"""
# simple threshold based decision
if confidence >= 0.65:
return "Posture looks fine"
elif confidence >= 0.45:
return "Posture is almost correct"
else:
return "Posture theek karo" # there is risk of injury
