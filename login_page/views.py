from django.shortcuts import render
from .models import login_model
from .form import login_form
# Create your views here.

def login_page_index_page(request):
	request.session.set_expiry(86400)

	senders =[]
	obj = login_model.objects.all()
	for i in obj:
		senders.append(i.username)
	

	if request.method=='POST':
		if request.POST['action']=="LOGOUT":
			obj = login_model.objects.get(session_key=request.POST['session_key'])
			obj.session_key='n/a'
			obj.save()
			return render(request,"login_page.html",{})
		else:
			obj = login_model.objects.all()
			for i in obj:
				if str(i.mobile_no) == str(request.POST['mobile_no']) and str(i.password) == str(request.POST['password']):
					i.session_key = request.session.session_key 
					i.save()
					return render(request,"homepage.html",{"username":i.username,"session_key":i.session_key,"number":i.mobile_no,"auth":i.auth,"senders":senders})
			return render(request,"login_page.html",{})
	
	else:
		try:
			obj = login_model.objects.get(session_key=request.session.session_key) 	
			return render(request,"homepage.html",{"username":obj.username,"number":obj.mobile_no,"auth":obj.auth,"session_key":obj.session_key,"senders":senders})
		except:
			return render(request,"login_page.html",{})