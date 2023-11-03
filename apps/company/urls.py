from django.urls import path

from company.views import AboutListAPIView, PhoneListAPIView, SocialListAPIView, SettingsListAPIView

urlpatterns = [
    path('about/', AboutListAPIView.as_view(), name='about'),
    path('phone/', PhoneListAPIView.as_view(), name='phone'),
    path('social/', SocialListAPIView.as_view(), name='social'),
    path('settings/', SettingsListAPIView.as_view(), name='settings'),
]

"""
A train approached the dead end from track 1 (see picture). You are allowed to uncouple one
or several of the first 11 cars from the train at once and drive them to a dead end (if desired
you can even drive the entire train to a dead end at once). After this, some of these cars can 
be taken out towards track 2. After this, a few more cars can be brought into the dead end
and again some of the remaining cars can be taken out towards track 2. And so on (so that 
each car can only enter once from track 1 into dead end, and then drive out of the dead end
onto path 2 once). It is prohibited to enter a dead end from path 2 or exit from a dead end
onto path 1. It is impossible to get from path 1 to path 2 without reaching a dead end. It is
known in what order the train cars initially go. It is required, using the indicated operations, to
ensure that the train cars move in order (first the first, then the second, etc., counting from the
head of the train traveling along track 2 away from the dead end).
"""
