# TVChaud

# Installation

## First we are going to setup and activate a virtual environment
In the terminal:
* Go to Desktop
    ```
    cd Desktop
    ```
* Install the *virtualenv* package
    ```
    pip install virtualenv
    ```
* Create the virtual environment
    * if the command *python -V* returns a python3 version, type :
        ```
        virtualenv -p python tvchaudenv
        ```
    * otherwise, if it returns a python2 version, type :
        ```
        virtualenv -p python3 tvchaudenv
        ```

* Activate the environment
    ```python
    # On Windows
    tvchaudenv\Scripts\activate.bat
    
    # On MacOS/Linux
    source tvchaudenv/bin/activate
    ```

## You can now go to the TVChaud folder on your computer

* In your file explorer, go to __static/fonts/__ and install fonts *Raleway-Black.ttf* and *Raleway-Regular.ttf* (double click on a font to install it)

* In the terminal, while in the TVChaud folder, run :
    ```
    pip install --upgrade -r requirements.txt
    ```

* Then run the django server
    ```
    python manage.py runserver
    ```

* Open your web browser and enter the URL displayed in the terminal. It should be either http://127.0.0.1:8000/ or http://localhost:8000/.