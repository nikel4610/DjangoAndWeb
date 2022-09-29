from django.views.generic import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth.mixins import AccessMixin

from django.shortcuts import render
import requests
import json

class HomeView(TemplateView):
    template_name = 'home.html'

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

class OwnerOnlyMixin(AccessMixin):
    raise_exception = True # False로 바꾸면 로그인 페이지로 이동
    permission_denied_message = "Owner only can update/delete the object"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

def SpaceAPI_FV(request):   
    query = request.GET.get('q')
    if query:
        search_response = requests.get("https://images-api.nasa.gov/search?q="+query+'&media_type=image')
    else:
        search_response = requests.get("https://images-api.nasa.gov/search?q=earth&media_type=image")
    loaded_json = json.loads(search_response.text)
    collection = loaded_json.get('collection')
    items = collection.get('items')
    
    images=[]
    descriptions=[]
    titles=[]

    for i in items:
        images.append(i.get('links')[0].get('href'))
        titles.append(i.get('data')[0].get('title'))

    images=list(zip(images,titles))

    context = {
                'search_term' : query,
                'object_list' : images
                }
    return render(request, "images.html", context)
    