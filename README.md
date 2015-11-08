This is a simple script I use to facilitate downloading YouTube videos on my desktop.

It works like this:
- On my iOS device I copy the URL of a video
- I use the Workflow app to put that URL into a new time stamped file in a specific folder in my Dropbox. The files has an extension of .queue
- On my desktop Mac I have Hazel watch the folder where .queue files will appear. When it notices a new file it triggers the YouTubeDownloader.py script which handles the downloads from there