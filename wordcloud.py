

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

# Read text from file
text_from_file_with_apath = open('test.txt').read()

# Word segment using jieba (https://github.com/fxsjy/jieba)
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

# Create wordcloud using WordCloud (https://github.com/amueller/word_cloud)
my_wordcloud = WordCloud().generate(wl_space_split)

# Show result
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
 
