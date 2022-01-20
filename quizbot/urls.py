from django.contrib import admin
from django.urls import path

from leaderboard.views import UpdateScores, Leaderboard
from quiz.views import RandomQuestion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/random/', RandomQuestion.as_view(), name='random'),
    path('api/score/update/', UpdateScores.as_view(), name='score_update'),
    path('api/score/leaderboard/', Leaderboard.as_view(), name='leaderboard')

]
