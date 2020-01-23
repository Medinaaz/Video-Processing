import cv2
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.io.VideoFileClip import VideoFileClip
import re
bad_chars = ['[','"',']','{','}','"guestTeam":"USA","homeTeam":"Turkey"}','events:','0','1','2','3','4','5','6','7','8','9','?','\n']
bad_chars1 = ['[','"',']','{','}','guestTeam":"USA","homeTeam":"Turkey"}','events:','?']
content_array = []
f = open("game_data.txt", "r")
   #Content_list is the list that contains the read lines.
for line in f:
    content_array.append(line)
    content_array = [w.replace(',', ' ') for w in content_array]
    #print(content_array)

event1 = []
event2 = []
event3 = []
event4 = []
event1 = content_array[0]
event2 = content_array[1]
event3 = content_array[2]
event4 = content_array[3]
for i in bad_chars:
    event2 = event2.replace(i, '')
    event1 = event1.replace(i, '')
    event3 = event3.replace(i, '')
    event4 = event4.replace(i, '')

output_video_path1 = '/home/XX/PycharmProjects/untitled/crop1.mp4'
output_video_path2 = '/home/XX/PycharmProjects/untitled/crop2.mp4'
output_video_path3 = '/home/XX/PycharmProjects/untitled/crop3.mp4'
output_video_path4 = '/home/XX/PycharmProjects/untitled/crop4.mp4'

cap = cv2.VideoCapture('crop4.mp4')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
size = (width, height)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('action4.mp4', fourcc, 20.0, size)
#out = cv2.VideoWriter('output.mp4', -1, 20.0, (480,480))
# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

# Read until video is completed
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        fps = cap.get(cv2.CAP_PROP_FPS)  # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps
        minutes = int(duration / 60)
        seconds = duration % 60
        print('duration (M:S) = ' + str(minutes) + ':' + str(seconds))
        # Display the resulting frame
        frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        #constraint for the time specified

        print("Position : %d" % cap.get(cv2.CAP_PROP_POS_MSEC))
        """Pop up text at a required time"""
        if(cap.get(cv2.CAP_PROP_POS_MSEC)):
         cv2.rectangle(frame,(550,0),(0,70),(96, 15, 255),3)
         cv2.putText(img=frame, text=event4, org=(50,50),
                     fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                     color=(173, 241, 255))

         #fourcc = cv2.VideoWriter_fourcc(*'MJPG')
         #out = cv2.VideoWriter('output.avi', fourcc, 20.0, (480, 480))

        """Show the text for all frames"""
        cv2.imshow('Frame', frame)
        out.write(frame)
            # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
          break

        # Break the loop
    else:
        break


cap.release()
cv2.destroyAllWindows()
"""    # Closes all the frames"""


"""other part of the code"""

content_array1 = []
f1 = open("game_data.txt", "r")

#Content_list is the list that contains the read lines.
for line in f1:
    content_array1.append(line)
    content_array1 = [w.replace(',', ' ') for w in content_array1]
    #print(content_array)

#remove the bad characters
event1_1 = []
event2_1 = []
event3_1 = []
event4_1 = []
event1_1 = content_array1[0]
event2_1 = content_array1[1]
event3_1 = content_array1[2]
event4_1 = content_array1[3]
for i in bad_chars1:
    event2_1 = event2_1.replace(i, '')
    event1_1 = event1_1.replace(i, '')
    event3_1 = event3_1.replace(i, '')
    event4_1 = event4_1.replace(i, '')


event1_time1 = list(map(int,re.findall('\d+',event1_1)))
event1_time1[0]=int((event1_time1[0])/1000)
print(event1_time1[0])

event2_time2 = list(map(int,re.findall('\d+',event2_1)))
event2_time2[0]=int((event2_time2[0])/1000)
print(event2_time2[0])

event3_time3 = list(map(int,re.findall('\d+',event3_1)))
event3_time3[0]=int((event3_time3[0])/1000)
print(event3_time3[0])

event4_time4 = list(map(int,re.findall('\d+',event4_1)))
event4_time4[0]=int((event4_time4[0])/1000)
print(event4_time4[0])

#read the video and crop it


my_clip = VideoFileClip('/home/XX/PycharmProjects/untitled/USA_Turkey.mp4')
new1 = my_clip.subclip(event1_time1[0], event1_time1[0]+4)
new1.write_videofile(output_video_path1, audio_codec='aac')
new1.close()

new2 = my_clip.subclip(event2_time2[0], event2_time2[0]+4)
new2.write_videofile(output_video_path2, audio_codec='aac')
new2.close()

new3 = my_clip.subclip(event3_time3[0], event3_time3[0]+4)
new3.write_videofile(output_video_path3, audio_codec='aac')
new3.close()

new4 = my_clip.subclip(event4_time4[0], event4_time4[0]+4)
new4.write_videofile(output_video_path4, audio_codec='aac')
new4.close()
