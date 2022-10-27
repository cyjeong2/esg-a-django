from django.shortcuts import render, redirect
from .models import Restaurant

def index(request):
    posts = Restaurant.objects.all().order_by('-pk')
    
    
    return render(
        request,
        'Restaurant/index.html',
        {
            'posts' : posts,
        }
    )

def single_post_page(request, pk) :
    post = Restaurant.objects.get(pk=pk)
    
    return render(
        request,
        'Restaurant/single_post_page.html',
        {
            'post' : post,
        }
    )

from django.views.generic import CreateView
from Restaurant.forms import RestaurantForm

def restaurant_new(request):
    # print("request.method =", request.method)
    # print("request.POST =", request.POST)
    if request.method == "GET" :
        form = RestaurantForm()
    else :
        form = RestaurantForm(request.POST)
        if form.is_valid() :
            #유효성 검사에 통과한 값들이 저장된 dict
            # form.cleaned_data
            post = form.save() # ModelForm에서 지원
            # return redirect(f"/blog/{post.pk}/")
            # return redirect(post.get_absolute_url())
            return redirect(post)
        
    return render(request, "Restaurant/Restaurant_form.html", {
        "form" : form,
    })