from django_filters import FilterSet, ModelChoiceFilter, DateTimeFilter
from .models import *
from django.forms import DateTimeInput
from .resources import CATEGORIES


class PostFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label='Category',
        empty_label='все категории',
    )

    added_after = DateTimeFilter(
        field_name='time',
        lookup_expr='gt',
        label='Date',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }


