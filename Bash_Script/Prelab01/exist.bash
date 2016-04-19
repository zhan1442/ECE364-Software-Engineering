#! /bin/bash
#
#$Author: ee364c07 $
#$Date: 2016-01-17 10:40:58 -0500 (Sun, 17 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364c07/Prelab01/exist.bash $
#$Revision: 85287 $



for file in $@
do
    if [[ -r $file ]]
    then
        echo "File $file is readable!"
    elif [[ ! -e $file ]]
    then
        touch $file
    fi
done

