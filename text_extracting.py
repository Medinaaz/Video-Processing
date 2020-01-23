from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.io.VideoFileClip import VideoFileClip
import re
import cv2
import just
# When everything done, release the video capture object"""
bad_chars1 = ['[','"',']','{','}','guestTeam:USA,homeTeam:Turkey','events:','?']
content_array = []
f = open("game_data.txt", "r")

#Content_list is the list that contains the read lines.
for line in f:
    content_array.append(line)
    content_array = [w.replace(',', ' ') for w in content_array]
    #print(content_array)

#remove the bad characters
event1 = []
event2 = []
event3 = []
event1 = content_array[0]
event2 = content_array[1]
event3 = content_array[2]
event4 = content_array[3]
for i in bad_chars1:
    event2 = event2.replace(i, '')
    event1 = event1.replace(i, '')
    event3 = event3.replace(i, '')
    event4 = event4.replace(i, '')


event1_time = list(map(int,re.findall('\d+',event1)))
event1_time[0]=int((event1_time[0])/1000)
print(event1_time[0])

event2_time = list(map(int,re.findall('\d+',event2)))
event2_time[0]=int((event2_time[0])/1000)
print(event2_time[0])

event3_time = list(map(int,re.findall('\d+',event3)))
event3_time[0]=int((event3_time[0])/1000)
print(event3_time[0])

event4_time4 = list(map(int,re.findall('\d+',event4)))
event4_time4[0]=int((event4_time4[0])/1000)
print(event4_time4[0])

#read the video and crop it
output_video_path1 = '/home/XX/PycharmProjects/untitled/crop1.mp4'
output_video_path2 = '/home/XX/PycharmProjects/untitled/crop2.mp4'
output_video_path3 = '/home/XX/PycharmProjects/untitled/crop3.mp4'
output_video_path4 = '/home/XX/PycharmProjects/untitled/crop4.mp4'



my_clip = VideoFileClip('/home/XX/PycharmProjects/untitled/USA_Turkey.mp4')
new1 = my_clip.subclip(event1_time[0], event1_time[0]+4)
new1.write_videofile(output_video_path1, audio_codec='aac')
new1.close()

new2 = my_clip.subclip(event2_time[0], event2_time[0]+4)
new2.write_videofile(output_video_path2, audio_codec='aac')
new2.close()

new3 = my_clip.subclip(event3_time[0], event3_time[0]+4)
new3.write_videofile(output_video_path3, audio_codec='aac')
new3.close()

new4 = my_clip.subclip(event4_time4[0], event4_time4[0]+4)
new4.write_videofile(output_video_path4, audio_codec='aac')
new4.close()
#re-open again but now as cv2 and plot the text in each part

