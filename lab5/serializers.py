from rest_framework import serializers
from .models import Person, Team

class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    shirt_size = serializers.ChoiceField(choices=Person.SHIRT_SIZES, default='S')
    miesiac_dodania = serializers.ChoiceField(choices=Person.MONTHS, default=1)
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), allow_null=True)

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.shirt_size = validated_data.get('shirt_size', instance.shirt_size)
        instance.miesiac_dodania = validated_data.get('miesiac_dodania', instance.miesiac_dodania)
        instance.team = validated_data.get('team', instance.team)
        instance.save()
        return instance

class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'miesiac_dodania', 'shirt_size', 'team']
        read_only_fields = ['id']

class StanowiskoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = '__all__'
