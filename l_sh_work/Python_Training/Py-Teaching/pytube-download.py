#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pip install pytube

import pathlib
import pytube

def on_progress(stream, chunk, bytes_remaining):
	total_size = stream.filesize
	bytes_downloaded = total_size - bytes_remaining
	percentage_of_completion = round(bytes_downloaded / total_size * 100)
	print(percentage_of_completion)

def filterName(innames: str) -> str:
	outname = str(innames).replace('|', '.').replace('%', '.').replace(':', '.').replace('"', '.').replace("'", ".").replace('<', '.').replace('>', '.')\
	.replace('[', '.').replace(']', '.').replace('{', '.').replace('}', '.').replace('#', '.').replace('$', '.').replace('?', '.')\
	.replace('`', '.').replace('~', '.').replace('@', '.').replace('!', '.').replace('&', '.').replace('^', '.').replace('*', '.')
	return outname

def getTitle(urlFile: str) -> str:
	yt = pytube.YouTube(urlFile)
	outname = filterName(yt.title) + '.mp4'
	return outname

def downloadYouTube(urlFile: str, yourPath: str = None, FName: str = None, quality: str = '720p'):
	yt = pytube.YouTube(urlFile, on_progress_callback=on_progress)
	yt = yt.streams.filter(progressive=True, mime_type="video/mp4", res="720p").first()
	yt.download(output_path=yourPath, filename=FName)

def main():
	playlist = pytube.Playlist('playlist-url')
	all_count = str(len(playlist.video_urls))
	print('Number of videos in playlist: %s' % len(playlist.video_urls))
	'''
	with open('selfedu.txt', 'w') as the_file:
		index=1
		for url in playlist.video_urls:
			the_file.write(str(index))
			the_file.write(' ')
			the_file.write(url)
			the_file.write('\n')
			index+=1
	'''
	download_path = str(pathlib.Path(pathlib.Path.cwd()).resolve().joinpath("download-folder-1024p"))
	if not pathlib.Path(download_path).exists():
		pathlib.Path(download_path).mkdir(parents=True, exist_ok=True)
	video_url = [] 
	for url in playlist.video_urls:
		video_url.append(url)
	#video_link = 'video-url'
	#index = 1
	#fname = str(index) + '.' + getTitle(video_link)
	#downloadYouTube(video_link, download_path, fname)
	#yt = pytube.YouTube(video_link, on_progress_callback=on_progress)
	#yt = yt.streams.filter(progressive=True, mime_type="video/mp4", res="720p").order_by('resolution').desc().first()
	#yt = yt.streams.filter(progressive=True, mime_type="video/mp4", res="720p").first() # fps="24fps"
	#yt.download(download_path)
	#print(yt.streams)
	#titles = filterName(yt.title)
	#print(titles)
	index = 1
	for onURL in video_url:
		fname = str(index) + '.' + getTitle(onURL)
		print(fname, all_count)
		downloadYouTube(onURL, download_path, fname, '1024p')
		index+=1

if __name__ == '__main__':
    main()
