import os
import sys
import numpy as np

COLORS = [
	"255,0,0", #red
	"0,255,0", #lime
	"0,0,255", #blue
	"0,255,255", #cyan
	"255,0,255", #magenta
	"128,0,0", #maroon
	"128,128,0", #olive
	"128,0,128", #purple
	"0,128,128", #teal
	"0,0,128", #navy
	"189,183,107", #dark khaki
	"255,228,225", #misty rose
	"139,69,19", #saddle brown
	"255,105,180", #hot pink
	"255,140,0", #dark orange
	"192,192,192", #silver
	"178,34,34", #firebrick
	"205,92,92", #indian red
	"218,165,32", #golden rod
	"238,130,238", #violet
	"244,164,96", #sandy brown
	"0,0,0", #black
	"128,128,128" #gray 
	]	

def rootname(f):
	a = os.path.basename(f)
	aParts = a.split('.')
	return aParts[0]

def makeTrackStr(f,tag,color):
	str = (
		'track ' + tag + '\n'
		'bigDataUrl ' + f + '\n'
		'shortLabel ' + tag + '\n'
		'longLabel '  + tag + '\n'
		'type bigWig\n'
		'color '+color+'\n'
        	'visibility full\n'
        	'autoScale on\n'
		'graphTypeDefault bar\n'
		'windowingFunction mean\n'
#		'viewLimits 0.0:1000.0\n'
		'smoothingWindow 12\n'
		'spectrum on\n\n\n'
	       )
	return str

#get top folders
top_folders = [a for a in os.listdir('hg19') if os.path.isdir('hg19/' + a)]
top_folders.sort()

#folder iter
fout = open('hg19/trackDb.txt','w')
for f in top_folders:
	files = [f + '/' + a for a in os.listdir('hg19/' + f) if ".bigWig" in a]
	for urlIndex in xrange(0,len(files)):
		url = files[urlIndex]
		command = makeTrackStr(url,f+'-'+rootname(url),COLORS[np.random.randint(len(COLORS))])
		if(f==top_folders[-1] and urlIndex==len(files)-1):
			command = command.rstrip()
		fout.write(command)
fout.close()
