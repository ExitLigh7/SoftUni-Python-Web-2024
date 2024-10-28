
from django.views.generic import TemplateView, ListView
from Exam_27_10.posts.models import Post


class IndexPage(TemplateView):
    template_name = 'common/index.html'


class DashboardPage(ListView):
    model = Post
    template_name = 'common/dashboard.html'