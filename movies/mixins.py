from django.contrib import messages
from django.http import HttpResponseRedirect


class ManageErrorResponseMixin:
    
    error_message = ''
    
    def post(self, request, *args, **kwargs):
        try:
            result = super().post(request, *args, **kwargs)
        except Exception as e:
            print(e)
            messages.error(request, self.error_message)
            return HttpResponseRedirect(self.success_url)
        else:
            return result
        
        
class MockRequestMixin:
    
    def get_form(self):
        form_class = self.get_form_class()
        return form_class(request=self.form_type, **self.get_form_kwargs())
