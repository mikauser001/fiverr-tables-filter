import django_tables2 as tables
from .models import Exchange


class ExchangeTable(tables.Table):

    # coin Template Column
    coin = tables.TemplateColumn(
        '{% if record.coin.all %} {% for coin in record.coin.all %}<img class="token" style="margin-bottom: 2px; margin-left: 0rem; max-height: 32px;" '
        'width=""  src="/media/{{coin.logo}}" title="{{coin.name}}"/>	{% endfor %} {% endif %}'
        , orderable=False)
    logo = tables.TemplateColumn(
        '{% if record.logo %} <img class="logo" style="margin-bottom: 2px; margin-left: 0rem; max-height: 32px;" '
        'width=""  src="/media/{{record.logo}}"/> {% endif %}'
        , orderable=False)

    dex = tables.BooleanColumn()

    class Meta:
        model = Exchange
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'logo', 'coin', 'dex', 'kyc', 'maker_fee')
