from django.contrib.auth.decorators import login_required
from django.http.response import  HttpResponseRedirect,HttpResponse
from django.shortcuts import render
import os
import mimetypes

from .models import Res
# Create your views here.
@login_required(login_url="/admin/login/?next=/")
def Home(request):
    res = Res.objects.all()
    context = {'res':res}
    return render(request,'index.html',context)

@login_required(login_url="/admin/login/?next=/")
def delete(request,code):
    res = Res.objects.get(code=code)
    file_path = f'./static{res.file.url}'
    os.remove(file_path)
    res.delete()
    return HttpResponseRedirect("/")

@login_required(login_url="/admin/login/?next=/")
def Download_func(request,code):
    file = Res.objects.get(code=code)
    file_path = f'./static{file.file.url}'
    file_name = file.file.name
    path = open(file_path, 'r',errors='ignore')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(file_path)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % file_name
    # Return the response value
    return response
    return HttpResponseRedirect('/')

