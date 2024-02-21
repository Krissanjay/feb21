
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse, get_object_or_404

from persons.forms import UpdateUserForm, ChangePasswordForm, MovieForm,CommentForm
from persons.models import Movie, Comment,CartItem


def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid Credentials")
            return redirect('login')


    return render(request,"login.html")
def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('message')
                print("User registered")
                messages.info(request, "User registered")
        else:
            messages.info(request,"password not match")
            return redirect('register')
        # return redirect('/')



    return render(request,"register.html")

def logout(request):
        auth.logout(request)
        return redirect('/')




def index(request):
    return redirect('/')
# def profile(request,user=None):
#     return render(request,'profile.html')
def movie_list(request):
    return render(request,'movie_list.html')
def message(request):
    return render(request,'message.html')

def profile(request):
    context = {

    }
    return render(request, 'profile.html', context)


def update_user(request):
    if request.user.is_authenticated:
        current_user=User.objects.get(id=request.user.id)
        user_form=UpdateUserForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request,"user has been updated")
            return redirect('/')
        return render(request,"update_profile.html",{'user_form':user_form})
    else:
        messages.success(request, "you must be logged in")
        return redirect('/')


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, "Your Password Has Been Updated...Please login")
                return redirect('login')
            else:
                messages.success(request, "Error!!!... Please create correct password.")
                return redirect('update_password')
        else:
            form = ChangePasswordForm(current_user)
            return render(request, "update_password.html", {'form': form})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')

@login_required
def add_movie(request, movie=None):
    if request.method == 'POST':
        form = MovieForm(request.POST or None, request.FILES,instance=movie)
        if form.is_valid():
            movie = form.save()
            movie.manager = request.user
            movie.save()
            return redirect('movie_list')  # Redirect to post list page after post creation
    else:
        form = MovieForm()
    return render(request, 'add.html', {'form': form})
    # form = MovieForm(request.POST or None, request.FILES, instance=movie)
    # if form.is_valid():
    #     form.save()
    #     return redirect('movie_list')
    # return render(request, 'add.html', {'form': form, 'movie': movie})

    # if request.method=="POST":
    #     name=request.POST.get('name',)
    #     desc = request.POST.get('desc', )
    #     release_date = request.POST.get('release_date', )
    #     img = request.FILES['img']
    #     actors = request.POST.get('actors', )
    #     category = request.POST.get('category', )
    #     trailer = request.POST.get('trailer', )
    #     movie=Movie(name=name,desc=desc,release_date=release_date,img=img,actors=actors,category=category,trailer=trailer)
    #     movie.save()
    #     return redirect('movie_list')
    # return render(request,'add.html')
def movie_list(request):
    if request.user.is_authenticated:
        movie=Movie.objects.all()
        context={
            'movie_list':movie

        }
        return render(request,'movie_list.html',context)
    else:
        return redirect('login')

def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'movie':movie})
def delete(request,id):
    movie=Movie.objects.get(id=id)
    if request.method=='POST':
        movie.delete()
        return redirect('movie_list')

    return render(request,'delete.html')
#
# def delete(request, id):
#         movie=Movie.objects.get(pk=id)
#         if request.user == movie.manager:
#             movie.delete()
#             messages.success(request, ("Event Deleted!!"))
#             return redirect('movie_list')
#         else:
#             messages.success(request, ("You Aren't Authorized To Delete This Event!"))
#             return redirect('movie_list')

def add_comment(request, pk):
    movie = Movie.objects.get(id=pk)

    form = CommentForm(instance=movie)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=movie)
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['comment_body']
            c = Comment(movie=movie, commenter_name=name, comment_body=body, date_added=datetime.now())
            c.save()
            return redirect('movie_list')
        else:
            print('form is invalid')
    else:
        form = CommentForm()


    context = {
        'form': form
    }

    return render(request, 'add_comment.html', context)
def delete_comment(request, pk):
    comment = Comment.objects.filter(movie=pk).last()
    movie_id = comment.movie.id
    comment.delete()
    return redirect(reverse('detail', args=[movie_id]))

def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            movies = Movie.objects.filter(category__icontains=query)
            return render(request, 'searchbar.html', {'movies':movies})
        else:
            print("No information to show")
            return render(request, 'searchbar.html', {})

def category(request):
    return render(request, 'category.html')

def thriller(request):
    if request.method == 'GET':
        movies = Movie.objects.filter(category__icontains='thriller')
        return render(request, 'thriller.html', {'movies': movies})

def action(request):
    if request.method == 'GET':
        movies = Movie.objects.filter(category__icontains='action')
        return render(request, 'thriller.html', {'movies': movies})
def drama(request):
    if request.method == 'GET':
        movies = Movie.objects.filter(category__icontains='drama')
        return render(request, 'thriller.html', {'movies': movies})

def adventure(request):
    if request.method == 'GET':
        movies = Movie.objects.filter(category__icontains='adventure')
        return render(request, 'thriller.html', {'movies': movies})
def horror(request):
    if request.method == 'GET':
        movies = Movie.objects.filter(category__icontains='horror')
        return render(request, 'thriller.html', {'movies': movies})
def scifi(request):
    if request.method == 'GET':
        movies = Movie.objects.filter(category__icontains='scifi')
        return render(request, 'thriller.html', {'movies': movies})


def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})


def add_to_cart(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    cart_item, created = CartItem.objects.get_or_create(movie=movie,
                                                        user=request.user)
    cart_item.save()
    return redirect('movie_list')

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')

def detail_item(request,item_id):
    movie = Movie.objects.get(id=item_id)
    return render(request,"detail.html",{'movie':movie})
