#! /bin/bash
#
#$Author: ee364c07 $
#$Date: 2016-01-17 10:40:58 -0500 (Sun, 17 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364c07/Prelab01/line_num.bash $
#$Revision: 85287 $

[[ ! $# == 1 ]] && echo "Usage: line_num.bash <filename>" && exit 0
[[ ! -r $1 ]] && echo "Cannot read $1" && exit 0
#cat -n $1 | cut -d $' ' -f 6 | cut -d $'\t' -f 1 > 1.f
#cat -n $1 | cut -d $' ' -f 6 | cut -d $'\t' -f 2 > 2.f
#paste -d : 1.f 2.f > $1
#rm 1.f
#rm 2.f

ct=0
while read line
do
    ((ct++))
    echo $ct:$line
done < $1

exit 0
