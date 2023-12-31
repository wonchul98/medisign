from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView


urlpatterns = [

    # /
    #path("", include("medisign.users.urls", namespace="users")),

    # /medicines/
    path("medicines/", include("medisign.medicines.urls", namespace="medicines")),
    # /users/
    path("users/", include("medisign.users.urls", namespace="users")),
    # /pharmacies/
    path("pharmacies/", include("medisign.pharmacies.urls", namespace="pharmacies")),
    # /diseases/
    path("diseases/", include("medisign.diseases.urls", namespace="diseases")),
    # /widgets/
    path("widgets/", include("medisign.widgets.urls", namespace="widgets")),
    
    #/admin
    path('admin/', admin.site.urls),
    # /home
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
        
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
