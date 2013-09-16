

# local system - specific
import crocodoc
from crocodoc import CrocodocErorr


from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import View

class CrocoDocView(View):
    redirect = None

    def get(self, request, *args, **kwargs):
        uuid = kwargs.pop('uuid', None)
        if uuid is None:
            raise Http404

        try:
            params = {}
            qs_params = request.GET
            
            bool_params = ("editable", "admin", "downloadable", "copyprotected", "demo")
            for p in bool_params:
                if p in qs_params:
                    params[p] = True
            
            if 'user_id' in qs_params and 'user_name' in qs_params:
                params['user'] = {
                    'id': qs_params['user_id'],
                    'name': qs_params['user_name'],
                }
            
            if 'filter' in qs_params:
                params['filter'] = qs_params['filter']
            
            if 'sidebar' in qs_params:
                params['sidebar'] = qs_params['sidebar']

            session = crocodoc.session.create(uuid, **params)
        except crocodoc.CrocodocError as e:
            return HttpResponse(content=e.response_content,
                                status=e.status_code)
        
        url = 'https://crocodoc.com/view/{0}'.format(session)
    
