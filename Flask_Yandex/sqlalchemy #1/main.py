import time

from flask import Flask, render_template, url_for
from data import db_session
from datetime import datetime, timedelta
from data.users import User
from data.jobs import Jobs


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index1():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()

    # job = Jobs()
    # job.team_leader = 1
    # job.job = 'deployment of residential modules 1 and 2'
    # job.work_size = 15
    # job.collaborators = '2, 3'
    # job.is_finished = False
    # job.start_date = datetime.now()
    # job.end_date = datetime.now() + timedelta(hours=5)
    # db_sess.add(job)
    #
    # job = Jobs()
    # job.team_leader = 1
    # job.job = 'deployment of residential modules 1'
    # job.work_size = 19
    # job.collaborators = '2, 5'
    # job.is_finished = False
    # job.start_date = datetime.now()
    # job.end_date = datetime.now() + timedelta(hours=5)
    # db_sess.add(job)
    #
    # job = Jobs()
    # job.team_leader = 1
    # job.job = 'deployment of residential modules 2'
    # job.work_size = 18
    # job.collaborators = '2, 1'
    # job.is_finished = False
    # job.start_date = datetime.now()
    # job.end_date = datetime.now() + timedelta(hours=5)
    # db_sess.add(job)
    # db_sess.commit()

    work_list = [work for work in db_sess.query(Jobs).all()]
    for i, wr in enumerate(work_list):
        try:
            id1 = wr.team_leader
            work_list[i].duration = str(wr.end_date - wr.start_date).split(':')[0]
            work_list[i].team_leader_name = db_sess.query(User).filter(User.id == 1).first().name
            work_list[i].team_leader_surname = db_sess.query(User).filter(User.id == 1).first().surname
        except Exception as e:
            print('error', type(e).__name__)
    return render_template(
        'index.html',
        title='Домашняя страница',
        head1='Миссия Колонизация Марса',
        head2='И на Марсе будут яблони цвести!',
        head3='Works log',
        works=work_list
    )


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

