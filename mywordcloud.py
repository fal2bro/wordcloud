import matplotlib.pyplot as plt
from wordcloud import WordCloud
import MeCab

def CreateWordcloud(text):
    # MeCabを使用して日本語の単語を抽出
    mecab = MeCab.Tagger("-Ochasen")
    text_wakati = mecab.parse(text)
    fpath="./ipaexg00401\ipaexg.ttf"
    # WordCloudオブジェクトを作成
    wordcloud = WordCloud(font_path=fpath,width=800, height=400, background_color='white', colormap='viridis', collocations=False).generate(text_wakati)

    # 画像を描画するためのプロットを作成
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    # 画像を表示
    plt.show()

if __name__ == '__main__':
    filename = input("ファイルパスを指定してください: ")
    with open(filename, 'r', encoding='utf-8') as file:
        mytext = file.read()
    CreateWordcloud(mytext)
