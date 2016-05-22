from django import forms

from books.models import Book

class BookEntryForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = fields = ['book_name','book_content','book_image']