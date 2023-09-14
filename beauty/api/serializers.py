from rest_framework import serializers
from business.models import Business
from locations.models import Region
from beauty.models import *

class GenericNameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name']

    def __init__(self, model, *args, **kwargs):
        self.Meta.model = model
        super().__init__(*args, **kwargs)



class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business  # Replace with your BUSINESS MODEL
        fields = ['name', 'phone_number']  # Replace with the name and phone number fields in your Business model
class RegionSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Region
        fields = ['name', 'subcounty', 'county', 'is_city']
        depth = 1 

class BeautySerializer(serializers.ModelSerializer):
    category = GenericNameSerializer(Beauty_Category)
    subcategory = GenericNameSerializer(Beauty_Sub_Category)
    type = GenericNameSerializer(Beauty_Type)
    region = RegionSerializer() # Add this field to the serializer
    app_name = serializers.SerializerMethodField()
    owner_info = serializers.SerializerMethodField()

    class Meta:
        model = Beauty
        exclude = ["owner", "id", "sponsored", "featured", "new"]
        read_only_fields = ['owner']

    def get_app_name(self, obj):
        return obj.__class__._meta.app_label

    def get_owner_info(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            owner_serializer = OwnerSerializer(obj.owner)
            return owner_serializer.data
        return None


class BeautyCreateSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Beauty
        exclude = ["owner", "id", "created", "updated", "slug", "currency", "product_serial",
                   "sponsored", "featured", "new", "most_sold", "out_of_stock"]

        
