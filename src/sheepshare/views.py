from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

def home(request):
	params = {
		"minutes": range(0, 60, 5),
		"hours": range(0, 24),
		"days": range(0, 365)
	}

	return render(request, "index.html", params)

def upload(request):
	file_list = request.FILES.getlist("file")

	return redirect("/")
