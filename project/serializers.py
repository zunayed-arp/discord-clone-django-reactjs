from dataclasses import fields
from rest_framework import serializers
from .models import IpList,AllowOrigin
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','username','email','password')
        extra_kwargs = {'password': {'write_only': True}}

class IpListSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpList
        fields='__all__'
        

class AllowOriginSerializer(serializers.ModelSerializer):

    class Meta:
        model = AllowOrigin
        fields = '__all__'
        
 
        
class AllowOriginAPIViewSerializer(serializers.ModelSerializer):
    ip_list = IpListSerializer(many=True)
    class Meta:
        model = AllowOrigin
        fields = ('id','ip_list','user')
        
    def create(self, validated_data):
        ips_data = validated_data.pop('ip_list')
        instance = AllowOrigin.objects.create(**validated_data)
        
        for ip_data in ips_data:
            ip = IpList.objects.create(**ip_data)
            instance.ip_list.add(ip)
        return instance
    
    
    
    def create_or_update_allow_orign(self,ips):
        ip_ids =[]
        for ip in ips:
            ip_instance,created = IpList.objects.update_or_create(pk=ip.get('id'),defaults=ip)
            ip_ids.append(ip_instance.pk)
        return ip_ids
        
    def update(self, instance, validated_data):
        ip_list = validated_data.pop('ip_list',[])
        instance.ip_list.set(self.create_or_update_allow_orign(ip_list))
        
        fields = ['user','is_active']
        for field in fields:
            try:
                setattr(instance,field,validated_data[field])
            except KeyError:
                pass
        instance.save()
        return instance   
            
    # def create_or_update_packages(self, packages):
    #     package_ids = []
    #     for package in packages:
    #         package_instance, created = Package.objects.update_or_create(pk=package.get('id'), defaults=package)
    #         package_ids.append(package_instance.pk)
    #     return package_ids
    
    #update
    #  def update(self, instance, validated_data):
    #     package = validated_data.pop('package', [])
    #     instance.package.set(self.create_or_update_packages(package))
    #     fields = ['order_id', 'is_cod']
    #     for field in fields:
    #         try:
    #             setattr(instance, field, validated_data[field])
    #         except KeyError:  # validated_data may not contain all fields during HTTP PATCH
    #             pass
    #     instance.save()
    #     return instance

        
        
    
    
    #not working
    # def update(self, instance, validated_data):
    #     contacts_data = validated_data.pop('contacts')

    #     instance.name = validated_data.get('name', instance.name)
    #     instance.save()

    #     # many contacts
    #     for contact_data in contacts_data:
    #         contact = Contact.objects.get(pk=contact_data['id']) # this will crash if the id is invalid though
    #         contact.name = contact_data.get('name', contact.name)
    #         contact.last_name = contact_data.get('last_name', contact.last_name)
    #         contact.save()

    #     return instance
    
    
    
    # def create(self, validated_data):
    #     ips_data = validated_data.pop('ip_list')
    #     instance = AllowOrigin.objects.create(**validated_data)
        
    #     ips = []
    #     for ip_data in ips_data:
    #         ip_id = ip_data.pop('id',None)
    #         ip,_ = IpList.objects.get_or_create(id=ip_id,defaults=ip_data)
    #         ips.append(ip)
    #     instance.ip_list.add(*ips)
    #     return instance
        
        
   
 
    
        