from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def random_testing(test_script):
    print("Celery Working" + test_script)
