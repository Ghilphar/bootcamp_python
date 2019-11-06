#!/bin/bash

test -d /goinfre/fgaribot/miniconda
if [ "$?" -ne "0" ] ; then
	wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O /goinfre/fgaribot/miniconda.sh
	bash /goinfre/fgaribot/miniconda.sh -b -p /goinfre/fgaribot/miniconda
	export PATH="/goinfre/fgaribot/miniconda/bin:$PATH"
fi

if [ "$?" -ne "1" ] ; then
	read -p "Python is already installed, do you want to upload it? (yes/no)" yn
    case $yn in
        [Yy]* ) bash /goinfre/fgaribot/miniconda.sh -b -u -p /goinfre/fgaribot/miniconda 
				export PATH="/goinfre/fgaribot/miniconda/bin:$PATH" exit;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
fi
