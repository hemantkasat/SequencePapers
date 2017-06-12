
import os.path
import json


classification_file = open('../../coradataset/classifications')

with open('../../coradataset/classifications') as f:
	papername_class = f.readlines()

papername_class = [x.strip() for x in papername_class]
del papername_class[-1]

# print len(papername_class)

papernames = []
classes = []
for p in papername_class:
	papernames.append(p.split('\t')[0])
	classes.append(p.split('\t')[1])

# print len(papernames)
# print len(classes)

papers_file = open('../../coradataset/papers')

with open('../../coradataset/papers') as f:
	paper_id_name_detail = f.readlines()


paper_id_name_detail = [x.strip() for x in paper_id_name_detail]

# print len(paper_id_name_detail)


papers_id = []   #may or may not have class labels
papers_names = []  #may or may not have class labels

for p in paper_id_name_detail:
	if(len(p.split('\t'))>=2):
		if(os.path.isfile('../../coradataset/extractions/' + p.split('\t')[1])):
			papers_id.append(p.split('\t')[0])
			papers_names.append(p.split('\t')[1])

# print len(papers_id)


final_papers_id = []
final_papers_name = []
final_papers_class = []
final_papers_abstract = []
for i in range(len(papernames)):
	if(papernames[i] in papers_names):
		ind = papers_names.index(papernames[i])
		final_papers_id.append(papers_id[ind])
		final_papers_name.append(papernames[i])
		final_papers_class.append(classes[i])


print len(final_papers_id)
print len(final_papers_name)
print len(final_papers_class)

# count = 0


files_withnoabstract = []
for file in final_papers_name:
	flag = 0
	flag1=0
	with open('../../coradataset/extractions/' + file) as f:
		paper_content = f.readlines()

	paper_content = [x.strip() for x in paper_content]
	for p in paper_content:
		if(p.split(':')[0]=='Abstract'):
			flag = 1
			final_papers_abstract.append(p.split(':')[1])
	if(flag==0):
		files_withnoabstract.append(file)
		
print len(final_papers_abstract)
# print len(files_withnoabstract)


with open('./final_papers_id.json','rw+') as f:
	json.dump(final_papers_id,f)

with open('./final_papers_name.json','rw+') as f:
	json.dump(final_papers_name,f)


with open('./final_papers_class.json','rw+') as f:
	json.dump(final_papers_class,f)


with open('./final_papers_abstract.json','rw+') as f:
	json.dump(final_papers_abstract,f)

# with open('../../coradataset/citations') as f:
# 	edges = f.readlines()

# edges = [x.strip() for x in edges]

# edges_from_network = []

# for ed in edges:
# 	# print ed
# 	if((ed.strip().split('\t')[0] in final_papers_id) & (ed.strip().split('\t')[1] in final_papers_id)):
# 		edges_from_network.append(ed)

# print len(edges_from_network)