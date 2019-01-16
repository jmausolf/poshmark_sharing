![](https://d2zlsagv0ouax1.cloudfront.net/assets/home_page/hp-v5-logo@2x-6003c7f00d83f4df697830d18bdcf167.png)

# Welcome to the Poshmark Sharing App

This script is designed for users with a [seller account on Poshmark marketplace](https://poshmark.com).

It is designed to automate sharing the listings for every item in your closet with all subscribers. Once the script is executed, it will share your listings every 60 minutes. You can edit the timing and other options if you desire.

# Let the Share War Begin

### Prerequisites

* Python 3.5+
* Firefox 46.0.1+
* [Selenium](http://selenium-python.readthedocs.io)==2.53.6+

### Setup

#### Git Clone

First clone the repository in terminal:
* `git clone https://github.com/jmausolf/poshmark_sharing

Change directories to enter the local repository:
* `cd poshmark_sharing`

#### User Credentials

You will need to create a `credentials.py` file. It is recommended to simply edit the `example_credentials.py` file and rename it.

```python
poshmark_username = "poshmarkusername"
poshmark_password = "poshmarkpassword"
```

Edit the text in quotes to your actual username and password. Save the file and rename it credentials.py. Assuming you are in the repo directory, the bash command would be `mv example_credentials.py credentials.py` .

#### Firefox

* *Recommendation:* Under Firefox Settings>Privacy: select "Always use private browsing mode" | This will help avoid Amazon captcha's. Adjusting the timing can also help if you have trouble.



## Run Share War App in Terminal

In terminal run the following command: `python share_war.py`

*Note:* If you have several versions of python, you will need to amend the above line to run your python 3 alias, e.g. `python3 share_war.py`.

## Run the Jupyter App

This program can also be run in Jupyter with a Python 3 kernel. Simply launch `jupyter notebook` in terminal and click the notebook, `PoshMark_Seller_Sharing_App.ipynb`. Once in the notebook, simply follow the instructions to run the script.

## Options

There are a variety of optional arguments for the script, including timing, closet scroll size, and closet ordering.

### Timing

You can adjust the timing from the command line. The default is 3600 seconds (60 minutes). Here are some examples:

* Every hour: `python share_war.py -t 3600`
* Every two hours: `python share_war.py -t 7200`

### Closet Size

If you have many listings, you may need to increase the number of times the application scrolls to the end of page (default, n=3), with the `-n` parameter:

* Scroll 5 times: `python share_war.py -n 5`

### Closet Ordering

To preserve closet order, the closet items must be shared in their reverse order. To this end, the default sorting is `order=True`:

* Preserve Closet Order, version 1:  `python share_war.py`
* Preserve Closet Order, version 2:  `python share_war.py -o True`

To override this option, you can reverse order the items of the closet with the following flag, `-o False`:

* Reverse Original Closet Order: `python share_war.py -o False`
