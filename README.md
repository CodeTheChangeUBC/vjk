### 1) Install your environment

https://docs.djangoproject.com/en/1.10/intro/install/

Follow the steps outlined in the link above to install the latest version of Python 3.X, create a virtualenv, and then install Django within that virtualenv.

### 2) Clone this repo
Go to the directory containing your virtualenv (it should have folders such as bin, lib, include..), and pull the vjk repo into that directory using this command: 
```
git clone https://github.com/CodeTheChangeUBC/vjk.git
```

### 3) Run the app
To test, cd into the vjk repo and through the command line, enter: 
```
python manage.py runserver
```
then through your web browser, go to http://127.0.0.1:8000 (or localhost:8000) and you should see a default Django page saying "congrats, it worked!"

### Connect to the database through command line
Run "mysql -h vjk.c9vzvqoxblsh.us-west-2.rds.amazonaws.com -u ctc_vjk -p". This will create a prompt where you type in the password, which is in your mysite/settings.py file under the database section. If successful, you will be in the MySQL client and then you can type "use VJK" and then "show tables;"


