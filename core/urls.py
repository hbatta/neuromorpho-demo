from django.urls import path
from core.views import Home, DisplayData
# from home_assignment.views import Home, display_data

app_name = "core"

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('neuron-list/', DisplayData.as_view(), name="neuron-list")
]

