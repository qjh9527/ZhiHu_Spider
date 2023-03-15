# @Time : 2023/3/18 17:56
"""
1. 读取 favorites_2023_3_13.html 的文本
2. 通过bs4的库获取其中关于zhihu的内容
3. 筛掉含有answer的内容
4. 将剩余的部分通过 问题、用户、文章、专栏等保存到 else目录下
"""

from bs4 import BeautifulSoup
import os

question = ''
answer = ''
zhuanlan = ''
people = ''
column = ''

with open('favorites_2023_3_13.html', 'r', encoding='utf8') as f:
    html = f.read()

bs = BeautifulSoup(html, "html.parser")
for item in bs.find_all("a"):
    href = item.get("href")
    text = item.get_text()
    row = f'- [{text}]({href})\n'
    if 'zhihu.com' in href:
        if '/question/' in href:
            if '/answer/' in href:
                answer += row
            else:
                question += row
        elif '/zhuanlan.' in href:
            zhuanlan += row
        elif '/people/' in href:
            people += row
        elif '/column/' in href:
            column += row
        # print(href)
        # print(text)

var_list = [question, answer, zhuanlan, people, column]
file_list = ['question.md', 'answer.md', 'article.md', 'user.md', '专栏-column.md']
root_dir = r'D:\Code\Spider\ZhiHu_Spider\Markdown\else'
for file, var in zip(file_list, var_list):
    md_file_path = os.path.join(root_dir, file)
    with open(md_file_path, 'a', encoding='utf8') as f:
        f.write(var)
