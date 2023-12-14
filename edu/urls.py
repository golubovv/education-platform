from django.contrib import admin
from django.urls import path, include

import users.urls
import lessons.urls
import courses.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(users.urls.url_patterns)),
    path('', include(lessons.urls.url_patterns)),
    path('', include(courses.urls.url_patterns))
]
