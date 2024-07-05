import matplotlib.pyplot as plt
from wordcloud import WordCloud
import MeCab
import re

def CreateWordcloud(text):
    # MeCabを使用して日本語の単語を抽出
    #mecab = MeCab.Tagger("-Owakati")
    #text_wakati = mecab.parse(text)
    filtered_text = filter_words(text)
    font_path=".\wordcloud\ipaexg00401\ipaexg.ttf"
    # WordCloudオブジェクトを作成
    wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis', collocations=False, font_path=font_path).generate(filtered_text)

    # 画像を描画するためのプロットを作成
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    # 画像を表示
    plt.show()



def filter_words(text):
    mecab = MeCab.Tagger()
    node = mecab.parseToNode(text)
    words = []
    
    # ストップワードリスト
    stop_words = {'思い','さい','せ','よう','い','さ','う','よ','の', 'が', 'は', 'に', 'を', 'と', 'も', 'で', 'から', 'や', 'ば', 'へ', 'けど', 'です', 'ます', 'この', 'その', 'あの', 'だ', 'いる', 'ある', 'する', 'こと'}
    
    while node:
        word = node.surface
        pos = node.feature.split(',')[0]
        #ひらがなを除外
        if re.match(r'^[\u3040-\u309F]+$', word):
            node = node.next
            continue
        # 助詞、助動詞、記号、接続詞、ストップワードを除外
        if pos not in ['助詞', '助動詞', '記号', '接続詞'] and word not in stop_words:
            words.append(word)
        node = node.next
    
    return ' '.join(words)


if __name__ == '__main__':
    filename = input("ファイルパスを指定してください: ")
    with open(filename, 'r', encoding='utf-8') as file:
        mytext = file.read()
    CreateWordcloud(mytext)
