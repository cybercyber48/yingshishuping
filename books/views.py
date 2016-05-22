from django.views import generic
from django.template import RequestContext
from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book
from books.Book_Form import BookEntryForm
from PIL import Image

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'books/index.html'
    context_object_name = 'book_list'
    
    def get_queryset(self):
        #return Book.objects.order_by('-book_name')[:5]
        return Book.objects.order_by('-id')
        
class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'
    #context_instance=RequestContext(request)
    
class AddView(CreateView):
    model = Book
    fields = ['book_name','book_content','book_image']
    template_name = 'books/add.html'
    
def Save(request):
    #p = Book.objects.create(book_name=request.FILES['book_name'], book_content="Springsteen")
    b = BookEntryForm(request.POST or None, request.FILES or None)
    if b.is_valid():
        b.save()
        im = Image.open( b.cleaned_data['book_image'])
        width, height = im.size
        pix = im.load()
        value = pix[width/2, height/2]
        bb = Book.objects.get(book_name=b.cleaned_data['book_name'])
        bb.book_image_R = value[0]
        bb.book_image_G = value[1]
        bb.book_image_B = value[2]
        bb.save()
        im.close()
    return HttpResponseRedirect(reverse('books:index'))
