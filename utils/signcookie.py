from django.core.signing import TimestampSigner

class MySigner(TimestampSigner):
    def sign(self, value):
        return value + '12345678'

    def unsign(self, value, max_age=None):

        return value[0:-8]
