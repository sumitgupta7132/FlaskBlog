from flask import render_template, request, Blueprint, url_for
from flaskblog.models import Post


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=10)
    return render_template('home.html', posts=posts, footer="home")


@main.route("/about")
def about():
    image_file = url_for(
        'static', filename='profile_pics/' + 'author.jpeg')
    return render_template('about.html',
                           image_file=image_file, about='about')
