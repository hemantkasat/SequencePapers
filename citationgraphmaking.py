import json


jsonfile = open('./final_papers_id.json')
jsonfile_str = jsonfile.read()
final_papers_id = json.loads(jsonfile_str)

jsonfile = open('./final_papers_name.json')
jsonfile_str = jsonfile.read()
final_papers_name = json.loads(jsonfile_str)

jsonfile = open('./final_papers_class.json')
jsonfile_str = jsonfile.read()
final_papers_class = json.loads(jsonfile_str)

jsonfile = open('./final_papers_abstract.json')
jsonfile_str = jsonfile.read()
final_papers_abstract = json.loads(jsonfile_str)


with open('../../coradataset/citations') as f:
	edges = f.readlines()

edges = [x.strip() for x in edges]

edges_from_network = []

# print edges[3]
# print len(edges)

for ed in edges:
# 	# print ed.split('\t')
	# if((ed.strip().split('\t')[0] in final_papers_id) | (ed.strip().split('\t')[1] in final_papers_id)):
	edges_from_network.append([str(ed.split('\t')[0]),str(ed.split('\t')[1])])
	print len(edges_from_network)
# 
# 
print len(edges_from_network)

with open('./citationnetworkedges.json','rw+') as f:
	json.dump(edges_from_network,f)
