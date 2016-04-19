#! /bin/bash
#
#$Author: ee364c07 $
#$Date: 2016-01-17 10:46:26 -0500 (Sun, 17 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364c07/Prelab01/sum.bash $
#$Revision: 85288 $

for val in $@
do
    ((sum =$sum+$val))
done
echo $sum
exit 0
