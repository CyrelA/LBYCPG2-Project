from django.views.generic import ListView,DetailView
from .models import *
from taggit.models import Tag
from django.views import generic
# Create your views here.

class TagMixin(object):
          def get_context_data(self, **kwargs):
              context = super(TagMixin, self).get_context_data(**kwargs)
              context['tags'] = Tag.objects.all()
              return context

class PostDetail(generic.DetailView):
    model = Vtuber
    template_name = 'info.html'

class PostView(TagMixin,ListView):
    model = Vtuber
    template_name = 'Vtubes.html'
    queryset=Vtuber.objects.all()
    context_object_name = 'vt'

class TagView(TagMixin,ListView):
    model = Vtuber
    template_name = 'Vtubes.html'
    context_object_name = 'vt'

    def get_queryset(self):
        return Vtuber.objects.filter(tags__slug=self.kwargs.get('tag_slug'))

