import httpx
from tools import get_answer_id as get_answer_from_url
from database import SQL, Answer, User, Question
import time


def answer2db(text, output):
    output.append('-' * 15 + 'Answer' + '-' * 15)
    answer = get_answer_from_url(text)
    output.append(str(answer))

    sql = SQL()

    url = 'https://api.zhihu.com/answers/'

    answer_list = []
    user_list = []
    question_list = []
    for i in answer:
        answer_url = url + str(i) + '?include=created_time,updated_time,voteup_count,favlists_count,comment_count,content,is_labeled,author.badge_v2'
        output.append(str(f'<a href="{answer_url}"><span style=" text-decoration: underline; color:#0000ff;">{answer_url}</span></a>'))
        resp = httpx.get(url=answer_url)
        data = resp.json()
        answer_list.append(data)
        user_list.append(data.get('author'))
        question_list.append(data.get('question'))
        time.sleep(0.1)

    if answer_list:
        sql.insert_into('answer', Answer, answer_list)
        pass
    if user_list:
        sql.insert_into('user', User, user_list)
        pass
    if question_list:
        sql.insert_into('question', Question, question_list)
        pass
