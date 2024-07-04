# from rest_framework import serializers

# class LoginSerializer(serializers.Serializer):
#     nome = serializers.CharField()
#     senha = serializers.CharField()

#     def validate(self, data):
#         nome = data.get('nome')
#         senha = data.get('senha')

#         if not nome:
#             raise serializers.ValidationError("O nome de usuário é necessário para fazer login.")
#         if not senha:
#             raise serializers.ValidationError("A senha é necessária para fazer login.")

#         return data
