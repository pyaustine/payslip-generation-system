from django.shortcuts import render
from . models import Staff

# Create your views here.
def index(request):
    staff = Staff.objects.all()

    context = {
        'staff': staff
    }
    return render(request, 'dashboard/index.html', context)