from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator

from .models import Post, Category
from .forms import CommentForm


def post_list(request):
    # строка поиска из GET-параметра ?q=
    query = request.GET.get('q')

    # базовый queryset: только опубликованные посты
    posts_qs = Post.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('-published_date')

    # ПОИСК ПО КОРНЮ СЛОВА
    if query:
        q = query.lower().strip()
        root = q

        # если запрос длиннее 5 символов — режем один символ с конца
        if len(q) > 5:
            root = q[:-1]

        filtered = []
        for p in posts_qs:
            title_l = (p.title or "").lower()
            content_l = (p.content or "").lower()
            if root in title_l or root in content_l:
                filtered.append(p)

        posts_qs = filtered

    # пагинация: по 5 постов на страницу
    paginator = Paginator(posts_qs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,      # цикл for post in posts
        'page_obj': page_obj,   # навигация по страницам
        'query': query,         # чтобы в инпуте поиска сохранялся текст
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(approved=True)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            form = CommentForm() 
    else:
        form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog/post_detail.html', context)


def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(
        category=category,
        published_date__lte=timezone.now()
    ).order_by('-published_date')

    return render(
        request,
        'blog/category_posts.html',
        {'category': category, 'posts': posts}
    )
