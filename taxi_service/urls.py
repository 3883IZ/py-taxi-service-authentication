urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("taxi.urls", "taxi"), namespace="taxi")),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="registration/logged_out.html"),
        name="logout",
    ),
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT,
)
