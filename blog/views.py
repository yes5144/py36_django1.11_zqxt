from django.shortcuts import render
import json
from users.models import User

# Create your views here.
def index(request):
    return render(request, 'baseblog.html')

def test_jinja(request):
    return render(request, 'test_jinja.html')
	
def accounts_profile(request):
    if request.method == 'POST':
        a = json.loads(request.body)
        print(a)
        b = User.objects.get(email=request.user.email)
        b.name = a['name']
        b.save()
    return render(request, 'accounts_profile.html')
