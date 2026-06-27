import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np

#load the model
base_option = python.BaseOptions(model_asset_path='hand_landmarker.task') #load file path of data
opt=vision.HandLandmarkerOptions(
    base_options=base_option,
    num_hands=1,                    # track one hand
    min_hand_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
detector=vision.HandLandmarker.create_from_options(opt)

cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print('failed to open camera or not found')
else:
    print('camera found successfully and open')
print('hand detection started...stay tuned...Press q to quit')
# drawing setup
canvas    = None        # drawing layer — starts empty
pre_x, pre_y = None, None  # previous finger position
color     = (0, 0, 255)      # default red
thickness = 5

print("✅ Finger Drawing Started!")
print("Draw with INDEX finger")
print("Press C to clear | Press Q to quit")
c1=None
while True:
    ret,frame= cap.read()
    if not ret:
        print('failed to capture frame')
        break
    frame =cv2.flip(frame,1) # make mirror effect 
    if canvas is None:
        canvas=np.zeros_like(frame) # like same frame size make canvas on first run
    #convert frame data to mediapipe image format and accept RGB ,means frame data given to model
    mp_img=mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=frame
    )
    result=detector.detect(mp_img) # detect if there is any hand in frame
    
    if result.hand_landmarks:
        print(f'Hand detected!! Landmarks: {len(result.hand_landmarks[0])} ') # len or no of joints of hands .0 means one right  hands
        # draw a circle on index fingertip — landmark 8
        index_tip=result.hand_landmarks[0][8]
        index_base=result.hand_landmarks[0][5]
        print(f'finger top y value before erase : {index_tip.y} and index base value is {index_base.y}')
        # proper fist detection — ALL fingers curled
        middle_tip  = result.hand_landmarks[0][12]
        middle_base = result.hand_landmarks[0][9]
        ring_tip    = result.hand_landmarks[0][16]
        ring_base   = result.hand_landmarks[0][13]

        is_fist = (
        index_tip.y  > index_base.y  and
        middle_tip.y > middle_base.y and
        ring_tip.y   > ring_base.y
        )

        if is_fist:
            canvas = np.zeros_like(frame)
            pre_x, pre_y = None, None
            print("Canvas cleared by fist!")
        anghota=result.hand_landmarks[0][4]
        h,w,_=frame.shape
        print(f'h shape {h}., w shape {w}')
        x=int(anghota.x*w)
        y=int(anghota.y*h)
        cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)
        print(f'h shape {h}., w shape {w}')
        x1=int(index_tip.x*w)
        y2=int(index_tip.y*h)
        cv2.circle(frame, (x1, y2), 10, (0, 255, 0), -1)
        print(f'your index finger values x cordinates is : {x1},your index finger value y cordinates is : {y2}')
        print(f'your thumb finger values x cordinates is : {x},your index finger value y cordinates is : {y}')
        distance=np.hypot(x-x1,y-y2)
        print(f'the Euclidean distance is  : {distance}')
        if distance<35:
           # Click confirm karne ke liye screen par text dikha sakte hain
            cv2.putText(frame, "Drawing Mode ON", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            # draw line from previous position to current
            if pre_x is not None and pre_y is not None:
                cv2.line(canvas,(pre_x,pre_y),(x1,y2),color,thickness)
            pre_x,pre_y=x1,y2
        else:
            cv2.putText(frame, "Drawing Mode Off", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            pre_x,pre_y=None,None  
      
        
       
    else:
        pre_x,pre_y=None,None  
    if c1=='red':
        cv2.putText(frame, "R=Red",
            (80, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2) 
        cv2.putText(frame, "G=Green B=Blue G=White S=save Q=Quit",
            (150, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2) 
    elif c1=='green':
          cv2.putText(frame, "G=Green",
            (80, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2) 
          cv2.putText(frame, "R=Red B=Blue G=White S=save Q=Quit",
            (150, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2) 

    else:
        cv2.putText(frame, "R=Red G=Green B=Blue G=White S=save Q=Quit",
            (80, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)  
    combined=cv2.addWeighted(frame,1,canvas,1,0)
    cv2.imshow('Hand Detection ',combined)
   
    key = cv2.waitKey(30) & 0xFF
    if key == ord('q'):
        break
    if key == ord('r'):
        color = (0, 0, 255)    # red
        c1='red'
    if key == ord('g'):
        color=(0, 255, 0)
        c1='green'
        # cv2.putText(frame, "R=Red",
        #     (80, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2) 
    
    if key == ord('g'): color = (0, 255, 0)    # green
    if key == ord('b'): color = (255, 0, 0)    # blue
    if key == ord('w'): color = (255, 255, 255) # white
    if key == ord('s'): 
        cv2.imwrite('screenshot.png',combined)
cap.release()
cv2.destroyAllWindows()
