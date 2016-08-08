"#Django_Export_Excel" 
This is a pretty simple example which tells us how to add/modify data into database, 
and export one or multi data from database to Excel file.

how to install(below steps runs on windows):
1. Download Python 3.5 from official website. it will help us install like pip, easy_install, etc.
2. pip install virtualenv to install virtualenv tool which is very useful for multi django projects on your local develpment computer.
3. go to a folder whatever you want. and use command 'virtualenv djang_env' to create a python virtual environment. we will see it will use python 3.5 which you installed on your comptuer to install the new virtual enviroment. that means if you want to install a virtualenv which depends on python 2.7, you need to install python 2.7, and install the virtualenv on your python2.7/lib/site-pacakges, and at the same time, the command of virtualenv cames from python2.7. you must change the path system variables.
4. go to the virtualenv folder, you will see the several folder here. input the command: 'Scripts\activate', it will activate the virtualenv.
5. use command: 'pip install django', it will install the newest version of django for you. if you want to install like django 1.9, use 'pip install django==1.9'
6. pip install django-bootstrap3
7. pip install xlsxwriter
8. django-admin createproject xxx
9. copy the excel_export app to your django project.
10. add the excel_export to your settings/INSTALLED_APPS.
11. go to the django project folder, and command 'python manage.py makemigrations'.
12. python manage.py migrate.
13. python manage.py runserver.


good luck.
