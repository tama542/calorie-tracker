
from django.shortcuts import render, redirect
from .models import FoodItem

def home(request):
    food_items = FoodItem.objects.all()
    total_calories = sum(item.calories for item in food_items)
    return render(request, 'home.html', {'food_items': food_items, 'total_calories': total_calories})

def add_food(request):
    if request.method == 'POST':
        name = request.POST['name']
        calories = request.POST['calories']
        FoodItem.objects.create(name=name, calories=calories)
        return redirect('home')
    return render(request, 'add-food.html')

def delete_food(request, food_id):
    FoodItem.objects.get(id=food_id).delete()
    return redirect('home')

def reset_calories(request):
    FoodItem.objects.all().delete()
    return redirect('home')

