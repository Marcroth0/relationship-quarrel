from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import generic, View
from django.conf import settings
from django.contrib.auth.models import User
from .models import Post, CommentPost, Comment
from .forms import CommentForm, PostForm
from django.core.paginator import Paginator


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by("-date_published")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.order_by('date_published')
        liked_one = False
        liked_two = False
        if post.content_one.likes.filter(id=self.request.user.id).exists():
            liked_one = True
        if post.content_two.likes.filter(id=self.request.user.id).exists():
            liked_two = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked_one": liked_one,
                "liked_two": liked_two,
                "comment_form": CommentForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.order_by('date_published')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            # comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )

    def delete_own_comment(request, id=None):
        comment = get_object_or_404(Comment, id=id)
        if comment.name == request.user.username and request.user.is_authenticated:
            comment.delete()
            messages.add_message(
                request, messages.SUCCESS,
                f"Congratulations, your tracks are hidden"
            )
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            # return HttpResponseRedirect(reverse(''))
        else:
            messages.add_message(
                request, messages.ERROR,
                f"An error occurred"
            )


class UserPost(View):
    def get(self, request):
        form = PostForm(request.GET or None)
        if request.user.is_authenticated:
            return render(request, "user_post.html",
                          {
                              "form": form,
                              "post_form": PostForm()
                          }
                          )
        else:
            messages.add_message(
                request, messages.ERROR,
                f"You need to login first, silly."
            )
            return HttpResponseRedirect('/accounts/login')

    def post(self, request):
        form = PostForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                post = form.save(commit=False)
                c_one = request.POST["content_one"]
                c_two = request.POST["content_two"]

                post.content_one = CommentPost.objects.create(
                    content=c_one)
                post.content_two = CommentPost.objects.create(
                    content=c_two)
                post.user = request.user

                post.save()
            return HttpResponseRedirect('/')
        context = {'form': form,
                   }


class PostLike(View):
    def post(self, request, slug, id):
        post = get_object_or_404(Post, slug=slug)

        if post.content_one.id == id:
            if post.content_one.likes.filter(id=request.user.id).exists():
                post.content_one.likes.remove(request.user)
            else:
                post.content_one.likes.add(request.user)
            if post.content_two.likes.filter(id=request.user.id).exists():
                post.content_two.likes.remove(request.user)

        if post.content_two.id == id:
            if post.content_two.likes.filter(id=request.user.id).exists():
                post.content_two.likes.remove(request.user)
            else:
                post.content_two.likes.add(request.user)
            if post.content_one.likes.filter(id=request.user.id).exists():
                post.content_one.likes.remove(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostEdit(View):
    def edit_post(request, slug):
        post = Post.objects.get(slug=slug)
        if request.method != 'POST':
            form = PostForm(instance=post)
        else:
            form = PostForm(instance=post, data=request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                c_one = request.POST["content_one"]
                c_two = request.POST["content_two"]

                CommentPost.objects.filter(
                    id=post.content_one.id).update(content=c_one)
                CommentPost.objects.filter(
                    id=post.content_two.id).update(content=c_two)
                form.save()
                return HttpResponseRedirect(reverse('profile'))

        context = {'post': post, 'form': form}
        return render(request, 'edit_post.html', context)
