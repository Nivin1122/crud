from django.urls import path,include
from . import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('',views.signup,name="signup"),
    path('login/',views.login_user,name="login"),
    path('players/',views.players,name="players"),
    path('delete_players/<int:id>',views.delete_players,name="delete_players"),
    path('coaches/',views.coaches,name="coaches"),
    path('delete_coaches/<int:id>',views.delete_coaches,name="delete_coach"),
    path('contact_us/',views.contact_us,name="contact_us"),
    path('booking/',views.booking,name="booking"),
    path('ticket_list/',views.ticket_list,name="ticket_list"),
    path('confirmation/',views.confirmation,name="confirmation"),
    path('add_players/',views.add_players,name="add_players"),
    path('edit_players/<int:id>/',views.edit_players,name="edit_players"),
    path('add_tickets/',views.add_tickets, name="add_tickets"),
    path('ed_tickets/<int:id>/',views.edit_tickets,name="edit_ticket"),
    path('delete_tickets/<int:id>/',views.delete_tickets,name="delete_ticket"),
    path('add_coaches/',views.add_coaches, name="add_coaches"),
    path('edit_coach/<int:id>/',views.edit_coaches, name="edit_coach")
]
