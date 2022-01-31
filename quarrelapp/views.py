from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import generic, View
from django.contrib.auth.models import User
from .models import Post, CommentPost
from .forms import CommentForm, PostForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by("-date_published")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.order_by('date_published')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

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
