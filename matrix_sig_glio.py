import codecs
import numpy as np
from scipy import stats
import os

# read only rows of matrix with fewer than 5% of values missing and then replace any remaining zeros with row mean
with codecs.open('/Users/Carol/Desktop/MayoGlioblastomaProject/Work_files/output_glio.txt', encoding='utf-8', mode='r') as fr:
	line = fr.readline()
	columnlabels = line.strip().split('\t')[2:] #
	numcols = len(columnlabels)
	datamatrix = []
	genes = []
	for line in fr:
		entries = line.strip().split('\t')
		gene = entries[0]
		values = []
		numzeros = 0
		valuesum = 0
		for entry in entries[2:]:
			value = float(entry)
			valuesum += value
			values.append(value)
			if value == 0:
				numzeros += 1
		if numzeros < 0.05*numcols:
			valuemean = valuesum/(numcols - numzeros)
			for i, value in enumerate(values):
				if value == 0:
					values[i] = valuemean
			genes.append(gene)
			datamatrix.append(values)

# convert datamatrix to numpy two-dimensional array
datamatrix = np.array(datamatrix)

# log2 transformation
# datamatrix = np.log2(datamatrix)

# quantile normalization
# sortedrowmeans = np.mean(np.sort(datamatrix, axis=0), axis=1)
# backsortedindices = np.argsort(np.argsort(datamatrix, axis=0), axis=0)
# for j in range(numcols):
# 	datamatrix[:,j] = sortedrowmeans[backsortedindices[:,j]]

# z-score
datamatrix = stats.zscore(datamatrix, axis=1)

# create folder for saving signatures
folders = os.listdir('./')
savefolder = 'signatures'
if savefolder not in folders:
	os.mkdir(savefolder)

# specify meta-data
metadata = ['!required_metadata',
'!organism: homo sapiens',
'!diff_exp_method: z-score',
'!cutoff: null',
'!processed: true',
'!source: Mayo Glioblastoma',
'',
'!optional_metadata',
'!cancer_type: Glioblastoma',
'!sample_id: insertsampleid',
'',
'!end_metadata',
'',
'']

# specify prefix of output files
savefileprefix = 'gliobasltoma_mayo_'

# write signatures to separate files
for j, columnlabel in enumerate(columnlabels):
	savefile = savefolder + '/' + savefileprefix + str(j+1) + '.txt'
	metadatastring = '\n'.join(metadata).replace('insertsampleid', columnlabel)
	with codecs.open(savefile, encoding='utf-8', mode='w') as fw:
		fw.write(metadatastring)
		for i, gene in enumerate(genes):
			fw.write('{0}\t{1!s}\n'.format(gene, datamatrix[i,j]))
