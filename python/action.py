#!/usr/bin/python
import subprocess
import sys
import string
import os
import time

kanaPath = "/do/kana/www/"

if len(sys.argv) == 2:
    actionGroup = string.split(sys.argv[1], " ")
    for actionItem in actionGroup:
        php_args = string.split(actionItem, ";")
        nb_args = len(php_args)
        # print nb_args
        if nb_args == 4:
            object = php_args[0]
            id = php_args[1]
            command = php_args[2]
            state = php_args[3]

            cmd = "php-cgi " + kanaPath + "actions.php type=action object="+object+" id="+id+" command="+command+" state="+state
            subprocess.call([cmd], shell=True)

        elif nb_args == 2:
            if php_args[0] == "wait_s":
                print "Waiting for "+php_args[1]+" seconds"
                time.sleep(int(php_args[1]))
            if php_args[0] == "wait_m":
                time_to_wait = float(php_args[1])*60
                print "Waiting for " + str(time_to_wait) + " seconds"
                time.sleep(time_to_wait)
else:
    print "No enough arguments / Wrong arguments"
