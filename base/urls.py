from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_page, name="login"),
    path("register/", views.register_page, name="register"),
    path("spacecrafts/", views.spacecrafts_page, name="spacecrafts"),
    path("expeditions/", views.expeditions_page, name="expeditions"),
    path("order-history/", views.order_history, name="order-history"),
    path("book/<str:pk>", views.view_expedition, name="view-expedition"),

    path("modules/", views.view_modules, name="view-modules"),
    path("take-module/<str:pk>", views.take_module, name="take-module"),

    path("pdf/", views.pdf, name="pdf"),

    path("logout/", views.logout_user, name="logout"),


] 