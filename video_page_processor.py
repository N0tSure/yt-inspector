from bs4 import BeautifulSoup
from datetime import datetime

report_file_name = '/data/report.csv'


def save_report(count, likes, dislikes):
    report_file = open(report_file_name, 'a')
    now = datetime.today()
    row = '{:%Y-%m-%d %H:%M:%S},{},{},{}\n'.format(now, count, likes, dislikes)
    report_file.write(row)
    print(row, end='')
    report_file.close()


def process_node(html_doc):

    # getting all page
    root = BeautifulSoup(html_doc, 'html.parser')

    # get watch counter node
    count = root.find('div', class_='watch-view-count')
    raw = count.get_text().replace(u'\xa0', u'')
    views_count = raw.split(' ')[0]

    # get like counter node
    like_bt = root.find('button', class_='like-button-renderer-like-button')
    likes_count = like_bt.get_text().replace(u'\xa0', u'')

    # get dislike counter node
    dislike_bt = root.find('button', class_='like-button-renderer-dislike-button')
    dislikes_count = dislike_bt.get_text().replace(u'\xa0', u'')

    save_report(views_count, likes_count, dislikes_count)
