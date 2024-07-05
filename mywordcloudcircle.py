import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
import mywordcloud

def create_wordcircle(text):
    filtered_text = mywordcloud.filter_words(text)
    font_path=".\wordcloud\ipaexg00401\ipaexg.ttf"
    # WordCloudオブジェクトを作成
    wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis', collocations=False, font_path=font_path).generate(filtered_text)

    # 画像を描画するためのプロットを作成
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    word_positions = {item[0]: item[1] for item in wordcloud.layout_}
    for word, freq in wordcloud.words_.items():
        fontsize = np.log2(freq + 1) * 20  # 単語の頻度に基づいてフォントサイズを調整
        position = word_positions[word]
        plt.text(position[0], position[1], word, fontsize=fontsize, ha='center', va='center', bbox=dict(boxstyle="circle,pad=0.3", edgecolor='black', facecolor='none'))

    # 画像を表示
    plt.show()


if __name__ == '__main__':
    filename = input("ファイルパスを指定してください: ")
    with open(filename, 'r', encoding='utf-8') as file:
        mytext = file.read()
    create_wordcircle(mytext)
