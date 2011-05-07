=====================
django-admin-jqueryui
=====================

This app adds jQuery UI to your Django admin panel.

Installation
------------

1. Put 'admin_jqueryui' on your python path

2. Add 'admin_jqueryui' to INSTALLED_APPS tuple in settings file 

3. Unless using Django 1.3 or above, make static/admin_jqueryui/
   available under {{ MEDIA_URL }}admin_jqueryui/

Usage
-----

jQuery UI is now available in admin under both jQuery and 
django.jQuery namespace.