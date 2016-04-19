#! /bin/bash
#
#$Author: ee364c07 $
#$Date: 2016-01-17 04:08:28 -0500 (Sun, 17 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364c07/Prelab01/check_file.bash $
#$Revision: 85280 $

(( ! $# == 1 )) && echo "usage: ./check_file.bash <filename>" && exit 0

if [[ -e $1 ]]
then
    echo $1 exists
else
    echo $1 does not exist
fi

if [[ -d $1 ]]
then
    echo $1 is a directory
else
    echo $1 is not an directory
fi

if [[ -f $1 ]]
then
    echo $1 is a ordinary file
else
    echo $1 is not a ordinary file
fi

if [[ -r $1 ]]
then
    echo $1 is readable
else
    echo $1 is not readable
fi

if [[ -w $1 ]]
then
    echo $1 is writable
else
    echo $1 is not writable
fi

if [[ -x $1 ]]
then
    echo $1 is executable
else
    echo $1 is not executable
fi

exit 0
