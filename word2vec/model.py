import logging
from gensim.models import word2vec

from config import PATH

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.LineSentence(PATH + 'in_the_name_of_people_segment.txt')

model = word2vec.Word2Vec(sentences, hs=1, min_count=10, window=3, vector_size=100)