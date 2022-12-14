import jieba
import wordcloud
from imageio import imread
mask = imread("fivestart.png")
f = open("关于实施乡村振兴战略的意见.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(width = 1000, height = 700, background_color = "white", \
                        max_words = 15, \
                        font_path = "msyh.ttc", mask=mask)
w.generate(txt)
w.to_file("grwordcloud.png")
