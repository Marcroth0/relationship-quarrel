from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import View, TemplateView
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect

from quarrelapp.models import Post

from .forms import UserDeactivateForm, UserDeleteForm


@login_required
def profile(request, pk=None):
    """ """
    if pk:
        post_creator = get_object_or_404(User, pk=pk)
        user_posts = Post.objects.filter(user=request.user)

    else:
        post_creator = request.user
        user_posts = Post.objects.filter(user=request.user)
    return render(
        request,
        "profile.html",
        {"post_creator": post_creator, "user_posts": user_posts},
    )


class UserDeactivateView(LoginRequiredMixin, View):
    """
    Deactivates currently signed-in user by setting is_active to False.
    """

    def get(self, request, *args, **kwargs):
        form = UserDeactivateForm()
        return render(request, "deactivate_user.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = UserDeactivateForm(request.POST)
        # Form will be valid if checkbox is checked.
        if form.is_valid():
            # Make user inactive and save to database.
            request.user.is_active = False
            request.user.save()
            # Log user out.
            logout(request)
            # Give them a success message.
            messages.success(request, "Account successfully deactivated")
            # Redirect to home page.
            return redirect(reverse("home"))
        return render(request, "deactivate_user.html", {"form": form})


class UserDeleteView(LoginRequiredMixin, View):
    """
    Deletes currently signed-in user and all data.
    """

    def get(self, request, *args, **kwargs):
        form = UserDeleteForm()
        return render(request, "delete_user.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = UserDeleteForm(request.POST)
        # Form will be valid if checkbox is checked.
        if form.is_valid():
            user = request.user
            # Logout before we delete. This will make request.user
            # unavailable (or actually, it points to AnonymousUser).
            logout(request)
            # Delete user (and any associated ForeignKeys, according to
            # on_delete parameters).
            user.delete()
            messages.success(request, "Account successfully deleted")
            return redirect(reverse("home"))
        return render(request, "delete_user.html", {"form": form})


@login_required
class PostDeleteView(DeleteView):
    def delete_post(request, slug=None):
        post_to_delete = Post.objects.get(slug=slug)
        post_to_delete.delete()
        return HttpResponseRedirect(reverse("profile"))


class About(TemplateView):
    """About us page"""
    template_name = 'about.html'

    def about(self, request):
        return render(request, 'about.html')
