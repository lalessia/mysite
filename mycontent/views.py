from django.shortcuts import render

def post_list(request):
    return render(request, 'mycontent/post_list.html', {})