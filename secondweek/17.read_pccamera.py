import cv2
from Common.utils import put_string

capture = cv2.VideoCapture(0)  # 0번 카메라 연결
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")

# 카메라 속성 획득 및 출력
print("너비 %d" % capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print("높이 %d" % capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("노출 %d" % capture.get(cv2.CAP_PROP_EXPOSURE))
print("밝기 %d" % capture.get(cv2.CAP_PROP_BRIGHTNESS))

while True:  # 무한 반복
    ret, frame = capture.read()  # 카메라 영상 받기
    if not ret: break
    if cv2.waitKey(1) >= 0: break

    exposure = capture.get(cv2.CAP_PROP_EXPOSURE)
    put_string(frame, "EXPOS: ", (10, 40), exposure)
    title = "View Frame from Camera"
    cv2.imshow(title, frame)  # 윈도우에 영상 띄우기
capture.release()