from database import SQL

root = './Markdown/'

sql = SQL()
answer_data = sql.fetchall("SELECT answer.uid,answer.author_id,answer.url,answer.content_text,question.title "
                           "FROM answer LEFT JOIN question ON  answer.question_id=question.uid")
header = ['uid', 'author_id', 'url', 'content_text', 'question_title']
print(header)
item = {'question': None, 'author': None, 'answer_url': None}
for i in answer_data:
    # 数据
    api_id, author_id, api_url, content_text, question_title = i  # TODO： 用户昵称
    author_url = 'https://www.zhihu.com/people/' + str(author_id)
    url = 'https://www.zhihu.com/answer/' + str(api_id)
    md_title = f'{question_title} - {api_id}.md'  # TODO：用户昵称
    # print(i)

    # 追加到目录
    with open(root + '目录.md', 'a', encoding='utf8') as f_contents:
        item_text = f'- [{md_title}]({url})\n'
        # item_text += f'- [{md_title}](./{md_title}.md)\n'
        f_contents.write(item_text)

    # # 单个回答
    # with open(root + md_title, 'w', encoding='utf8') as f_answer:
    #     """
    #     格式
    #     # 问题
    #     ---
    #     - [回答链接](回答链接)
    #     - [问题](问题链接)
    #     - [作者名](作者链接)
    #     ---
    #     content_text
    #     """
    #     text = f"""# {question_title}\n---\n- [{md_title}]({url})\n---\n"""
    #     f_answer.write(text)



    # break

# 在台湾，大概多少比例的台湾人对大陆人有善意？ - 黃仁勳的回答 - 知乎
# https://www.zhihu.com/question/279138438/answer/2936303803
