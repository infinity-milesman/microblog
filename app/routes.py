from flask import render_template, flash, url_for
from werkzeug.utils import redirect

from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
	user = {'username':'Amit'}
	posts = [
		{
			'author':{'user_name':'amit'},
			'body':'beautiful day in portland.'
		},
		{
			'author':{'user_name':'shraddz'},
			'body':'The avengers movie was so cool.'
		}
	]
	return render_template('index.html',user=user,title='Home',posts=posts)
	# return 'Hello, World!.'

@app.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {} ,remember me={}'.format(form.username.data,form.remember_me.data))
		return redirect(url_for('index'))
	return render_template("login.html",form=form,title='Sign In')
