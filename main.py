import zipfile
from Doc2Vec import Doc2Vec
# Read the data into a list of strings.
def read_data(filename):
  """Extract the first file enclosed in a zip file as a list of words"""
  with zipfile.ZipFile(filename) as f:
    data = f.read(f.namelist()[0]).split()
  return data


filename = '/home/shmuelfeld/Desktop/rt-polaritydata.zip'
path_for_files = '/home/shmuelfeld/Desktop/model/test_d2v_model'
path_for_restore = '/home/shmuelfeld/Desktop/model/test_d2v_model/model.ckpt'
words = read_data(filename)
words = words[:10000]
print('Data size', len(words))

# fake some docs
doc_length = 100
docs = [words[i:i+doc_length] for i in range(0, doc_length, len(words))]

vocabulary_size = 500

d2v = Doc2Vec(vocabulary_size=vocabulary_size,
	document_size=len(docs),
	n_steps=2001)
#
# # print w2v.get_params()
# d2v.fit(docs)
# print(d2v.word_embeddings.shape)
# print(d2v.doc_embeddings.shape)
#
# save_path = d2v.save(path_for_files)
# print(d2v.word_embeddings[0,0])
# print(d2v.doc_embeddings[0,0])
#
# print save_path
#
# # restore a saved model
# d2v_restored = Doc2Vec.restore(save_path)
# print(d2v_restored.word_embeddings[0,0])
# print(d2v_restored.doc_embeddings[0,0])

esti = d2v.restore(path_for_restore)
print "shani hamalka"