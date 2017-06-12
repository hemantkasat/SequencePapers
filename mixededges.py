import json

jsonfile = open('./similarity_edges.json')
jsonfile_str = jsonfile.read()
similarity_edges = json.loads(jsonfile_str)

jsonfile = open('./citationnetworkedges.json')
jsonfile_str = jsonfile.read()
citationnetworkedges = json.loads(jsonfile_str)

jsonfile = open('./final_papers_id.json')
jsonfile_str = jsonfile.read()
final_papers_id = json.loads(jsonfile_str)


# print similarity_edges[1]
# print len(similarity_edges)
# print citationnetworkedges[1]

# print len(citationnetworkedges)

extra_edges = []

for i in range(len(citationnetworkedges)):
	citationnetworkedges[i][0] = int(citationnetworkedges[i][0])
	citationnetworkedges[i][1] = int(citationnetworkedges[i][1])

# print citationnetworkedges[1]

# print similarity_edges[0][0],citationnetworkedges[0][0]

for i in range(len(similarity_edges)):
	flag=0
	for j in range(len(citationnetworkedges)):
		if((similarity_edges[i][0]==citationnetworkedges[j][0]) & (similarity_edges[i][1]==citationnetworkedges[j][1])):
			print "edge already there"
			flag = 1
		if((similarity_edges[i][0]==citationnetworkedges[j][1]) & (similarity_edges[i][1]==citationnetworkedges[j][0])):
			print "edge already there"
			flag=1

	if(flag==0):
		print "edge created"
		extra_edges.append(similarity_edges[i])
		# print similarity_edges[i]
	print i


print len(similarity_edges)
print len(citationnetworkedges)
print len(extra_edges)

citationplussimilarityedges = citationnetworkedges + extra_edges

from gensim.models.doc2vec import LabeledSentence, Doc2Vec
model = Doc2Vec.load('./abstract_vectors_model')


nodes_in_graph = []
for i in range(len(citationplussimilarityedges)):
	nodes_in_graph.append(citationplussimilarityedges[i][0])
	nodes_in_graph.append(citationplussimilarityedges[i][1])


count = 0
for i in range(len(final_papers_id)):
	if int(final_papers_id[i]) not in nodes_in_graph:
		count = count + 1
		sim = model.docvecs.most_similar(str(final_papers_id[i]))
		citationplussimilarityedges.append([int(final_papers_id[i]),int(sim[0][0])])
	print count
print count


print len(citationplussimilarityedges)
# print len(citationplussimilarityedges)
print citationplussimilarityedges[3]

with open('citationplussimilarityedges.json','rw+') as f:
	json.dump(citationplussimilarityedges,f)



		