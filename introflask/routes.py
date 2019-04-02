from flask import render_template, url_for, flash, redirect, request
from introflask import app, bcrypt
from introflask.forms import RegistrationForm, LoginForm, UpdateAccountForm
from introflask.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import MetaData, create_engine, inspect
from sqlalchemy.engine import reflection
from introflask.metadata import meta




posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/database")
def database():
    # db_uri = 'sqlite:///chinook.db'
    # engine = create_engine(db_uri)
    # metadata = MetaData()
    # # metadata.create_all(engine)
    # metadata = MetaData(bind=engine)
    # inspector = inspect(engine)

    # insp = reflection.Inspector.from_engine(engine)
    #
    # # insp =(str(metadata.tables))
    # #
    # # # # reflect db schema to MetaData
    # # metadata.reflect(bind=engine)
    # # tablenames = (metadata.tables)
    # #
    # # Create MetaData instance
    # #metadata = MetaData(engine, reflect=True)
    # for table in metadata.tables.values():
    #     print(table.name)
    # # for column in table.c:
    # #     print(column.name)
    #
    # meta = (metadata.sorted_tables)
    # keys = []
    #
    # metas = insp.get_table_names()
    #
    # if metas:
    #     empty = "full"
    # else:
    #     empty = "empty"

    print(isinstance(meta, str))


    #
    # query = (Album.query.all())
    # # # Get Table
    # # album = (Artists.query.all)
    #
    return render_template('database.html',
    title='Database',
    # query=query,
    meta=meta,
    # metas=metas,
    # isit=empty,
    # keys=keys)
    )


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('your account has been updated', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form= form)
