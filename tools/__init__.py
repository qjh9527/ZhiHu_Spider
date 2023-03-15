# @Time : 2023/3/13 22:36

import re

from bs4 import BeautifulSoup


def get_answer_url(text):
    pattern1 = r"(https://www.zhihu.com/answer/\d+)"
    pattern2 = r"(https://www.zhihu.com/)question/\d+/(answer/\d+)"

    answer_numbers1 = re.findall(pattern1, text)
    answer_numbers2 = re.findall(pattern2, text)
    answer_numbers = answer_numbers1 + answer_numbers2
    return answer_numbers


def get_answer_id(text):
    pattern1 = r"https://www.zhihu.com/answer/(\d+)"
    pattern2 = r"https://www.zhihu.com/question/\d+/answer/(\d+)"

    answer_numbers1 = re.findall(pattern1, text)
    answer_numbers2 = re.findall(pattern2, text)
    answer_numbers = answer_numbers1 + answer_numbers2
    return answer_numbers


def get_article_url(text):
    pattern = r"(https://zhuanlan.zhihu.com/p/\d+)\" "

    article_numbers = re.findall(pattern, text)
    return article_numbers


def get_question_url(text):
    pattern = r"(https://www.zhihu.com/question/\d+)\" "

    question_numbers = re.findall(pattern, text)
    return question_numbers


def get_user_url(text):
    pattern1 = r'(https://www.zhihu.com/people/[\w-]+)" '
    pattern2 = r'(https://www.zhihu.com/people/[\w-]+/.+)" ADD_DATE'

    question_numbers1 = re.findall(pattern1, text)
    question_numbers2 = re.findall(pattern2, text)
    return question_numbers1 + question_numbers2


if __name__ == '__main__':
    f = open(r'D:\Code\Spider\ZhiHu_Spider\test\favorites_2023_3_13.html', 'r', encoding='utf8')
    text = f.read()
    f.close()
    result1 = get_answer_url(text)
    result2 = get_article_url(text)
    result3 = get_question_url(text)
    result4 = get_user_url(text)
    # print(len(result1))
    # print(len(result2))
    # print(len(result3))
    # print(len(result4))
    # print(len(result1) + len(result2) + len(result3) + len(result4))
    print('# article\n')
    for i in result2:
        print(f'- [{i}]({i})')

    print('\n# question\n')
    for i in result3:
        print(f'- [{i}]({i})')

    print('\n# user\n')
    for i in result4:
        print(f'- [{i}]({i})')

    # soup = BeautifulSoup(text, "html.parser")
    #
    # # 找到所有带有 href 属性的标签
    # a_tags = soup.find_all("a", href=True)
    #
    # # 输出所有 href 属性的值
    # for a_tag in a_tags:
    #     href = a_tag["href"]
    #     if '.zhihu' in href:
    #         print(href)
