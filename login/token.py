from django.contrib.auth.tokens import PasswordResetTokenGenerator  
import six

class TokenGenerator(PasswordResetTokenGenerator):  
    def _make_hash_value(self, user, timestamp):  
        return (  
            six.text_type(user.data['id']) + six.text_type(timestamp) +  
            six.text_type(user.validated_data['is_active'])  
        )
    
class TokenVerifier(PasswordResetTokenGenerator):  
    def _make_hash_value(self, user, timestamp):  
        return (  
            six.text_type(user.pk) + six.text_type(timestamp) +  
            six.text_type(user.is_active)  
        )  
    
account_activation_token_verifier = TokenVerifier()  

account_activation_token = TokenGenerator()