from django.shortcuts import render_to_response

from recipe.models import RecipeType


def search(request):
    query = request.GET.get('q', '')
    if query:
        results = RecipeType.objects.filter(name__icontains=query)
        return render_to_response("html/recipeType/search.html", {"results": results, "search": query})
    return render_to_response("html/recipeType/search.html", {"results": [], "search": query})


def create(request):
    name = request.GET.get('name', '')
    if name:
        p = RecipeType(name=name)
        p.save()
        return render_to_response('html/recipeType/create.html', {"success": True})
    else:
        return render_to_response('html/recipeType/create.html')


def delete(request):
    code = request.GET.get('code', '')
    results = RecipeType.objects.all().order_by('id')
    if code:
        p = RecipeType.objects.get(id=code)
        p.delete()
        return render_to_response('html/recipeType/delete.html', {"results": results, "code": code, "success": True})
    return render_to_response('html/recipeType/delete.html', {"results": results})


def update(request):
    id = request.GET.get('id', '')
    results = RecipeType.objects.all().order_by('id')
    if id:  # si solo obtengo el id , mostrar el detalle
        if not request.GET.get('name', ''):
            results = RecipeType.objects.filter(id=id).order_by('id')
            return render_to_response('html/recipeType/details.html', {"results": results})
    if id:
        if request.GET.get('name', ''):
            p = RecipeType.objects.get(id=request.GET.get('id', ''))  # Que registro va a actualizar
            p.id = request.GET.get('id', '')
            p.name = request.GET.get('name', '')
            p.save()
            results = RecipeType.objects.all().order_by('id')
            return render_to_response('html/recipeType/update.html', {"results": results, "id": id, "exito": True})
    return render_to_response('html/recipeType/update.html', {"results": results})
