from django.shortcuts import render
from django.shortcuts import render
from .models import Gallery
from .models import Listing
from django.db.models import Q
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def developers(request):
    return render(request, 'main/developers.html')


def indoor(request):
    return render(request, 'main/indoor.html')


def outdoor(request):
    return render(request, 'main/outdoor.html')


def gallery(request):
    gal_img = Gallery.objects.all()
    return render(request, 'main/gallery.html', context={'gal_img': gal_img})


def listings(request):
    unit_type = request.GET.get('unit_type')
    view = request.GET.get('view')
    if unit_type or view:
        listing_object = Listing.objects.filter(Q(UNIT_TYPE__icontains=unit_type) & Q(VIEW__icontains=view))
        return render(request, 'main/listings.html', context={'listing_object': listing_object})
    else:
        listing_object = Listing.objects.all()
        return render(request, 'main/listings.html', context={'listing_object': listing_object})


def contact(request):
    return render(request, 'main/contact.html')


def privacy(request):
    return render(request, 'main/privacy-policy.html')


def disclaimer(request):
    return render(request, 'main/disclaimer.html')




