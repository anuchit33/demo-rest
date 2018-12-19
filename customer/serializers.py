from django.contrib.auth.models import User, Group
from rest_framework import serializers
from customer.models import Customer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name')
# class CustomerListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ('name', 'id','code','user','gender')

class CustomerListSerializer(serializers.ModelSerializer):
    gender_display = serializers.CharField(source='get_gender_display',)
    class Meta:
        model = Customer
        fields = ('name', 'id','code','user','gender','gender_display')
        #extra_kwargs = {'password': {'write_only': True}}

class CustomerDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Customer
        fields = ('name', 'id','code','user','email','gender')

class CustomerUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('name', 'id','code','user','email','gender')