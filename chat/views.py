from django.shortcuts import render

# Create your views here.
def mian_view(request):
    context={}
    return render(request,'chat/main.html',context=context)