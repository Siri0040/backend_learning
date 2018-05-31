from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///FbPosts.sqlite3'

db = SQLAlchemy(app)


class FbPosts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    user_post = db.Column(db.String(200))


@app.route('/')
def show_all():
    all_posts = FbPosts.query.all()
    all_posts_dict = {}
    for each in all_posts:
        all_posts_dict.update({each.username:each.user_post})
    return jsonify(all_posts_dict)


@app.route('/updating_post', methods=['POST'])
def updating_post():
    if request.method == 'POST':
        post_details = \
            FbPosts.query.filter_by(username=request.form['name']).first()
        post_details.user_post =request.form['updated_post']
        db.session.commit()
        updated_dict = {request.form['name']: post_details.user_post}
        return jsonify(updated_dict)



@app.route('/get_post', methods=['POST'])
def get_post():
    if request.method == 'POST':
        user_post_data = FbPosts.query.filter_by(username=request.form['name']).first()
        posts_dict = {}
        posts_dict.update({request.form['name']: user_post_data.user_post})
        return jsonify(posts_dict)


@app.route('/insert_post', methods=['POST'])
def insert_post():
    if request.method == 'POST':
        post_details = FbPosts(username=request.form['name'],
                               user_post=request.form['user_post'])

        db.session.add(post_details)
        db.session.commit()
        return "Record Inserted\n"


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
