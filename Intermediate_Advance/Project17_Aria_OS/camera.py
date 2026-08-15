import cv2
from PyQt5.QtCore import QThread , pyqtSignal
from PyQt5.QtGui import QImage

class ai_camer(QThread):
    finished=pyqtSignal(QImage)
    def __init__(self):
      super().__init__()
      self.running=True
    

    def run(self):
        cap=cv2.VideoCapture(0)
        cap.set(3, 640)
        cap.set(4, 480)    
        if not cap.isOpened:
            print("camera not found")
            return
        else:
            print("camera found successfully")

        while self.running:
                ret,frame = cap.read()
                if not ret:
                 break
                frame=cv2.flip(frame,1)
               # convert OpenCV BGR to RGB
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_frame.shape
                bytes_per_line = ch * w
                # 4. RAM memory se data lekar PyQt5 ki QImage banayein
                qt_img = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            
                # 5. Picture ko 320x240 size mein chota karein taaki panel mein fit aaye
                qt_img = qt_img.scaled(320, 240)

                self.finished.emit(qt_img)
        cap.release()
    # 7. Thread ko safely band karne ka switch
    def stop(self):
        self.running = False
        self.quit()
        self.wait()




def cammera():
    
    cap=cv2.VideoCapture(0)

   
    

        
        

  
