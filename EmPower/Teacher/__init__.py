"""
Why to use __init__ in python package?
> We when we put this file in each package, then whenever we run
any file from that package then first, the MyClass.py will be executed,
then the imported file will be executed. Thus,

    *  If we need some task that must be complete before executing any .py file
    then it can be written in MyClass.py file.
    * Like whenever we use any external package that needs to be installed before execution,
    we can put such commands on that file, so that when other users execute that file, if the
    imported package is absent then it'll be automatically installed.
"""

print("I am starting...")