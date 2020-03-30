from django import forms
from .models import Meal
# from tinymce import TinyMCE

# class TinyMCEWidget(TinyMCE):
#   def use_required_attribute(self, *args):
#     return False



class MealForm(forms.ModelForm):
  class Meta:
    model = Meal
    fields = ('meal_name',
      'date',
      'meal_type',
      'cuisine',
      'person',
      'location',
      'notes',
      'recipe',
      'make_again'
    )





# class PostForm(forms.ModelForm):
#   text = forms.CharField(
#     widget=TinyMCEWidget(
#       attrs={'required': False, 'cols': 30, 'rows': 10}
#     )
#   )
#   class Meta:
#     model = Post
#     fields = ('title', 'text',)


# class SubtitleForm(forms.ModelForm):
#   class Meta:
#     model = Subtitle
#     fields = ('text',)


# class ErrorMessageForm(forms.ModelForm):
#   class Meta:
#     model = ErrorMessage
#     fields = ('text',)





# class ReviewForm(forms.ModelForm):
#   class Meta:
#     model = ProductReview
#     fields = ('product', 'rating', 'title', 'reviewer_name', 'text')


# class CategoryForm(forms.ModelForm):
#   class Meta:
#     model = CategoryName
#     fields = ('category_name',)
