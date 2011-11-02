from .views import *

urlpatterns = QuickBlockCRUDL().as_urlpatterns()
urlpatterns += QuickBlockTypeCRUDL().as_urlpatterns()
