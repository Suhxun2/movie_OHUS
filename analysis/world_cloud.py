import pprint
from collections import Counter
from db.movie_crud import get_reviews
from konlpy.tag import Okt
import numpy as np
from wordcloud import WordCloud
from PIL import Image

# 1.Load reviews form MongoDB

reviews = get_reviews()
print("=" * 50)
print(f"= 총 {len(reviews)}건의 리뷰")
print("=" * 50)

okt = Okt()
doc = ""

for one in reviews:
    doc += one[2]

nouns_list = okt.nouns(doc)

print(f"= [전체 단어(명사)수] → {len(nouns_list)}", )
print(f"= [중복제거 후 전체 단어(명사)수] → {len(set(nouns_list))}")

word_list = []
for noun in nouns_list:
    if len(noun) >= 2:  # 2글자 이상만 추출
        word_list.append(noun)

print(f"= [최종 단어수(2글자 이상)] → {len(set(word_list))}", )
print("=" * 50)
print(f"= [상위 10개 단어] →")
pprint.pprint(Counter(word_list).most_common(10))
print("=" * 50)

most_list = Counter(word_list).most_common(500)

# mask 만들기
circle_mask = np.array(Image.open("movie_apple/img/circle.png"))
cnu_circle_mask = np.array(Image.open("movie_apple/img/CNU_circle_logo.png"))
cnu_text_mask = np.array(Image.open("movie_apple/img/cnu_text.png"))
wc = WordCloud(

    # font_path="‪C:\\Windows\\Fonts\\NanumGothic.ttf",
    # mask=cnu_circle_mask,
    font_path="malgun",
    background_color="white",
    width=400,
    height=400,
    max_words=100,
    max_font_size=300,
    mask=circle_mask

)

wc.generate_from_frequencies(dict(most_list))
wc.to_file('wc.png')