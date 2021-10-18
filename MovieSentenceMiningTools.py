from moviepy.editor import *
import os
class Subtitle:
	"""
	
	Attributes
	id
		id corresponding to order in the 
	start
		start location in seconds
	end
		end location in seconds
	text
		text for the subtitle
	AudioFileClip
		moviepy AudioFIleClip of the subtitle being spoken
	"""
	def __init__(self, id, start, end, text, audio_clip):
		self.id = id
		self.start = start
		self.end = end
		self.text = text
		self.AudioFileClip = self.cut_audio(audio_clip)
	
	def cut_audio(self, audio_clip):
		"""
		Take the moviepy AudioFileClip instance for this
		show and cut out the audio corresponding to the 
		subtitle
		"""
		return audio_clip.subclip(self.start, self.end)
	
	def save_clip(self, dir):
		"""
		"""
		self.AudioFIleClipwrite_audiofile(dir)

class Show:
	"""
	
	"""
	def __init__(self, mp4_dir, subtitles_dir):
		self.mp4_dir = mp4_dir
		self.subtitles_dir = subtitles_dir
		self.subtitles = []
		
		#TODO: add self.audiofileclip
		
		
	def parse_srt_file(self):
		"""
		Read through the srt file of subtitles and
		for each subtitle create a 
		"""
		subtitles_file = open(self.dir, 'r')
		subtitle_id = 0
		last_line = ""
		for line in subtitles_file.readlines():
			subtitle_text = None
			start_time = None
			end_time = None
			if last_line=="":
				subtitle_id += 1
				if int(line)<>subtitle_id:
					print("things not as expected")
			elif (last_line<>"") & (len(line.split(" --> "))>1):
				split_string = line.split(" --> ")
				start_string = split_string[0]
				end_string = split_string[1]
			elif (last_line<>"") & (len(line.split(" --> "))<=1):
				start_time = parse_time_string(line.split(" --> ")[0])
				end_time = parse_time_string(line.split(" --> ")[1])
			self.subtitles.append(Subtitle(id = ,
											start = start_time, 
											end = end_time, 
											text = subtitle_text, 
											audio_clip = self.audiofileclip
											)
								)
			last_line = line
	
	def parse_time_string(self, string):
		"""
		Parse a subtitle time string
		
		for instance take '00:00:30,416' and return 30.416
		"""
		milisecs = int(string.split(",")[1])
		hours_mins_seconds = string.split(",")[0]
		
		hours, mins, secs = [int(i) for i in hours_mins_seconds.split(":")]
		
		return (hours*3600) +(mins*60) + secs + (milisecs/1000)
		