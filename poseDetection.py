# PROGRAM DEVELOPED BY BADBOI DAVE
# START DATE: 7TH JANUARY 2024
# START TIME: 10:43PM
# END DATE: 13th FEBRUARY 2024
# END TIME: 5:23AM

# STILL WORKING ON IMPROVEMENTS


import cv2
import mediapipe as mp
import numpy as np

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils
pose = mp_pose.Pose()

cap = cv2.VideoCapture(r"C:\\Users\\USER\\PycharmProjects\\Human body pose tracking\\videos\\video2.mp4")


if not cap.isOpened():
    print("Error opening Video File.")
try:
    while True:
        # Capture frame-by-frame
        ret, img = cap.read()
        img = cv2.resize(img, (600, 400))
        results = pose.process(img)
        #mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS, mp_draw.DrawingSpec((2555, 0, 0), 2, 2), mp_draw.DrawingSpec((255, 0, 255), 2, 2))

        h, w, c = img.shape


        opImg = np.zeros([h, w, c])
        opImg.fill(255)

        mp_draw.draw_landmarks(opImg, results.pose_landmarks, mp_pose.POSE_CONNECTIONS, mp_draw.DrawingSpec((255, 0, 0), 2, 2), mp_draw.DrawingSpec((255, 0, 255), 2, 2))
        cv2.imshow("Extracted Pose", opImg)

        print(results.pose_landmarks)
        cv2.imshow("Pose Estimation", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # if frame is read correctly, ret is True
        if not ret:
            print("Can't retrieve frame - stream may have ended. Exiting..")
            break
except:
    print("Video has ended.")


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

#while True:
#    ret, img = cap.read()
#    img = cv2.resize(img, (600, 400))
#    cv2.imshow("Pose Estimation", img)
#    cv2.waitKey(1)