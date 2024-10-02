**BSS** (Bitpin scoring system)

## Initialize
### 1. Run the project directly

1. **Install requirements files and packages**
    * Creating new python environment
    ```bash
    python3 -m vnev .venv
    ```
    * Install mysql-server and setup database
    * First open the terminal and run the following command to install mysql-server
        * Linux
        ```bash
        sudo apt install mysql-server
        ```
        * Mac OS
        ```bash
        brew install mysql
        ```
    * Create new database in mysql for the project (Use `mysql` command to run MySQL)
        ```bash
        CREATE DATABASE [PROJECT_DB_NAME];
        CREATE USER '[USERNAME]'@'localhost' IDENTIFIED BY '[PASSWORD]';
        GRANT ALL PRIVILEGES ON [PROJECT_DB_NAME] . * TO '[USERNAME]'@'localhost';
        QUIT;
        ```
    * Install BSS python package requirements
        ```bash
        pip3 install -r requirements.txt
        ```
        * You may get some errors in Mac OS. Run this command and then try again.
        ```bash
        CFLAGS="-I$(brew --prefix)/include" LDFLAGS="-L$(brew --prefix)/lib" pip install mysqlclient==2.0.3
        ```

    **NOTE:** If mysqlclient didn't install, first run these commands on terminal and try again pip install.
    ```bash
    sudo apt-get install python3.8-dev default-libmysqlclient-dev
    ```
   
2. **Setup environment variables**
    * Copy env_vars file entries into a file with name .env and fill the empty fields.<br>



3. **Run django-project**
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py createsuperuser
   python3 manage.py runserver 8000
   ```
   
4. **Create some user and contents**
      ```bash
      python3 create_data.py
      ```
   
5. **Test with locust**
   ```bash
   locust -f locustfile.py
   ```
   and test on locust server with any load
   
   

