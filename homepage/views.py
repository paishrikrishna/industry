from django.shortcuts import render
from login_page.models import login_model
from messaging_module.models import messages_model
from messaging_module.form import messages_form
# Create your views here.

import datetime

x = str(datetime.datetime.now()).split(" ")


def homepage_index_page(request,session_key):
	senders =[]
	obj = login_model.objects.all()
	for i in obj:
		senders.append(i.username)
	
	if request.method == "GET":
		obj = login_model.objects.get(session_key=session_key)
		return render(request,"homepage.html",{"session_key":obj.session_key,"username":obj.username,"senders":senders})
	else:
		if request.POST['action'] == "Send Message":
			obj = login_model.objects.get(session_key=session_key)
			try:
				messages_form().save()
			except:
				msg = messages_model.objects.get(sender='n/a')
				msg.sender = obj.username
				msg.rx = request.POST['recivers']
				msg.message = request.POST['message']
				msg.date = x[0]
				msg.time = x[1][0:5]
				msg.save()
			return render(request,"homepage.html",{"session_key":obj.session_key,"username":obj.username,"senders":senders})