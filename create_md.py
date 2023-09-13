import os

from bs4 import BeautifulSoup
from html2markdown import convert
from database import SQL


def create_file(output, mode='Markdown'):
    suffix = 'md' if mode == 'Markdown' else 'html'

    output.append('-' * 15 + 'Markdown' + '-' * 15)
    root = rf'D:\Code\Spider\ZhiHu_Spider\{mode}'  # Markdown HTML
    if not os.path.exists(root):
        os.mkdir(root)

    sql = SQL()
    # sql.execute('use zhihu_v1;')
    answer_data = sql.fetchall("SELECT "
                               "answer.uid, answer.author_id, answer.url, answer.content,"
                               "question.uid, question.title,"
                               "user.name, user.url_token "
                               "FROM answer "
                               "JOIN question ON  answer.question_id=question.uid "
                               "JOIN user ON  answer.author_id=user.uid;")

    for i in answer_data:
        # 数据
        answer_uid, author_id, api_url, content, \
        question_uid, question_title, \
        user_name, user_token = i

        answer_url = 'https://www.zhihu.com/answer/' + str(answer_uid)
        question_url = 'https://www.zhihu.com/question/' + str(question_uid)
        author_url = 'https://www.zhihu.com/people/' + str(author_id)
        content = content.replace('noscript', 'p')
        content_html = BeautifulSoup(content, 'html.parser').string
        content_html = content_html.replace('&gt;', '>').replace('&lt;', '<')

        question_title = question_title.replace('?', '？')
        md_title = f'{question_title} - {user_name} - {answer_uid}.{suffix}'  # 文件名
        if md_title.replace('\n', '') in os.listdir(root):
            continue

        output.append(str(md_title))
        print(md_title)

        file_path = os.path.join(root, md_title)  # 文件路径

        def create_md():
            # content_md = convert(content_html)  # TODO 目前找不到合适的库

            item_text = f'- [{md_title}]({answer_url})\n'  # 文件在目录中命名
            # 追加到目录
            with open(os.path.join(root, '0A目录.md'), 'a', encoding='utf8') as f_contents:
                f_contents.write(item_text)

            # 单个回答
            """
            格式
            ---
            - [回答链接](回答链接)
            - [问题](问题链接)
            - [作者名](作者链接)
            ---
            content_text_md
            """
            with open(file_path, 'w', encoding='utf8') as f_answer:
                text = f"""QJH\n
- [来源：{answer_url}]({answer_url})
- [问题：{question_title}]({question_url})
- [作者：{user_name}]({author_url})\n
---\n
{content_html}"""
                f_answer.write(text)

        def create_html():
            html_head = """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
        """
            item_text = f'<A HREF="{md_title}" >{md_title}</A><br>'  # 文件在目录中命名
            # <A HREF="{md_title}" >{md_title}</A>
            # 追加到目录
            content_file_path = os.path.join(root, '0A目录.html')
            if not os.path.exists(content_file_path):
                item_text = html_head + item_text
            with open(content_file_path, 'a', encoding='utf8') as f_contents:
                f_contents.write(item_text)

            # 单个回答
            """
            格式
            ---
            - [回答链接](回答链接)
            - [问题](问题链接)
            - [作者名](作者链接)
            ---
            content_text_md
            """
            with open(file_path, 'w', encoding='utf8') as f_answer:
                text = html_head
                text += f"""<A HREF="{answer_url}" >来源：{answer_url}</A><br>
                    <A HREF="{question_url}" >问题：{question_title}</A><br>
                    <A HREF="{author_url}" >作者：{user_name}</A><br>
                    <p>------------------------------------------</p><br>
                    {content_html}"""
                f_answer.write(text)

        if mode == 'Markdown':
            create_md()
        else:
            create_html()
        # break


if __name__ == '__main__':
    create_file([])
