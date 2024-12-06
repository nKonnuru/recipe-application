from django.shortcuts import render, get_object_or_404, redirect
from django.db import connection
from .models import Recipe
from .forms import RecipeForm


def recipe_list(request):
    query = request.GET.get('search', '')  # Get the search query from the URL
    if query:
        recipes = Recipe.objects.filter(title__icontains=query)  # Filter recipes by title
    else:
        recipes = Recipe.objects.all()  # Show all recipes if no query is provided

    return render(request, 'recipe_app/recipe_list.html', {'recipes': recipes, 'query': query})

def recipe_create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipe_app/recipe_form.html', {'form': form})


def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe_app/recipe_form.html', {'form': form})


def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'recipe_app/recipe_confirm_delete.html', {'recipe': recipe})


def recipe_report(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        # Use gte and lte for inclusive filtering
        recipes = Recipe.objects.filter(created_at__gte=start_date, created_at__lte=end_date)
    else:
        recipes = Recipe.objects.all()

    return render(request, 'recipe_app/recipe_report.html', {'recipes': recipes})


def advanced_report(request):
    with connection.cursor() as cursor:
        # Replace this SQL with your desired query
        cursor.execute("SELECT COUNT(*), AVG(LENGTH(ingredients)) FROM recipe_app_recipe")
        result = cursor.fetchone()  # Returns a tuple (count, avg_length)

    # Prepare the data for the template
    context = {
        'recipe_count': result[0],
        'avg_ingredient_length': result[1],
    }
    return render(request, 'recipe_app/advanced_report.html', context)


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_app/recipe_detail.html', {'recipe': recipe})

