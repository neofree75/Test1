from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from .models import Poziadavka_ee
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect

import datetime

from .forms import OdoslatForm
from django.core.paginator import Paginator

@login_required(login_url="/")
def zmena_dodavatela_ee(request):
	
	if request.method == "POST":
		form = OdoslatForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.kod_spravy = "101"
			post.save()
			return redirect('detail_poziadavky', pk=post.pk)
	else:
		form = OdoslatForm()
	return render(request, 'Zmena_dodavatela_ee.html', {'form': form})

from django.shortcuts import render, get_object_or_404

@login_required(login_url="/")
def poziadavky(request):
	posts = Poziadavka_ee.objects.filter(datum_vytvorenia__lte=timezone.now()).order_by('-datum_vytvorenia')

	#user_list = User.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(posts, 5)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	return render(request, 'Poziadavky.html', {'posts': posts})

@login_required(login_url="/")
def detail_poziadavky(request, pk):
    post = get_object_or_404(Poziadavka_ee, pk=pk)
    return render(request, 'Detail_poziadavky.html', {'post': post})