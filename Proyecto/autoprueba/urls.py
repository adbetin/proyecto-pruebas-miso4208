"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from autoprueba import views as view
from tester import views as view_tester

urlpatterns = [
    path('', view.index, name='index'),
    path('headless/cypress', view.headless_cypress, name='headless_cypress'),
    path('headless/cypress_process', view.headless_cypress_process, name='headless_cypress_process'),
    path('headless/webdriver', view.headless_webdriver, name='headless_webdriver'),
    path('mutation/mdroid', view.mutation_mdroid, name='mutation_mdroid'),
    path('mutation/mdroid_process', view.mutation_mdroid_process, name='mutation_mdroid_process'),
    path('android/', view.android, name='android'),
    path('calabash/', view.calabash, name='calabash'),
    path('cucumber/', view.cucumber, name='cucumber'),
<<<<<<< HEAD
    path('SQLGenerator/', view.sqlGenerator, name='sqlGenerator'),
    path('tester_android/<numEvent>/<packageHerramienta>/', view_tester.android, name='android')
=======
    path('tester_android/<numEvent>/<packageHerramienta>/', view_tester.android, name='android'),
    path('vrt/cypress', view.vrtcypress, name='vrtcypress'),
    path('vrt/resemble', view.vrtresemble, name='vrtresemble'),
>>>>>>> 689ace020016427e409a693c2597714a09a43477
]

