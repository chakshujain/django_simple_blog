from django.shortcuts import render,get_object_or_404,redirect
from posts.forms import PostModelForm
from django.contrib import messages

from posts.models import Post,Author

# Create your views here.

def post_list_view(request):
    posts = Post.objects.all()
    context = {
    'posts' : posts
    }
    messages.info(request, 'Here are all the current blog posts')
    return render(request,"posts/post_list.html",context)

def post_detail_view(request,slug):
    unique_post = get_object_or_404(Post,slug = slug)
    context = {
    'post' : unique_post
    }
    messages.info(request, 'This is the specific detail view')
    return render(request,"posts/post_detail.html",context)

def post_create_view(request):
    author,created = Author.objects.get_or_create(
                                    user = request.user,
                                    email = request.user.email,
                                    phone_no = 9896165054
    )
    form = PostModelForm(request.POST or None,
                        request.FILES or None  )
    context = {
    'form' : form
    }
    if form.is_valid():
        form.instance.author = author
        form.save()
        return redirect('/')
    messages.info(request, 'Successfully created a new blog post!')
    return render(request,"posts/post_create.html",context)


def post_update_view(request,slug):
    unique_post = get_object_or_404(Post,slug = slug,)
    form = PostModelForm(request.POST or None,
                        request.FILES or None,
                        instance = unique_post)

    context = {
    'form' : form
    }
    if form.is_valid():
        form.save()
        messages.info(request, 'Successfully updated your blog post.')
        return redirect('/')
    return render(request,"posts/post_create.html",context)


def post_delete_view(request,slug):
    unique_post = get_object_or_404(Post,slug = slug)
    unique_post.delete()
    messages.info(request, 'Successfully deleted your blog post.')
    return redirect('/')
