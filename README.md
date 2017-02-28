https://docs.djangoproject.com/en/1.10/intro/install/

Follow the steps outlined in the link above to install the latest version of Python 3.X, create a virtualenv, and then install Django within that virtualenv.

Go to the directory containing your virtualenv (it should have folders such as bin, lib, include..), and pull the vjk repo into that directory using this command: git clone https://github.com/CodeTheChangeUBC/vjk.git

To test, cd into the vjk repo and through the command line, enter: python manage.py runserver
then through your web browser, go to http://127.0.0.1:8000 and you should see a default Django admin page saying "congrats, it worked!"
