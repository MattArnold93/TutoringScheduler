# TutoringScheduler
Tutor Scheduling Service for the University of Mary Washington

#Installation:

This is a list of things to install to allow this to work:

**1. Python**

**2. Flask**

**3. MySql and MySQLdb** - MySQLdb is a library that you will need to download. It is easiest to use "pip" to install. If you dont have pip installed, install that as well. 

Download all of these things and install them and you should be good to go!

#Starting Up The Server:
This will be updated one the Database functionallity is added. To start up your server currently, in the terminal, type the command "python server.py". This will fire up the server. To view the application, navigate to 127.0.0.1:2500 in the web browser of your choice. Whatever is has been built and is functional will be present for you to enjoy. Again, this will be updated once Sql comes into play

#Working On Features/Functions:
When workin on new features, always create a new branch. Never work off of the master branch. This can cause a multitude of issues. The master should always contain stable and working features, not features that are currently being developed.
One example for branch is, lets say, you are about to work on Login. Use the command "git checkout -b nameofthebranchhere".
This will create a new branch with whatever you named it. Use the command "git pull origin master". This will make sure your branch is up to date with any changes from the master branch. 

When you are done working on a branch, and have commited any and all changes to files to your branch, you will execute the command "git push origin nameofyourbranchhere". This will commit your changes to your branch which will be reflected on github. Once you have deemed it bug free (or at least mostly bug free :D) you may then merge your branch into the master via the interface on github.com. 

**IMPORTANT:** 
It is important to make sure that when you create a branch, you are on the master branch. Branching from another branch can make things difficult. To determine what branch you are on, and to make sure you aren't about to branch improperly, use the command "git status". This will tell you what branch you are currently on. To exit back to the master branch, or to visit an already existing branch simply use the command "git checkout nameofthebranchyouwanttovisithere". 
