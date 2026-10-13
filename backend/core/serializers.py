from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, Profile


class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['user_email', 'password', 'name', 'phone_number', 'provider']

    def create(self, validated_data):
        # 비밀번호 해시 암호화 저장
        raw_password = validated_data.pop('password')
        validated_data['password_hash'] = make_password(raw_password)

        user = User.objects.create(**validated_data)

        # 회원가입 시 기본 본인 프로필 자동 생성
        Profile.objects.create(
            user=user,
            profile_name=user.name,
            relationship="본인",
            is_main=True
        )
        return user