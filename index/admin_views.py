import sendgrid
from sendgrid.helpers.mail import *
from decouple import config
import json

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import HttpResponse

from .forms import MealForm, RecipeForm, IngredientForm, PersonForm
from .models import *

from django.forms import modelformset_factory


@login_required
def new_meal(request):
    ImageFormset = modelformset_factory(Images, fields=('image',), extra=2)
    if request.method == 'POST':
        form = MealForm(request.POST, request.FILES)
        formset = ImageFormset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            meal = form.save(commit=False)
            meal.save()
            form.save_m2m()

            for f in formset:
                try:
                    photo = Images(meal=meal, image=f.cleaned_data['image'])
                    photo.save()


                except Exception as e:
                    break

            admin_name = config('admin')
            admin = User.objects.get(username=admin_name)
            admin_email = config('admin_email')
            send_email(admin.email, 'Jess posted a new meal', 'meal', admin_email)

            # return redirect('meal_detail', id=meal.id)
            return redirect('/')


    else:
        form = MealForm()
        formset = ImageFormset(queryset=Images.objects.none())

    obj = {
        'form': form,
        'formset': formset,
    }

    return render(request, 'form.html', obj)


@login_required
def meal_edit(request, id):
    meal = get_object_or_404(Meal, id=id)

    if request.method == 'POST':
        form = MealForm(request.POST, instance=meal)

        if form.is_valid():
            meal = form.save(commit=False)
            meal.save()

            return redirect('meal_detail', id=meal.id)
    else:
        form = MealForm(instance=meal)

    obj = {
        'form': form
    }

    return render(request, 'form.html', obj)


@login_required
def new_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('new_meal')
    else:
        form = PersonForm()

    obj = {
        'form': form
    }

    return render(request, 'form.html', obj)


@login_required
def new_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            form.save_m2m()
        return redirect('recipe_detail', id=recipe.id)
    else:
        form = RecipeForm()

    obj = {
        'form': form
    }

    return render(request, 'form.html', obj)


@login_required
def new_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.save()
            return redirect('new_ingredient')
    else:
        form = IngredientForm()

    obj = {
        'form': form
    }

    return render(request, 'form.html', obj)



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@csrf_exempt
def detect_browser(request):
    print(request.user.is_authenticated)

    try:
        if request.user.is_authenticated == False:

            data = json.loads(request.body)
            browser = data['browser']
            operating_system = data['os']

            b = Browser.objects.get_or_create(name=browser)
            o = OperatingSystem.objects.get_or_create(name=operating_system)

            p = PageLoad()
            p.page = data['url']

            p.meal = data['mealName'].strip()
            if len(p.meal) < 1:
                p.meal = 'Home Page'

            p.browser = b[0]
            p.operating_system = o[0]
            p.ip_address = get_client_ip(request)
            p.time_stamp = timezone.now()

            p.save()


    except Exception as e:
        print('-------')
        print("unable to do this for the following reason")
        print(e)
        print()


    return HttpResponse("Success")


# sendgrid
def send_email(email, subject, message, from_email):
    apikey = config('SENDGRID_API_KEY')
    sg = sendgrid.SendGridAPIClient(apikey=apikey)
    from_email = Email(from_email)
    to_email = Email(email)
    content = Content("text/html", message)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
