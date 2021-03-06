# coding=utf-8
from __future__ import absolute_import
from flask.views import MethodView
from flask.blueprints import Blueprint

from firefly.models.topic import Category, Post
from firefly.libs.template import render_template


bp = Blueprint("category", __name__, url_prefix="/category")


class CategoryView(MethodView):

    def get(self, slug):
        category = Category.objects.get_or_404(_slug=slug)
        posts = Post.objects.filter(
            category=category
        ).order_by("-recent_activity_time")
        return render_template('categories/detail.html',
                               category=category.name,
                               posts=posts)

bp.add_url_rule('/<slug>/', view_func=CategoryView.as_view('detail'))
