from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {
        'nickname': 'Grace'
    }

    posts = [
        {
            'author': {'nickname': 'JYP'},
            'date': '1/2/2015',
            'title': 'Who am i?',
            'body': 'i am chijil-jengi'
        },
        {
            'author': {'nickname': 'stewart'},
            'date': '1/3/2015',
            'title': 'What do?',
            'body': 'im gonna teabag u'
        }
    ]

    return render_template('index.html', user=user,posts=posts)
