# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from django.contrib.auth.models import User
from datetime import datetime
from app.models import File

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('get_full_name', 'email', 'username')
        read_only_fields = ('get_full_name', 'email', 'username')

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id_file', 'file_name', 'file_data', 'created_at', 'updated_at','deleted_at']



