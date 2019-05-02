from django.shortcuts import render
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# LoginRequiredMixin it needs when someone post without login so it will redirect to the login page
#UserPassesTestMixin used for that only the person who created their post only he can edit
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post


#function based views
# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request,'blog/home.html',context)



# class based views so we have to create a class for home
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = "posts"
    ordering = ['-date_posted']

#Detail View for particular post detail
class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    #here form is checking for validation that user is current login user its actually ovverride the form
    def form_valid(self,form):
        form.instance.author  = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    #here form is checking for validation that user is current login user its actually ovverride the form
    def form_valid(self,form):
        form.instance.author  = self.request.user
        return super().form_valid(form)

    #function prevent for update other people posts
    def test_func(self):
        post = self.get_object()  #gives the post which i  am trying to ipdate
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()  #gives the post which i  am trying to ipdate
        if self.request.user == post.author:
            return True
        return False




def about(request):
    return render(request,'blog/about.html',{'title':'About'})




# <app>/model _<viewtype>.html for class based view looking for always
