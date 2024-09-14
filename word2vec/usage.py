from model import model

print("选出最相似的5个词")
for e in model.wv.similar_by_word('沙瑞金', topn=5):
    print(e[0], e[1])

print("选出词汇相对于另一组词汇的对应词")
model.wv.most_similar(positive=['李达康', '欧阳菁'], negative=['侯亮平'])

print("计算两个词的相似度")
print(model.wv.similarity('沙瑞金', '季昌明'))
print(model.wv.similarity('沙瑞金', '田国富'))
