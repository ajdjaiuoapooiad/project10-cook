from django.views import generic
from django.urls import reverse_lazy
from .forms import PostCreateForm
from .models import Post

class IndexView(generic.ListView):
    model=Post
    
class CreateView(generic.CreateView):
    model=Post
    form_class=PostCreateForm
    success_url=reverse_lazy('cook:index')
    
class DetailView(generic.DetailView):
    model=Post