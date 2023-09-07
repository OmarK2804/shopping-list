from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'name': 'Omar Khalif Muchzi',
        'class': 'Platform-Based Development KKI'
    }

    return render(request, 'main.html', context)