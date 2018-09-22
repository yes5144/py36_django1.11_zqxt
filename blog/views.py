from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'baseblog.html')

def test_jinja(request):
    return render(request, 'test_jinja.html')
	
def accounts_profile(request):
    return render(request, 'accounts_profile.html')
