#! /usr/bin/env python

from __future__ import unicode_literals
import os
import youtube_dl

# Use of youtube-dl  is based on the example provided at
# https://github.com/rg3/youtube-dl#embedding-youtube-dl


class Logger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def progress_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


def process_file(file_path):
    ydl_opts = {
        'outtmpl': '~/Movies/YouTubeDownloads/%(uploader)s/%(title)s.%(ext)s'
    }

    with open(file_path) as f:
        lines = [line.rstrip('\n') for line in f if line != '' and line != '\n']

        if len(lines) > 0:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                for line in lines:
                    ydl.download([line])


def youtubedownloader():
    queue_path = '/Users/craigreynolds/Dropbox/Apps/YouTubeDownloader/'
    lock_path = os.path.join(queue_path, 'running.lock')

    if os.path.exists(lock_path):
        exit()

    lock_file = open(lock_path, 'w+')
    lock_file.close()

    directory_list = os.listdir(queue_path)
    queue_files = [file.rstrip('\n') for file in directory_list if file.endswith('.queue')]

    while len(queue_files) > 0:
        for filename in directory_list:
            file_path = os.path.join(queue_path, filename)

            if filename.endswith('queue'):
                try:
                    process_file(file_path)
                    os.rename(file_path, file_path.replace('.queue', '.handled'))
                except:
                    os.rename(file_path, file_path.replace('.queue', '.failed'))

        directory_list = os.listdir(queue_path)
        queue_files = [file.rstrip('\n') for file in directory_list if file.endswith('.queue')]

    os.remove(lock_path)


youtubedownloader()
