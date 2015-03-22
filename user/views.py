from django.shortcuts import render_to_response

# Create your views here.
from models import User
#######################
def search(request):
    search = request.GET.get('q', '')
    if search:
        results = User.objects.filter(login=search).order_by('id')
        return render_to_response("search.html", {"results": results, "search": search})
    return render_to_response("search.html", {"results": [], "search": search})


#######################

def combo(request):
    query = request.GET.get('q', '')
    elements = User.objects.values('login').distinct()
    if query:
        results = User.objects.filter(login=query)
        return render_to_response("search_combo.html", {"results": results, "query": query, "elements": elements})
    return render_to_response("search_combo.html", {"results": [], "query": query, "elements": elements})
    #######################