
############################# Cpannel hosting #############################
#cpanel ssh key create
ssh-keygen -t rsa -b 4096 -C "username@servername"


python manage.py makemigrations core
py manage.py migrate --database=mysql

from django.apps import apps
for app in apps.all_models:
    for key,value in apps.all_models[app].items():
        objlist = value.objects.using('default').all()
        print(key)
        for obj in objlist:
            print(obj)
            obj.save(using='mysql')