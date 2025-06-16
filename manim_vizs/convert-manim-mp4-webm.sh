# arg1: mp4 folder name
# arg2: mp4 file name

ffmpeg -i media/videos/$1/1080p60/$2.mp4 \
  -c:v libvpx-vp9 -b:v 0 -crf 35 -r 60 \
  $2.webm
