from sklearn import svm
import json
import numpy as np

import pandas as pd

from sklearn.model_selection import cross_val_score


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


jsonfile = open('./networkplusabstractembeddings.json')
jsonfile_str = jsonfile.read()
final_abstract_embeddings= json.loads(jsonfile_str)

print final_papers_class[4]
print final_papers_class[5]


print final_papers_class[1214].strip().split('/')


final_papers_class_broad = []

for i in range(len(final_papers_class)):
	final_papers_class_broad.append(str(final_papers_class[i].split('/')[1]))

# print len(final_papers_class_broad)
# print len(final_papers_class)

b = pd.get_dummies(final_papers_class_broad)

final_papers_class_id = b.values.argmax(1)


clf = svm.SVC(kernel='linear',C=10)
scores = cross_val_score(clf, final_abstract_embeddings, final_papers_class_id, cv=5, scoring='f1_macro')

print scores
