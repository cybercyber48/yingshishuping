from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from books.models import Book
from PIL import Image

from main.ImageUpload_Form1 import Image_Upload_Form1
    
def HomePageView(request):
    image_form = Image_Upload_Form1(request.POST or None, request.FILES or None)
    return render(request, 'main/index.html', {'image_form': image_form})


def Search(request):
    selected_book = Book.objects.get(book_name=request.POST['search_text'])
    return HttpResponseRedirect(reverse('books:detail',args=(selected_book.id,)))
    
def SearchImage(request):
    #uploaded_image = request.FILES['image']   # 'image' is the name of Image_Upload_Form1.image 
    im = Image.open( request.FILES['image'] )
    width, height = im.size
    pix = im.load()
    value = pix[width/2, height/2]
    R=value[0]
    G=value[1]
    B=value[2]
    im.close()
#    html = "<html><body>The color is (%(R)s,%(G)s,%(B)s).</body></html>" % {'R':value[0],'G':value[1],'B':value[2]}
    book_list =( Book.objects.filter(book_image_R__range=(R-50,R+50))
    .filter(book_image_G__range=(G-50,G+50))
    .filter(book_image_B__range=(B-50,B+50)))
    return render(request,'main/Search_result.html',{'book_list':book_list})