import cv2
from deepface import DeepFace
import time

class EmotionDetector():
    def __init__(self):
        self.web_cam = cv2.VideoCapture(0)
        self.last_analyzed = 0
        self.analyze_interval = 1  # seconds
        self.focus_emotions = {}
        self.top_emotion = None

    def emotion_detection(self, run=True):
        start_time = time.time()

        while True:
            ret, frame = self.web_cam.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)

            # Every few seconds, analyze the current frame
            current_time = time.time()
            if current_time - self.last_analyzed > self.analyze_interval:
                try:
                    # Analyze the frame for emotion
                    result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                    emotions = result[0]['emotion']
                    # print(type(emotions))
                    # top_emotions = emotions[3]
                    print("Detected Emotions:", emotions)

                    self.focus_emotions = {"happy": emotions.get("happy"), "sad": emotions.get("sad"), "neutral": emotions.get("neutral")}
                    # print(focus_emotions, type(focus_emotions))

                    # Optional: Show top emotion on screen
                    self.top_emotion = max(self.focus_emotions, key=self.focus_emotions.get)
                    
                    self.last_analyzed = current_time
                except Exception as e:
                    print("Error:", e)

            # Draw top emotion text
            if self.top_emotion:
                cv2.putText(frame, f"Emotion: {self.top_emotion}", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Draw emotion bars
            if self.focus_emotions:
                bar_start_y = 60
                for idx, (emotion, score) in enumerate(self.focus_emotions.items()):
                    bar_length = int(score * 3)  # scale bar length
                    y = bar_start_y + idx * 30
                    cv2.rectangle(frame, (10, y), (10 + bar_length, y + 20), (255, 0, 0), -1)
                    cv2.putText(frame, f"{emotion}: {score:.2f}%", (15 + bar_length, y + 15),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

            # Show the frame with emotion
            cv2.imshow("Emotion Detection", frame)

            # Press 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

            if current_time - start_time > 5:
                break
                # self.get_emotions(run=True)
    
    def get_emotions(self, run):
        if run == True:
            for x in [4,3,2,1]:
                time.sleep(1)
                print("Give me " + str(x) + "seconds to interpretate your feelings.")
                print("this is the top emotion" + str(self.top_emotion))
            return self.focus_emotions, self.top_emotion
        else:
            return("error")

    def close_window(self):
        self.web_cam.release()
        cv2.destroyAllWindows()
