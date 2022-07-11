#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
	video_size = {1: '240p',
				2: '360p',
				3: '480p',
				4: '720p',
				5: '1024p'}
	print(video_size[5])
	print(video_size.get(0,video_size[5]))

if __name__ == '__main__':
    main()
