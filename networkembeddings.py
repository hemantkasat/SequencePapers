
import json

with open('./networkplusabstractembeddings.txt') as f:
	id_embeddings = f.readlines()

id_embeddings = [x.strip() for x in id_embeddings]

# print len(id_embeddings)
# print id_embeddings[3]

id_embeddings_dict = {}

paper_id = []
paper_embeddings = []

del id_embeddings[0]

print id_embeddings[0]


for i in range(len(id_embeddings)):
	paper_id = id_embeddings[i].split(' ')[0]
	id_embeddings_dict[paper_id] = id_embeddings[i].split(' ')[1:]


# print id_embeddings_dict['2']

print id_embeddings_dict['1145049']



jsonfile = open('./final_papers_id.json')
jsonfile_str = jsonfile.read()
final_papers_id = json.loads(jsonfile_str)


# count = 0

# ids_not_in_graph = []
# for i in range(len(final_papers_id)):
# 	print "checking "
# 	print i
# 	if(final_papers_id[i] not in id_embeddings_dict.keys()):
# 		count = count + 1
# 		ids_not_in_graph.append(final_papers_id[i])
# 		print count

# print count 



networkplusabstractembeddings = []

for i in range(len(final_papers_id)):
	networkplusabstractembeddings.append(id_embeddings_dict[str(final_papers_id[i])])

print len(networkplusabstractembeddings)

with open('./networkplusabstractembeddings.json','rw+') as f:
	json.dump(networkplusabstractembeddings,f)



