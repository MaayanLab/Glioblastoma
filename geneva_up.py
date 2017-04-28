import json
import requests
import os
import csv 
files = os.listdir("/Users/lab/Desktop/work/projects/glioblastoma/glioblastoma_sigs")

for f in files:

	fname = "/Users/lab/Desktop/work/projects/glioblastoma/glioblastoma_sigs/"+f 
	ft = f
	ft = os.path.splitext(ft)[0]
	print(ft)

	genes=[]
	with open(fname,'rb') as f:
	#   data = f.readlines()[13:]
	#   for line in data:
	#    content=data[13:]
	#    description=content[:10]
	# genes= "".join(content)
	# genes=[]
	# for line in f:
	# 	csv.reader(f)
	# 	genes=''.join(line[:-1])
	# 	ranked_genes=zip(genes)
		data = f.readlines()
		for line in data:
			line=line.split(',')
			#print(line)
			genes.append(line)
			#print(genes)
			payload = {
			'ranked_genes': genes,
			'diffexp_method': 'z-score',
			'tags': 'Glioblastoma',
			'title': ft,
			}

			print(payload)

			#resp = requests.post('http://amp.pharm.mssm.edu/gen3va/api/1.0/upload', data=json.dumps(payload))