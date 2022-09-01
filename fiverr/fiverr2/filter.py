from django_filters import FilterSet, CharFilter, BooleanFilter
from django_filters.widgets import BooleanWidget
from .models import Exchange, Network
import django.forms as forms


class ExchangeFilter(FilterSet):
    name = CharFilter(label='Name',
                      lookup_expr='contains')
    dex = BooleanFilter(label='DEX', widget=forms.NullBooleanSelect(
        attrs={'title':'DEX', 'margin-left':'15px'}
    ))
    #network = CharFilter(label='network', method='get_networks' )

    class Meta:
        model = Exchange
        fields = ['name', 'dex', 'kyc']

