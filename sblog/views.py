from django.shortcuts import render_to_response 
from sblog.models import BQBlog
 
def chapter(request):
    posts = BQBlog.objects.all()
    return render_to_response("chapter.html", {'posts':posts})

