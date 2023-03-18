import httpx
from tools import get_answer_id
from database import SQL, Answer, User, Question
import time
from tqdm import tqdm

f = open(r'D:\Code\Spider\ZhiHu_Spider-master\test\favorites_2023_3_13.html', 'r', encoding='utf8')
text = f.read()
f.close()


answer = get_answer_id(text)
print(answer)

sql = SQL()

url = 'https://api.zhihu.com/answers/'

answer_list = []
user_list = []
question_list = []
for i in answer:
    answer_url = url + i + '?include=created_time,updated_time,voteup_count,favlists_count,comment_count,content,is_labeled,author.badge_v2'
    print(answer_url)
    resp = httpx.get(url=answer_url)
    data = resp.json()
    answer_list.append(data)
    user_list.append(data.get('author'))
    question_list.append(data.get('question'))

if answer_list:
    sql.insert_into('answer', Answer, answer_list)
    pass
if user_list:
    sql.insert_into('user', User, user_list)
    pass
if question_list:
    sql.insert_into('question', Question, question_list)
    pass

print('over!')