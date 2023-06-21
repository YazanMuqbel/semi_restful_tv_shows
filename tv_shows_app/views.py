from django.shortcuts import render, redirect
from .models import Show

# This function retrieves all shows from the database and displays them on the home page (index.html).
def index(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'index.html', context)

# This function displays a form that allows the user to input details about a new TV show, 
# and saves it to the database once the form is submitted.
def create_show(request):
    if request.method == 'POST':
        show = Show()
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
        return redirect('show_info', id=show.id)
    else:
        return render(request, 'create_show.html')

# This function displays all the details about a specific TV show 
# on a page with the corresponding ID (show_info.html).
def show_info(request, id):
    show = Show.objects.get(id=id)
    context = {
        'show': show
    }
    return render(request, 'show_info.html', context)

# This functionn displays a list of all TV shows that have been added to the database
def show_all_shows(request):
    shows = Show.objects.all()
    context = {
        'shows': shows
    }
    return render(request, 'shows.html', context)

# This function deletes a specific TV show from the database and sends the user to a page that has a list of existing shows
def delete_show(request, id):
    #if request.method == 'POST':
        Show.objects.filter(id=id).delete()
        return redirect('list_of_all_shows')

#This part allows the user to edit/update information of an existing tv show
"""def update_show(request, id):
    show = Show.objects.get(id=id)

    #if request.method == 'POST':
    Show.objects.filter(id=id)
    return redirect('update')"""


"""def session_show(request):
    session=request.session.get('show', int(id))

    request.session['show'] = session
    context = {
        "session": session
    }
    return render(request, 'show_info.html', context)"""
