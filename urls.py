from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Root points to the home app (minimal mapping for this sample project)
    path('', include('home.urls')),
    # Optional: include other app URLconfs as needed
    path('hello/', include('hello.urls')),
    path('users/', include('users.urls')),
]

# Basic custom error handlers (left as defaults unless apps override them)
# Uncomment and customize if you have handlers defined in your views
# handler404 = 'home.views.handler404'
# handler500 = 'home.views.handler500'
