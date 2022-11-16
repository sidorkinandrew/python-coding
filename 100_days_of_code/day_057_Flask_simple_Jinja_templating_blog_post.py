from flask import Flask, render_template
import requests


class Post:
    def __init__(self, post_id, title, subtitle, body):
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body


posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)


@app.route('/guess/<name>')
def guess(name):
    gender = requests.get(f'https://api.genderize.io?name={name}').json()['gender']
    age = requests.get(f'https://api.agify.io?name={name}').json()['age']
    return render_template("guess.html", person_name=name, gender=gender, age=age)


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    all_posts = requests.get(blog_url).json()
    return render_template('blog.html', posts=all_posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)


"""

### guess.html


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Guess</title>
</head>
<body>
    <h1>Hey {{ person_name.title() }}</h1>
    <h2>I think you are {{ gender }}</h2>
    <h3>And maybe {{ age }} years old</h3>
</body>
</html>

"""





"""

### blog.html


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Blog</title>
</head>
<body>
    {% for blog_post in posts: %}
        {% if blog_post["id"] == 2: %}
        <h1>{{ blog_post["title"] }}</h1>
        <h2>{{ blog_post["subtitle"] }}</h2>
        {% endif %}
    {% endfor %}
</body>
</html>
"""


"""

### index.html


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link href="https://fonts.googleapis.com/css2?family=Raleway" rel="stylesheet">
    <link rel="stylesheet" href="../static/css/styles.css">
</head>
<body>
<div class="wrapper">
    <div class="top">
        <div class="title"><h1>My Blog</h1></div>
    </div>

    {% for post in all_posts: %}
    <div class="content">
        <div class="card ">
            <h2>{{ post.title }}</h2>
            <p>{{ post.subtitle }}</p>
            <a href="{{ url_for('show_post', index=post.id) }}">Read</a>
        </div>

    </div>
    {% endfor %}

</div>
</body>
<footer>
    <p>Made with ♥️ in London.</p>
</footer>
</html>

"""

"""


### post.html

 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="../static/css/styles.css">
</head>
<body>
<div class="wrapper">
    <div class="top">
        <div class="title"><h1>My Blog</h1></div>
    </div>
    <div class="content">
        <div class="card">
            <h1> {{ post.title }}</h1>
            <h2> {{ post.subtitle }}</h2>
            <p> {{ post.body }}</p>
        </div>
    </div>
</div>
</body>
<footer>
    <p>Made with ♥️ in London.</p>
</footer>
</html>

"""

"""

### style.css

body{
 background: #efeff3;
 margin: 0;
 font-family: 'Raleway', sans-serif;
 -webkit-font-smoothing: antialiased;
  color:#212121;
}
.wrapper{
  position: relative;
  clear:both;
  margin: 0 auto 75px auto;
  width: 100%;
  overflow: hidden;
}
.top{
  background: #4e89ae;
  height: 180px;
  border-top: 20px solid #43658b;
}

.top .title {
  width: 700px;
  margin: 38px auto 0 auto; 
}

.title h1 {
  font-size:24px;
  color:#FFF;
  font-weight:500;
}

.content{
    margin: -80px auto 100px;
  padding-bottom: 20px;
}

.card{
  position: relative;
  background: #fff;
  padding:50px;
  width: 600px;
  margin: 20px auto 0 auto;
  box-shadow: 0 2px 4px rgba(100,100,100,.1);
}

.card h2 {
  font-size:21px;
  font-weight:500;
}

.card h2 a {
  color:#CC0000;
  text-decoration:none;
}

.card .text {
  color:#212121;
  margin-top:20px;
  font-size:15px;
  line-height:22px;
}

footer {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  background-color: #43658b;
  color: white;
  text-align: center;
}

"""
