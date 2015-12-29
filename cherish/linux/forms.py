from django import forms
from linux.models import Category, Page
class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, label='分類名稱', help_text='(請輸入分類名稱)')
 
    class Meta:
        model = Category
        fields = ('name', )
 
class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, label='網頁標題')
    url = forms.URLField(max_length=128, label='網頁網址')
 
    class Meta:
        model = Page
        exclude = ('category', 'views')