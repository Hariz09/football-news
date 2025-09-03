from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406428775',
        'name': 'Muhammad Hariz Albaari',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)