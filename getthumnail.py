# Retrive thumnail pictures 

import cv2

filename="test.mp4"
cap=cv2.VideoCapture(filename)
outpath=(r'video')

width=0
height=0
fps=0
frame=0
length=0
codec=''


def playVideo():
    if(cap.isOpened()==False):
        print("Error on opening the video")
    while(cap.isOpened()):
        ret,frame=cap.read()
        if ret == True:
            cv2.imshow("Video",frame)
            if cv2.waitKey(25)&0xFF==ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindow()

def getVideoInfo(vc):
    global width, height,fps,frame,length,codec
    width =vc.get(cv2.CAP_PROP_FRAME_WIDTH)
    height=vc.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps   =vc.get(cv2.CAP_PROP_FPS)
    frame =vc.get(cv2.CAP_PROP_FRAME_COUNT)
    length=vc.get(cv2.CAP_PROP_FRAME_COUNT)
    fourcc=int(vc.get(cv2.CAP_PROP_FOURCC))
    codec =fourcc.to_bytes(4,"little").decode("utf-8")

def showVideoInfo():
    print(f'codec:{codec}, {width}x{height}, {fps:.2f}fps, frame:{frame}, length:{length}')


def buildVideoCaptures(vc,outputPath):
    min_one_thumb=0.5
    count = int(frame/fps/60/min_one_thumb)
    frameunit = frame/count
    print(f'output {count} thumbnails, frame unit is {frameunit}')
    for i in range(count):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i*frameunit)
        _, img=cap.read()
        w=img.shape[1]
        h=img.shape[0]
        #new_w=100
        new_w=w
        new_h=int(h*new_w/w)
        #print(f'new w/h:{new_w}/{new_h}')
        img=cv2.resize(img, (new_w,new_h))
        cv2.imwrite(outputPath+'/'+str(i).zfill(4)+'.jpg',  img)


getVideoInfo(cap)
showVideoInfo()
buildVideoCaptures(cap,outpath)






