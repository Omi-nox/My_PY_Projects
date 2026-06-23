import cv2
from ultralytics import YOLO

model=YOLO('yolov8n.pt') # nano model creation - small , fast, accurate

cap=cv2.VideoCapture(0) #0= default webcam

# objects we consider as potential threats
threat_objects = ["knife", "scissors"]
thrt_counter=0
print(" Starting detection... Press Q to quit")

if not cap.isOpened(): # if cap is opende false then it will make it true to run
    print('Camera not found')
else:
    print('Camera opened successfully and found')

while True:
    ret, frame = cap.read() # reads one frame

    if not ret: # false make it true
        print('failed to grab a frame of the USER OR OBJECT')
        break      
    # run YOLO on current frame   
    result=model(frame,verbose=False) # give each frame within model , it will detect by deep learning  

    #draw boxes on each frame that you fetch, it will always at 0 on every iteration
    annotated_frame=result[0].plot() 

    # show fps and object count
    detected=result[0].boxes  # at 0 index result the no, of box of list in each frame
    count=len(detected) if detected is not None else 0
    threat_detected=False

     # loop through every detected object
    for box in result[0].boxes:
        class_id = int(box.cls[0])
        label = model.names[class_id]        # get object name , convert class number to readable label
        confidence = float(box.conf[0])  # get confidence score
        print(label ,end=',')     

        if label in threat_objects:
            threat_detected = True
            thrt_counter+=1
            print(f" THREAT DETECTED: {label} ({confidence:.2f})")

    # show status on screen
    status =  "!!! THREAT DETECTED" if threat_detected else "!!! ALL CLEAR"
    color  = (0, 0, 255) if threat_detected else (0, 255, 0)

    cv2.putText(annotated_frame, f"No of Objects: {count}", (10, 30),  # one for status to show in frame
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(annotated_frame, f"No of threats detected: {thrt_counter}", (10, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)  # one for counter
    cv2.putText(annotated_frame, status, (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2) # one for object
    # draw boxes on frame
    cv2.imshow('YOLOv8 Detection',annotated_frame)    # shows the frame in a window ny craeting window

    # press Q to quit , cv wait pause and freeze for 1 mili second so it give enough time to draw pixel render it  before next move , check user enter q in 1 mili second if it is then brea
    if cv2.waitKey(30) & 0xFF==ord('s'): 
        print('thanks for using me , bye')
        cv2.imwrite('screenshot.png',annotated_frame)
        break
cap.release() # release Camera
cv2.destroyAllWindows() #close all windows

#verbose mean talking to much than needed by true it will print  in backgorund , by false it will do his work silently