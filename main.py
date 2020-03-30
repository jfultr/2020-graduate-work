import cv2
import threading


def main_loop():
    cap = cv2.VideoCapture('http://169.254.104.205:8080/?action=stream')

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    thread = threading.Thread(target=main_loop).start()
    thread.start()
