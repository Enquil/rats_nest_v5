from products.models import Domain, Color, Category, Product
from django import forms


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'brand', 'color', 'description',
                  'feature_list', 'default_price',
                  'image', 'image2', 'image3')
        labels = {'body': 'Leave a comment'}
        # widgets = {'body': forms.Textarea(attrs={'cols': 60, 'rows': 4})}
