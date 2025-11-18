from django import forms

class IngredientSearchForm(forms.Form):
    ingredients = forms.CharField(
        label='Ваши ингредиенты',
        widget=forms.Textarea(attrs={
            'placeholder': 'Введите ингредиенты через запятую\nНапример: помидоры, лук, чеснок, масло',
            'rows': 3,
            'class': 'form-control'
        }),
        help_text='Перечислите ингредиенты, которые у вас есть'
    )