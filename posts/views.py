from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import RegisterForm, PostForm


# Register View (Function-Based)
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   # auto login after register
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


# Home Feed (Class-Based View)
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-created_at']   # latest first


# Upload Photo (Only logged-in users)
class UploadView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'upload.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
# register()

# 👉 Creates new user
# 👉 Automatically logs user in after register

# HomeView

# 👉 Shows all posts
# 👉 Latest photos first

# UploadView

# 👉 Only logged-in users can upload
# 👉 Automatically attaches logged-in user to post