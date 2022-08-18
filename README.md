# DjangoBlog
![background](https://user-images.githubusercontent.com/95189114/185355982-668ef120-21f6-44d1-8f0b-dacd7f9b66bc.jpg)
Blog created by using Django Framework which features tool like: creating profile, updating profile, 
creating post and possibility to update posts - but only by the post author. Visual aspects in CSS are based and inspired by Start Boostrap website.
# Configuration
 - Navigate to the project folder and run **pip3 install -r requirements.txt**
 - Start application by running: **$ python manage.py runserver**
 - Website should be accessible at 127.0.0.1:8000
 - To create the SQL commands to reflect the changes to any tables within models.py, you create a "migration" file, which is stored in ~/migrations/, by running: **$ python manage.py makemigrations**
 - to apply the SQL located within migration files and alter the database, run: **$ python.manage.py migrate**
