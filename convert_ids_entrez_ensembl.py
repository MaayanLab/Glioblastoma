import csv


with open("/Users/Carol/Desktop/MayoGlioblastomaProject/Work_files/probe_to_gene_names.txt", 'rU') as f:
    reader = csv.reader(f, delimiter="\t")
    d1 = {}
    for line in reader:
        if line[1] != "":
            #d1[line[0]] = int(line[1]) #convert to  ids ensembl
            d1[line[0]] = (line[1]) #convert to ids entrez

with open('/Users/Carol/Desktop/MayoGlioblastomaProject/Work_files/rma_summary_work_file.txt', 'rU') as f:
    reader = csv.reader(f, delimiter="\t")
    reader.next()  # Skip header row.
    d2 = {}
    for line in reader:
        d2[line[0]] = [float(i) for i in line[1:]]

d3 = {d1[k] if k in d1 else k: d2[k] for k in d2}

# with open('test.csv', 'a') as output:
#     a = csv.writer(output, delimiter=',')
#     a.writerows(d3)

with open('output_glio.txt','w') as output:
    output.write(str(d3))