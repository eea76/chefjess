from django import forms
from .models import Post, Subtitle, ErrorMessage, Product, ProductReview, CategoryName
from tinymce import TinyMCE

class TinyMCEWidget(TinyMCE):
  def use_required_attribute(self, *args):
    return False

class PostForm(forms.ModelForm):
  text = forms.CharField(
    widget=TinyMCEWidget(
      attrs={'required': False, 'cols': 30, 'rows': 10}
    )
  )
  class Meta:
    model = Post
    fields = ('title', 'text',)


class SubtitleForm(forms.ModelForm):
  class Meta:
    model = Subtitle
    fields = ('text',)


class ErrorMessageForm(forms.ModelForm):
  class Meta:
    model = ErrorMessage
    fields = ('text',)


class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = ('name', 'image', 'description', 'price', 'is_in_stock', 'size', 'color', 'is_top_seller', 'is_new',)


class ReviewForm(forms.ModelForm):
  class Meta:
    model = ProductReview
    fields = ('product', 'rating', 'title', 'reviewer_name', 'text')


class CategoryForm(forms.ModelForm):
  class Meta:
    model = CategoryName
    fields = ('category_name',)
