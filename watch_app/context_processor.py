from .models import *
from .views import *
def count(request):
    itm_ct=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            ct=CartList.objects.filter(cart_id=c_id(request))
            c_item=CartItems.objects.all().filter(cart=ct[:1])
            for i in c_item:
                itm_ct=itm_ct+1
        except CartList.DoesNotExist:
            itm_ct = 0
        return dict(itc=itm_ct)