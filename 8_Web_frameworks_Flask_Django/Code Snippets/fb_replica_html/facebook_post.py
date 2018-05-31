from flask import Flask, request, flash, url_for, redirect, render_template
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
    return render_template('show_all.html', user_posts=FbPosts.query.all())


@app.route('/update_post', methods=['POST'])
def update_post():
    if request.method == 'POST':
        if not request.form['name']:
    		flash('Please enter username', 'error')
    	else:
    		return render_template('update_post.html', user_posts=FbPosts.query.filter_by(username=request.form['name']))
    return render_template('update_post.html')

@app.route('/updating_post', methods=['GET', 'POST'])
def updating_post():
	if request.method == 'POST';
		post_details = FbPosts.query.filter_by(username=request.form['name']).first()
		post_details.user_post = request.form['updated_post']
		db.session.commit()
		flash('Record was successfully updated')
		return redirect((url_for('show_all')))
	return render_template('update_post.html')



@app.route('/get_post', methods=['POST'])
def get_post():
    if request.method == 'POST':
    	if not request.form['name']:
    		flash('Please enter username', 'error')
    	else:
		    return render_template('get_post.html', user_posts=FbPosts.query.filter_by(username=request.form['name']))
	return render_template('get_post.html')


@app.route('/insert_post', methods=['GET', 'POST'])
def insert_post():
    if request.method == 'POST':
    	if not request.form['name']:
    		flash('Please enter username', 'error')
    	else:
        	post_details = FbPosts(username=request.form['name'], user_post=request.form['user_post'])
        	db.session.add(post_details)
        	db.session.commit()
        	flash('Record was successfully added')
        	return redirect(url_for('show_all'))
    return render_template('insert_post.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
