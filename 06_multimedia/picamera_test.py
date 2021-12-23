import picamera
import time

path = '/home/pi/arc6/06_multimedia'

camera = picamera.PiCamera()

camera.resolution = (640,480)
camera.start_preview()

while True:
    val = input('photo:1 , video:2 , 9:exit > ')
    if val == '1':
        print('사진 촬영')
        now = time.strftime("%Y%m%d_%H%M%S")
        camera.capture('%s/photo_%s.jpg' % (path,now))
    elif val == '2':
        print('동영상 촬영')
        now = time.strftime("%Y%m%d_%H%M%S")
        time.sleep(1)
        camera.rotation = 180
        camera.start_recording('%s/video_%s.h264' % (path,now))
        input("press button to stop")
        camera.stop_recording()
    elif val == '9':
        camera.stop_preview()
        break
    else:
        print('틀린 명령어')