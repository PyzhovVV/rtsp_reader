import os
import time

import cv2

username = ''
password = ''
endpoint = ''
ip = ''


def rtsp_video(seconds: int):
    cap = cv2.VideoCapture(f'rtsp://{username}:{password}@{ip}/{endpoint}')
    out = cv2.VideoWriter(
        filename='RevisorVision.avi',
        fourcc=cv2.VideoWriter_fourcc('P', 'I', 'M', '1'),
        fps=24.0,
        frameSize=1024,
        isColor=True,
    )
    start_time = time.time()
    while True:
        if cap.isOpened():
            ret, frame = cap.read()
            if ret is True:
                seconds_passed = int(time.time() - start_time)
                if seconds_passed > seconds:
                    print('Запись окончена успешно')
                    break
                out.write(frame)
                cv2.imshow('frame', frame)
                if cv2.waitKey(20) == ord('q'):
                    print('Запись прервана нажатием кнопки')
                    break
            else:
                print('Битый кадр')
                break
        else:
            print('Потеря соединения')
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


def compress(source_video, video_finale):
    os.system(f'ffmpeg -i {source_video} -vcodec libx265 -crf 28 fps-fps=30 {video_finale}')
    return


def transcoding(source_video,  video_finale):
    os.system(f'ffmpeg -i {source_video} {video_finale}')
    return
