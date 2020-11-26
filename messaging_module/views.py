from django.shortcuts import render

# Create your views here.
def messages_index_page(request,session_key):
 	if request.method=="GET":
 		return render(request,"messages.html",{"session_key":session_key})