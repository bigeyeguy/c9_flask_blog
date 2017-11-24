from flask_app import app, db, login_manager, User
from flask import render_template, request, url_for, redirect
from flask_login import login_user, , login_required, logout_user
from project.form import LoginForm, PostForm
from project.models import Post


POSTS_PER_PAGE = 5

@app.route('/', methods = ["GET", "POST"])
@app.route('/index', methods = ["GET", "POST"])
@app.route('/index/<int:page>', methods = ["GET", "POST"])
def index(page=1):
    posts = Post.query.filter_by(live=True).order_by(Post.posted.desc()).paginate(page,3,False).items
    return render_template('main_page2.html', posts=posts)


@app.route('/login', methods = ["GET", "POST"])
def login():
    form = LoginForm()
    error = "Wrong username or password"

    if request.method == "GET":
        return render_template("login.html", form=form)

    user = load_user(request.form["username"])
    if user is None:
        return render_template("login.html", form=form, error=error)

    if not user.check_password(request.form["password"]):
        return render_template("login.html", form=form, error=error)

    login_user(user)
    return redirect(url_for('index'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(username=user_id).first()

@app.route('/logout', methods = ["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/post', methods = ["GET", "POST"])
@login_required
def post():
    form = PostForm()
    if request.method == "GET":
        return render_template('post.html', form=form)

    post = Post(title = request.form["title"], body = request.form["body"])
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/article', methods=('GET', 'POST'))
@app.route('/article/<slug>', methods=('GET', 'POST'))
def article(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()
    return render_template('article.html', post=post)

@app.route('/about')
def about():
    return render_template('about.html')








