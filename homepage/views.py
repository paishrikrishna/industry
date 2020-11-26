from django.shortcuts import render
from login_page.models import login_model
# Create your views here.
def homepage_index_page(request,session_key):
	senders =[]
	obj = login_model.objects.all()
	for i in obj:
		senders.append(i.username)
	
	if request.method == "GET":
		obj = login_model.objects.get(session_key=session_key)
		return render(request,"homepage.html",{"session_key":obj.session_key,"username":obj.username,"senders":senders})
	else:
		obj = login_model.objects.get(session_key=session_key)
		return render(request,"homepage.html",{"session_key":obj.session_key,"username":obj.username,"senders":senders})