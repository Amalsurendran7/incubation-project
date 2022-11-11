from rest_framework import serializers 
from .models import *
 
 
class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = customer
        fields = ('username',
                  'email',
                  'phone',
                  'password')

               
    def create(self, validated_data):
        return customer.objects.create(**validated_data)  

      

    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance = self.Meta.model(**validated_data)
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save() 
    #     return instance              