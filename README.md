
# Django Python Framework

## Upgrade pip windows
```
python -m pip install -U pip
```


## Install requirements

    ```
     pip freeze > requirements.txt
     pip install -U -r requirements.txt
     pip install -r requirements.txt
    ```


 Or

    ```
     pip install django
     pip install Django --upgrade

     pip install mysql-python
     pip install python-mysqldb

     pip2.7 install pytz
     pip3.4 install pytz

     pip2.7 install pillow
    ```




## Get Versions
    ```
     python --version
     django-admin --version
    ```



## Create virtual env in Windows

    ```
      pip install virtualenvwrapper-win

      mkvirtualenv myapp

      workon myapp
    ```


## Create project and apps


     ```
      django-admin startproject myapp
      python manage.py startapp blog
     ```



	  ```
        In  settings.py
        INSTALLED_APPS = (
            ....
            'blog',
        )
       ```


## Manage Help


   ```
       python manage.py help
   ```

## Make migrations and Migrate


  ```
       python manage.py makemigrations
       python manage.py migrate
  ```


## Create super user in Admin


   ```
       python manage.py createsuperuser
   ```


## Runserver In Dev


   ```
       python manage.py runserver
       http://127.0.0.1:8000/
   ```

## Load initial data

   ```
        python manage.py loaddata initial.json
   ```

## Open shell console

   ```
        python manage.py shell
   ```


## Edit Configurations In PyCharm

  * Script:                 C:\...\myapp\manage.py
  * Script parameters:     runserver 127.0.0.1:8000

