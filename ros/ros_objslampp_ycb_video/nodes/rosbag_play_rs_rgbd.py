#!/usr/bin/env python

import subprocess

import gdown

import rospy


bag_file = gdown.cached_download(
    url='https://drive.google.com/uc?id=12Aa_DWauLHeKokNi5byPwpTeIaRIs8YF',
    md5='93f0bfd3b7e0a4e3ca00fbe39bbbc587',
)

cmd = f"rosbag play {bag_file} {' '.join(rospy.myargv()[1:])}"
print(f'+ {cmd}')
subprocess.call(cmd, shell=True)
