import redis
from django.apps import AppConfig


class McDonaldsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mc_donalds'

red = redis.Redis(
    host='redis-13842.c73.us-east-1-2.ec2.cloud.redislabs.com',
    port=13842,
    password='f4zCXgTzfhfbYy7kUMJA8Mrpoe8F9c9U'
)