from datetime import datetime as dt
import bleach
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
# from sqlalchemy import desc
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField

# Templates are here
# sidorkinandrew.github.io/100-days-of-python/day_067_RESTful_blog

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    # num_date = db.Column(db.Date, nullable=True)


# db.create_all()


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    # Notice body's StringField changed to CKEditorField
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


##RENDER HOME PAGE USING DB
@app.route('/')
def get_all_posts():
    allposts = BlogPost.query.all()
    # for x in allposts:
    #     # patch posts already saved posts
    #     # that have a differently formatted timestamp
    #     x.num_date = dt.strptime(x.date, '%B %d, %Y')
    #     db.session.commit()
    # posts = BlogPost.query.order_by(desc(BlogPost.num_date)).all()
    # return render_template("index.html", all_posts=posts)
    return render_template("index.html", all_posts=allposts)


##RENDER POST USING DB
@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    return render_template("post.html", post=requested_post)


# @app.route("/edit/<int:post_id>", methods=["GET", "POST"])
# def edit_post(post_id):
#     return redirect(url_for('show_post', post_id=post_id))

@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    # edit_form = CreatePostForm(obj=post)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=strip_invalid_html(post.body.data)
    )
    return render_template("make-post.html", form=edit_form, is_edit=True)


## strips invalid tags/attributes
def strip_invalid_html(content):
    allowed_tags = ['a', 'abbr', 'acronym', 'address', 'b', 'br', 'div', 'dl', 'dt',
                    'em', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'i', 'img',
                    'li', 'ol', 'p', 'pre', 'q', 's', 'small', 'strike',
                    'span', 'sub', 'sup', 'table', 'tbody', 'td', 'tfoot', 'th',
                    'thead', 'tr', 'tt', 'u', 'ul']

    allowed_attrs = {
        'a': ['href', 'target', 'title'],
        'img': ['src', 'alt', 'width', 'height'],
    }

    cleaned = bleach.clean(content,
                           tags=allowed_tags,
                           attributes=allowed_attrs,
                           strip=True)

    return cleaned


@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            ## use strip_invalid_html-function before saving body
            body=strip_invalid_html(form.body.data),
            img_url=form.img_url.data,
            author=form.author.data,
            date=dt.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
