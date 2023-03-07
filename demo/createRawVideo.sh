#!/bin/bash

OVERLAY=$2

ffmpeg \
    -f video4linux2 \
    -i /dev/video0 \
    -vcodec libx264 \
    -vprofile baseline \
    -pix_fmt yuv420p \
    -f flv rtmp://127.0.0.1:1935/raw
    #-f rtp rtp://127.0.0.1:8000/raw
    #-f flv rtmp://127.0.0.1:1935/ideo/stream
