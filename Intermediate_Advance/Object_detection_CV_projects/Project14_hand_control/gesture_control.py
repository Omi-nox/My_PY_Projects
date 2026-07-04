import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import pyautogui
import numpy as np
import time

#safety - stop pyautogui if mouse hit corner / for safety if code has bug or get hang
pyautogui.FAILSAFE=False
pyautogui.PAUSE=0 # no delay between commands/no waits after click or move/ to make sure move simultaneously with hand

# screen size
screen_w, screen_h=pyautogui.size()
print(f'screen size : {screen_w} x {screen_h}')

#model setup
opt = python.BaseOptions(model_asset_path='hand_landmarker.task')
options=vision.HandLandmarkerOptions(
    base_options=opt,
    num_hands=1,
    min_hand_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
detector=vision.HandLandmarker.create_from_options(options)
cap=cv2.VideoCapture(0)


cam_w, cam_h=640,480
cap.set(3,cam_w) # set the selected size
cap.set(4,cam_h)

#smoothing variable cursor
smooth_x,smooth_y=0,0 # past loc mem / update faster in frame due to fast loop
smoothing=4 # higher = smother but slower


print("✅ Gesture Control Started! Move index finger to control mouse")
print("Move mouse to TOP LEFT corner to emergency stop!")

last_click=0
last_tab=0
while True:
    key = cv2.waitKey(30) & 0xFF
    if key == ord('q'):
        break
    ret,frame=cap.read()
    if not ret:
        break
    frame=cv2.flip(frame,1)
    h,w,_=frame.shape

    mp_img=mp.Image(image_format=mp.ImageFormat.SRGB,
                    data=frame)
    result=detector.detect(mp_img)
    if result.hand_landmarks:
        landmarks=result.hand_landmarks[0]
        index_tip=landmarks[8]
        thumb_tip   = landmarks[4]
        middle_tip  = landmarks[12]
        ring_tip    = landmarks[16]
        pinky_tip   = landmarks[20]
        index_base  = landmarks[5]
        middle_base = landmarks[9]
        ring_base   = landmarks[13]
        pinky_tip=landmarks[20]
        pinky_base=landmarks[17]
        #Section B control structure
        # finger states - is each finger up or down
        index_up=index_tip.y < index_base.y
        middle_up=middle_tip.y < middle_base.y
        ring_up=ring_tip.y<ring_base.y
        pinky_up=pinky_tip.y<pinky_base.y
        #pinching using eculedean distance formula between thumb and index
        pinch_dis=np.hypot(
            (thumb_tip.x-index_tip.x)*w,
            (thumb_tip.y-index_tip.y)*h
        )
        #SCROLL down - INDEX is up and middle is down
        if index_up and  not middle_up and not ring_up and not pinky_up:
            pyautogui.scroll(-43)
            cv2.putText(frame, "SCROLL DOWN", (10, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            pinch_dis=31
      # SCROLL up — index , middle are up and ring  and pinky is down
        if   index_up and middle_up and  not ring_up and not pinky_up:
            pyautogui.scroll(43)
            cv2.putText(frame, "SCROLL UP", (10, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            pinch_dis=31

        #click - on pinch gesture 
        print(f'distance before clicking  : {pinch_dis}')
        crnt_time=time.time()
       
        if pinch_dis<20 and (crnt_time-last_click)>0.9:  # 0.5 sec cooldown, not to clicks multiple times in per sec 30 time frame 
            pyautogui.click()
            last_click=crnt_time
            print(f'distance after clicking : {pinch_dis}')
            cv2.putText(frame,'Click!!1',(10,90),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,255),2)
        # ALT+TAB — three fingers up
        if index_up and not middle_up and not ring_up and pinky_up:
            now=time.time()
            if now-last_tab>1.5:
                pyautogui.hotkey('win','tab')
                last_tab=now
                cv2.putText(frame, "TASK VIEW (SELECT TAB)", (10, 90),
                     cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)
   
        #Section A mouse cursor movement
        #define a smaller zone in camera for frame separate from camera
        margin=100
        
        cv2.rectangle(frame, (margin, margin),
              (w - margin, h - margin),
              (255, 0, 255), 2)
        cv2.putText(frame, "Active Zone", (margin, margin - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
        # clamp finger position within the active zone
        fx = np.interp(index_tip.x * w, [margin, w - margin], [0, screen_w])
        # from 50 to 480-30= 450 not 380 so our hand can touch the taskbar
        fy = np.interp(index_tip.y * h, [50, h - 80], [0, screen_h])

        # mouse_x = int(fx)
        # mouse_y = int(fy)
        #convert finger position normalized value from camera frame  to screen coordinate
        mouse_x=int(fx)
        mouse_y=int(fy)
        #smoothing - gradual control formula
        smooth_x +=(mouse_x-smooth_x)/smoothing
        smooth_y +=(mouse_y-smooth_y)/smoothing

        pyautogui.moveTo(int(smooth_x),int(smooth_y)) # by formula

        #show dot on finger on camera frame
        cx=int(index_tip.x*w)
        cy=int(index_tip.y*h)
        cv2.circle(frame,(cx,cy),10,(0,255,0),-1)
        cv2.putText(frame,f'mouse: {int(smooth_x),{int(smooth_y)}}',(10,60),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)
    cv2.putText(frame, "Index Finger = Move Mouse | Q = Quit",
                   (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)
    cv2.imshow("ARIA Gesture Control", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()    
