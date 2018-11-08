# TVChaud

POOA project - Thomas Bellec, Edouard Borel, Hugo Martinet

## Installation

### First you need to copy the unzip folder in the desired directory

### Then we are going to setup and activate a virtual environment
In the terminal:
* Go to the project directory
    ```
    cd path/to/folder/TVChaud
    ```
* Install the *virtualenv* package
    ```
    pip install virtualenv
    ```
* Create the virtual environment
    * if the command *python -V* returns a python3 version
        ```
        virtualenv -p python tvchaudenv
        ```
    * otherwise, if it returns a python2 version, download python3 and
        ```
        virtualenv -p python3 tvchaudenv
        ```

* Activate the environment
    * On Windows
        ```
        tvchaudenv\Scripts\activate.bat
        ```
    * On MacOS/Linux
        ```
        source tvchaudenv/bin/activate
        ```

### You can now launch the application

* Install the fonts located in __static/fonts/__ : *Raleway-Black.ttf* and *Raleway-Regular.ttf*

* In the terminal, while in the TVChaud folder, run :
    ```
    pip install --upgrade -r requirements.txt
    ```

* Then run the django server
    ```
    python manage.py runserver
    ```

* Open your web browser and enter the URL displayed in the terminal (http://127.0.0.1:8000/ or http://localhost:8000/).


## The Application

### Users

You already have 5 users in order to test different features, the users are called *user1*, *user2*, *user3*, *user4* and *user5*, and they all have the same password, which is *ouiouioui*.

__user1__  
This user is friend with *user2* and *user3*.  
His favorite shows are *The Walking Dead* and *The Flash*, by the way he has notifications for these 2 shows.

__user2__  
This user is friend with *user1*.  
His favorite show is *The Simpsons*, by the way he has a notification for this show.

__user3__  
This user is friend with *user1*.  
His favorite show is *House of Cards*.

__user4__   
His favorite show is *Supernaturral*.

__user5__   
He has 2 pending friend requests from *user2* and *user3*.

You can easily create a new user with the register link, sign in with google or facebook, and send a friend request by tapping a username in the header.

### Features

With TVChaud, once logged in, you can navigate through TV shows, check out the cast, synopsis, similar shows etc, as well as season details, episodes resumes. You can also add shows to your favorites, add friends by typing their username in the invite bar and visualize your friends favorites. The notification button turns red when you have a new friend request or a new episode to watch.

You can try to consult series, add them to your favorites, invite friends and read your notifications. Enjoy !