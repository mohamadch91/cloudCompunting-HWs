from rest_framework import serializers

## create CryptoSerializer class with one field crypto name of type CharField

class CryptoSerializer(serializers.Serializer): 
    """serializer for crypto name

    Args:
        serializers (Charfield): input asset name
    """
    crypto_name = serializers.CharField(max_length=100)
