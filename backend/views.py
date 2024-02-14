from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


from .models import Post

def index(request):
    return render(request, "home.html")

def home(request):
    s = "All Posts: \r\n\r\n\r\n"
    for post in Post.objects.order_by('-created_at'):
        s += post.title + '\r\n'
    return HttpResponse(s, content_type="text/plain; charset=utf-8")


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["posts"] = Post.objects.all()
    #     context["post"] = Post.objects.get(id=self.kwargs["pk"])

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'  # Имя, которое будет использоваться в шаблоне для доступа к списку постов

    def get_queryset(self):
        # Переопределяем метод get_queryset для изменения набора записей, которые будут возвращены
        # По умолчанию Django вернет все записи, отсортированные по полю 'created_at' в порядке убывания
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        # Переопределяем метод get_context_data для добавления дополнительных данных в контекст
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        context['post'] = self.get_queryset().get(pk=self.kwargs.get('pk'))
        # Добавляем дополнительные данные в контекст, если это необходимо
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        return get_object_or_404(Post, pk=self.kwargs.get('pk'))
