import os
import subprocess
import sys
import shutil
import cv2

if os.path.exists('frames'):
	shutil.rmtree('frames')
os.mkdir('frames')
os.system('wsl ffmpeg -y -i ' + sys.argv[1] + ' -an -vf mpdecimate,setpts=N/FRAME_RATE/TB 2.' + sys.argv[1])
os.system('wsl ffmpeg -i 2.' + sys.argv[1] + ' frames/%d.bmp')
if os.path.exists('2.' + sys.argv[1]):
  os.remove('2.' + sys.argv[1])
i = 1

while os.path.exists('frames/'+str(i+1)+'.bmp'):
	A = cv2.imread('frames/'+str(i)+'.bmp')
	B = cv2.imread('frames/'+str(i+1)+'.bmp')
	similarity = 1 - cv2.norm( A, B, cv2.NORM_L2 ) / ( A.shape[0] * A.shape[1] )
	if similarity > 0.985:
		os.remove('frames/'+str(i)+'.bmp')
	i+=1

os.system('wsl ./rename.sh')

for file1 in os.listdir('frames'):
	if (os.path.exists(os.path.join('frames', file1))):
		for file2 in os.listdir('frames'):
			if file1 != file2:
				A = cv2.imread(os.path.join('frames', file1))
				B = cv2.imread(os.path.join('frames', file2))
				similarity = 1 - cv2.norm( A, B, cv2.NORM_L2 ) / ( A.shape[0] * A.shape[1] )
				if similarity > 0.985:
					os.remove(os.path.join('frames', file2))
					
os.system('wsl convert frames/*.bmp presentation.pdf')
os.system('wsl ocrmypdf presentation.pdf presentation_ocr.pdf')

if os.path.exists('presentation.pdf'):
  os.remove('presentation.pdf')
os.rename('presentation_ocr.pdf', sys.argv[2])