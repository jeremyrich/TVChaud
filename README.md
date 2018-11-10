# TVChaud

POOA project - Thomas Bellec, Edouard Borel, Hugo Martinet

## Installation

### First you need to copy the unzip folder in the desired directory

### Second, install the fonts located in __static/fonts/__ : *Raleway-Black.ttf* and *Raleway-Regular.ttf*

### Finally activate the virtual environment and launch the server
In the terminal:
* Go to the project directory
    ```
    cd path/to/folder/TVChaud
    ```

* Activate the environment
    * On Windows
        ```
        venv\Scripts\activate.bat
        ```
    * On MacOS/Linux
        ```
        source venv/bin/activate
        ```
* Then run the django server
    ```
    python manage.py runserver
    ```

* Open your web browser and enter the URL displayed in the terminal (http://127.0.0.1:8000/ or http://localhost:8000/).


## The Application

### Users

You already have 5 users in order to test different features, the users are called *user1*, *user2*, *user3*, *user4* and *user5*, and they all have the same password, which is *ouiouioui*.

Here are their specifications.

![Usermap](usermap.png)

### Features

With TVChaud, once logged in, you can navigate through TV shows, check out the cast, synopsis, similar shows etc, as well as season details, episodes resumes. You can also add shows to your favorites, add friends by typing their username in the invite bar and visualize your friends favorites. The notification button turns red when you have a new friend request or a new episode to watch.

You can try to consult series, add them to your favorites, invite friends and read your notifications. Enjoy !