# django_product_storesearch_app
Django application is for reading a JSON file, store the products and live search through registered products
<br><br> <img src="https://shahraksanatishk.ir/img/storesearch.png"> <br><br>
User tries to upload a JSON file via form, and then uploaded data will be stored in a database by using Django Models. Recurring uploads will update existing database rows instead of duplicating the data.
search box plus the registred records on the database will be apeared on the same page right after uploading them, and user will be able to search among the records (using live full text search method). Search results will be limited to 50 each page using pagination. A search for ”volkswagen polo” yield similar results to the figure bellow:
<br><br> <img src="https://shahraksanatishk.ir/img/storesearch2.png"> <br><br>

Database used in this project is MySQL, and you have to create one manually with the name "djangostoresearch" before making migrations! or you can change its configutation in the django project setting file!

```sh
$ git clone https://github.com/aliknd/django_product_storesearch_app.git
$ cd django_product_storesearch_app
$ pip install mysqlclient
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
