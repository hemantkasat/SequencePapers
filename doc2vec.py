import json
from gensim.models.doc2vec import LabeledSentence, Doc2Vec


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


docs = []

for i in range(len(final_papers_id)):
	word = final_papers_abstract[i].lower().split()
	tag = [str(final_papers_id[i])]
	docs.append(LabeledSentence(words=word,tags=tag))


# abstract_vectors = open('./abstract_vectors_model','rw+')

# model = Doc2Vec(docs, size = 100, window = 5, min_count = 1)
# model.save(abstract_vectors)

model = Doc2Vec.load('./abstract_vectors_model')

final_abstract_embeddings = []

# print model.docvecs[str(final_papers_id[1])].tolist()

for i in range(len(final_papers_id)):
	final_abstract_embeddings.append(model.docvecs[str(final_papers_id[i])].tolist())


print len(final_abstract_embeddings)

with open('./final_abstract_embeddings.json','rw+') as f:
	json.dump(final_abstract_embeddings,f)


similarity_edges = []

for i in range(len(final_papers_id)):
	sim = model.docvecs.most_similar(str(final_papers_id[i]))
	for item in sim:
		if(item[1]>0.9):
			similarity_edges.append([int(final_papers_id[i]),int(item[0])])


print len(similarity_edges)

print similarity_edges[3]


with open('./similarity_edges.json','rw+') as f:
	json.dump(similarity_edges,f)