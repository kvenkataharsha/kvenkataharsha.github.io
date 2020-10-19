from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
import datetime
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )

    def check_token(self, user, token):
        time = datetime.datetime.now()
        time1 = str(time)
        h = time1.split()
        h1 = h[0:1]
        h1 = str(h1)
        h1 = h1.split("-")
        h1 = str(h1)
        print(h1)
        # h1 = list(map(int, h1))
        if (self._num_days(self._today()) - h1) > 1: # 1 day = 24 hours
            print("****************************")
            return False
account_activation_token = TokenGenerator()