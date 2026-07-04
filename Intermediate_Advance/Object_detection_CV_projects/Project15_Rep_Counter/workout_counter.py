import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np
import time

#load model
base_options=python.BaseOptions(model_asset_path='pose_landmarker_lite.task')
options=vision.PoseLandmarkerOptions(
    base_options=base_options,
    min_pose_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
detector=vision.PoseLandmarker.create_from_options(options)
cap = cv2.VideoCapture(0)
print("✅ Pose Detection Started! Press 'q' to exit.")
cam_w, cam_h=840,680
cap.set(3,cam_w) # set the selected size
cap.set(4,cam_h)
counter=0
stage='down'
last_counter_time=0
while True:
    ret,frame=cap.read()
    if not ret:
        break
    frame=cv2.flip(frame,1)
    h,w,_=frame.shape
    mp_img=mp.Image(image_format=mp.ImageFormat.SRGB,
                    data=frame)
    result=detector.detect(mp_img)
    if result.pose_landmarks:
        landmarks=result.pose_landmarks[0]
        world_landmarks=result.pose_world_landmarks[0]
        # key landmarks we need for bicep curl
        # 11=left shoulder, 13=left elbow, 15=left wrist
        shoulder = landmarks[11]
        elbow    = landmarks[13]
        wrist    = landmarks[15]

          # 2. GLITCH-FREE ANGLE: 3D World Coordinates (Calculations ke liye)
        sh_3d = world_landmarks[11]
        el_3d = world_landmarks[13]
        wr_3d = world_landmarks[15]
        
        # 3D points (X, Y, Z) meters mein
        a = np.array([sh_3d.x, sh_3d.y, sh_3d.z])
        b = np.array([el_3d.x, el_3d.y, el_3d.z])
        c = np.array([wr_3d.x, wr_3d.y, wr_3d.z])


        # convert to pixel coordinates
        sx, sy = int(shoulder.x * w), int(shoulder.y * h)
        ex, ey = int(elbow.x * w),    int(elbow.y * h)
        wx, wy = int(wrist.x * w),    int(wrist.y * h)
        # calculate the angle at the elbow using the cosine law
        a = np.array([sx, sy])  # shoulder
        b = np.array([ex, ey])  # elbow
        c = np.array([wx, wy])  # wrist
        # calculate the distances from base elbow 
        ba=a-b
        bc=c-b
        # dot of two vectors
        dot_product=np.dot(ba,bc) # main component of angle
        # magnitude of vectors
        norm_ba=np.linalg.norm(ba)
        norm_bc=np.linalg.norm(bc)
        #Trignometry formula 
        cosine=dot_product/(norm_ba*norm_bc)
        cosine_angle=np.clip(cosine,-1.0,1.0) # clip to avoid numerical errors
        final_angle=np.degrees(np.arccos(cosine_angle))
        print(f'Elbow Angle: {final_angle:.2f} degrees')

        # rep counter logic
        crnt_counter_time=time.time()
        if final_angle > 150:  
            stage='down'
        if final_angle< 70 and stage=='down' and (crnt_counter_time-last_counter_time)>0.5:  # 0.5 sec cooldown, not to count multiple times in per sec 30 time frame
            stage='up'
            counter+=1
            last_counter_time=time.time()
            print(
                f"✅ Rep Count: {counter} | Stage: {stage} | Elbow Angle: {final_angle:.2f} degrees")
            
        cv2.circle(frame, (sx, sy), 10, (0, 255, 0), -1)   # shoulder
        cv2.circle(frame, (ex, ey), 10, (0, 255, 0), -1)   # elbow
        cv2.circle(frame, (wx, wy), 10, (0, 255, 0), -1)   # wrist

        # draw lines connecting joints
        cv2.line(frame, (sx, sy), (ex, ey), (255, 255, 0), 3)
        cv2.line(frame, (ex, ey), (wx, wy), (255, 255, 0), 3)

        # UI/Text Display
        # Angle overlay kohni ke paas
        cv2.putText(frame, f'{int(final_angle)} deg', (ex + 10, ey), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        # Rep counter dashboard (Top Left Corner)
        cv2.rectangle(frame, (0, 0), (250, 100), (0, 0, 0), -1)
        cv2.putText(frame, f'REPS: {counter}', (10, 40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 3)
        cv2.putText(frame, f'STAGE: {stage}', (10, 80), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0) if stage=='up' else (0, 0, 255), 2)

        print(f"Shoulder: ({sx},{sy}) | Elbow: ({ex},{ey}) | Wrist: ({wx},{wy})")

    cv2.imshow("ARIA Workout Counter", frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()