kylewpppd.com
=============

### Sources for kylewpppd.com website ###

Running
-------

**You'll need Python, PIP, and VirtualEnv to successfully run the site**

1. Clone the repo to a folder on your machine:

    `$ git clonse git@github.com:KyleWpppd/kylewpppd.com.git`

   **Or**, if for some reason, the ssh url gives you trouble, try the HTTP link:

    `$ git clone https://github.com/KyleWpppd/kylewpppd.com.git`

2. Create a new virtual environment

     `$ virtualenv --no-site-packages .virtualenv`

3. Activate the virtual environment:

    `$ source .virtualenv/bin/activate`

   This should update your prompt with a `(.virtualenv)` prefix. The prefix is reflected in the rest of the instructions.


4. Use pip to install the requirements:

    `(.virtualenv)$ pip install -r requirements.txt`

5. Run the app in **debug** mode:

    `(.virtualenv)$ env KYLEWPPPD_COM_ENVIRONMENT="Development" python run.py`

6. Visit the app in your browser at [127.0.0.1:5000]("http://127.0.0.1:5000").

    1. You'll probably want to change the email address on the contact page.

7. Have a beer.

Tests
-----

What tests? This is web dev.
