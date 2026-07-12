import time

import cv2


index = 0
arr = []
cap = {}
while index<10:
    cap[index] = cv2.VideoCapture(index)
    if cap[index].read()[0]:
        arr.append(index)
    cap[index].release()
    index += 1

out = {}
fourcc = {}
cap = {}
for i in arr:
    cap[i] = cv2.VideoCapture(i)
    cap[i].set(3,640)
    cap[i].set(4,480)

    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    out[i] = cv2.VideoWriter('frames/output-'+str(i)+'.mp4', fourcc, 20.0, (640,480))

end = False
while not end:
    for i in arr:
        ret, frame = cap[i].read()
        out[i].write(frame)
        cv2.imshow('frame', frame)
        # Writes frame to file frames/frame.png with current timestamp as name
        timestamp = time.time()*1000.0
        cv2.imwrite('frames/frame-'+str(i)+'-' + str(timestamp) + '.png', frame)
        c = cv2.waitKey(1)
        if c & 0xFF == ord('q'):
            end = True

for i in arr:
    cap[i].release()
    out[i].release()
    cv2.destroyAllWindows()