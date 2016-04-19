#! /bin/bash
#
#$Author$
#$Date$
#$HeadURL$
#$Revision$

if [[ -r $1 ]]
then 
    echo exists
else
   echo not exist
   exit 0
fi 

while read line
do
    echo $line >> aa
done < $1
exit 0
