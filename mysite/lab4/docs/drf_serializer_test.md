# drf_serializer_test.py
from lab4.models import Person
from lab4.serializers import PersonModelSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

# 1. Tworzenie instancji
person = Person(name='Jan', miesiac_dodania=1)
person.save()

# 2. Serializacja
serializer = PersonModelSerializer(person)
print(serializer.data)

# 3. Serializacja do JSON
content = JSONRenderer().render(serializer.data)
print(content)

# 4. Deserializacja
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
deserializer = PersonModelSerializer(data=data)

# 5. Walidacja i zapis
if deserializer.is_valid():
    deserializer.save()
    print(deserializer.data)
else:
    print(deserializer.errors)
