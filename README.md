![](https://d2zlsagv0ouax1.cloudfront.net/assets/home_page/hp-v5-logo@2x-6003c7f00d83f4df697830d18bdcf167.png)

# Welcome to the Poshmark Sharing App

This script is designed for users with a [seller account on Poshmark marketplace](https://poshmark.com).

It is designed to automate sharing the listings for every item in your closet with all subscribers or to share all the listings of another Poshmark account. Once the script is executed, it will share the requested listings every 120 minutes. You can edit the timing and other options if you desire.

# Let the Share War Begin

### Prerequisites

* Python 3.5+
* Firefox 46.0.1+
* [Selenium](http://selenium-python.readthedocs.io)==2.53.6+

## Setup

#### Git Clone

First clone the repository in terminal:
* `git clone https://github.com/jmausolf/poshmark_sharing`

Change directories to enter the local repository:
* `cd poshmark_sharing`

#### User Credentials

You will need to create a `credentials.py` file. It is recommended to simply edit the `example_credentials.py` file and rename it.

```python
poshmark_username = "poshmarkusername"
poshmark_password = "poshmarkpassword"
```

Edit the text in quotes to your actual username and password. Save the file and rename it `credentials.py`. Assuming you are in the repo directory, the bash command would be `mv example_credentials.py credentials.py` .

#### Firefox and Other Web Drivers

* The default webdriver for this script is Firefox, which was the original web browser used in writing this script and executing the code. From a development perspective Firefox offers a better interface to inspect the HTML code needed in writing the scraper. However, other webdrivers, including Chrome, Safari, or Edge may be used. 

To learn more about setting up the appropriate web driver, visit the Selenium web driver documentation below:
[https://selenium-python.readthedocs.io/installation.html#drivers](https://selenium-python.readthedocs.io/installation.html#drivers)

# Quick Start

## Run in Terminal (Recommended)

In terminal run the following command: `python share_war.py`, which will run the script with the default options (see below).

*Note:* If you have several versions of python, you will need to amend the above line to run your python 3 alias, e.g. `python3 share_war.py`.

## Run in Jupyter

This program can also be run in Jupyter with a Python 3 kernel. Simply launch `jupyter notebook` in terminal and click the notebook, `PoshMark_Seller_Sharing_App.ipynb`. Once in the notebook, simply follow the instructions to run the script, which is configured to run the default options.

# Advanced Options

There are a variety of optional arguments for the script, including timing, closet scroll size, closet ordering, the account to share, and the webdriver. To display the full range of command line arguments type `python share_war.py --help`. For convenience, these options are displayed in the Jupyter notebook and described below.

### Timing

You can adjust the timing from the command line. The default is 7200 seconds (120 minutes or 2 hours). Using a shorter time period is not recommended as it will be more likely caught by both captcha (`I am not a robot`) detection systems either at login or during the actual sharing. Here are some examples:

* Every four hours: `python share_war.py -t 14400`
* Every two hours: `python share_war.py -t 7200`

### Closet Size

The latest version of this code will automatically scroll to the end of your active listings in your closet. You should no longer need to adjust the number of possible scrolls (default, n=1000). If you desired to share only part of your closet, you could descrease the number of scrolls with the `-n` parameter:

* Scroll only 1 times: `python share_war.py -n 1`


### Closet Ordering

To preserve closet order, the closet items must be shared in their reverse order. To this end, the default sorting is `order=True`:

* Preserve Closet Order, version 1:  `python share_war.py` 
* Preserve Closet Order, version 2:  `python share_war.py -o True`

To override this option, you can reverse order the items of the closet with the following flag, `-o False`:

* Reverse Original Closet Order: `python share_war.py -o False`


### Account

By default, the code will share all the listings for Poshmark account provided in credentials.py. While you will still need your account information in credentials.py to login, you may request that the code share the listings of another Poshmark user with the account option: `python share_war.py -a another_poshmark_closet`. This can be a useful feature, for example, in becoming a Poshmark ambassador.

Since the code is setup to run on a loop (by default every two hours), a safeguard is put in place to confirm that you actually want to share another users account. This will appear in the terminal:

```
[*] you have requested to share
    the items in another poshmark closet:
    ------------------------------------
    [*]: another_poshmark_closet
    ------------------------------------


[*] to confirm this request, enter [y]
    to cancel and share your closet items instead enter [n] :
y
```
This prompt will occur each time the code runs. If you are confident you want to repeatedly share another users entire closet every few hours, you can bypass this prompt with the following command line option `b True`. 


### Random Sharing Subset

If you would prefer to not share your entire closet (or another account's entire closet), you may select to share a randomly selected subset of items from all possible active items. To do so, add the parameter `-r` followed by a number to your command in the terminal:

* Share 25 randomly selected items from another closet: `python share_war.py -a another_poshmark_closet -r 25`

This is helpful if you would like to share some of another person's closet but not every item they have.


### Webdriver

Alternative Selenium web drivers may also be specified. Drivers may be called by entering their name, e.g. `-d Firefox` or `-d Chrome` or alternatively referring to the numerical shortcut for those options, e.g. `-d 0` or `-d 1`. The full list of driver names and options is as follows:

* Firefox==0
* Chrome==1
* Edge==2
* Safari==3

These must be properly installed on your system, otherwise you will encounter an error. See https://selenium-python.readthedocs.io/installation.html#drivers for further details.
