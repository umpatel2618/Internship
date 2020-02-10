from rest_framewrok import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        # fields = ('ticker','volume')
        fields = '__all__'
